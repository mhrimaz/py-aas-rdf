import json
from pathlib import Path
import pytest
import rdflib

from py_aas_rdf.models.aas_namespace import AASNameSpace
from py_aas_rdf.models.environment import Environment
from py_aas_rdf.models import make_uri, is_irdi
from py_aas_rdf.models.data_specification_iec_61360 import ValueList, ValueReferencePair, DataSpecificationIec61360
from py_aas_rdf.models.environment import Environment
from py_aas_rdf.models.key import Key
from py_aas_rdf.models.multi_language_property import MultiLanguageProperty
from py_aas_rdf.models.property import Property
from py_aas_rdf.models.submodel import Submodel


from pyshacl import validate
# Root path configuration
REPO_ROOT = Path(r"C:\Users\hossein.rimaz\repos\aas-specs")
JSON_BASE = REPO_ROOT / "schemas" / "json" / "examples" / "generated"
RDF_BASE = REPO_ROOT / "schemas" / "rdf" / "examples" / "generated"


def get_json_examples():
    """Finds all json files in the generated examples folder."""
    if not JSON_BASE.exists():
        print(f"Warning: Path not found {JSON_BASE}")
        return []
    return list(JSON_BASE.rglob("*.json"))


import json


def frame_rdf_to_tree(raw_jsonld, context):
    """
    Takes JSON-LD data serialized with auto_compact=True (all nodes flat, prefixed names)
    and a JSON-LD context dict. Compacts property names, resolves enum/vocab values,
    nests blank nodes, and returns a tree rooted at the Environment node.
    """
    AAS = "https://admin-shell.io/aas/3/"
    IEC = "https://admin-shell.io/DataSpecificationTemplates/DataSpecificationIec61360/3/"

    # --- 1. Normalize input to a flat list of nodes ---
    if isinstance(raw_jsonld, dict) and "@graph" in raw_jsonld:
        graph_list = raw_jsonld["@graph"]
    elif isinstance(raw_jsonld, list):
        graph_list = raw_jsonld
    else:
        graph_list = [raw_jsonld]

    # --- 2. Build IRI → short name mapping from context ---
    iri_to_name = {}        # full IRI → context short name
    name_to_config = {}     # short name → context definition dict

    for name, defn in context.items():
        if name.startswith("@"):
            continue
        if isinstance(defn, str):
            continue  # prefix alias like "aas": "https://..."
        if isinstance(defn, dict) and "@id" in defn:
            iri = defn["@id"]
            if iri.startswith("aas:"):
                iri = AAS + iri[4:]
            elif iri.startswith("iec61360:"):
                iri = IEC + iri[9:]
            iri_to_name[iri] = name
            name_to_config[name] = defn

    def expand_prefix(s):
        """Expand any known prefix to full IRI."""
        if s.startswith("aas-3:"):
            return AAS + s[6:]
        if s.startswith("aas-iec61360-3:"):
            return IEC + s[15:]
        if s.startswith("aas:"):
            return AAS + s[4:]
        if s.startswith("iec61360:"):
            return IEC + s[9:]
        return s

    def compact_prop_name(k):
        """Compact a prefixed property name to its context short name."""
        full = expand_prefix(k)
        if full in iri_to_name:
            return iri_to_name[full]
        # @vocab fallback: any IRI under the vocab base gets its local name
        vocab = context.get("@vocab", "")
        if vocab and full.startswith(vocab):
            return full[len(vocab):]
        return k

    def resolve_vocab_value(iri_str, local_ctx):
        """Resolve an IRI to a short vocab name using a local @context mapping."""
        expanded = expand_prefix(iri_str)
        for vname, vdefn in local_ctx.items():
            if isinstance(vdefn, dict) and "@id" in vdefn:
                viri = expand_prefix(vdefn["@id"])
                if expanded == viri:
                    return vname
        # Fallback: use the local name after the last /
        return expanded.rsplit("/", 1)[-1] if "/" in expanded else expanded

    def compact_type_value(t):
        """Compact a @type value (class IRI) to its local name."""
        if isinstance(t, list):
            return compact_type_value(t[0]) if t else None
        expanded = expand_prefix(t) if isinstance(t, str) else t
        if isinstance(expanded, str):
            if expanded.startswith(AAS):
                return expanded[len(AAS):]
            if expanded.startswith(IEC):
                return expanded[len(IEC):]
        return t

    def compact_single_value(val, config):
        """Compact a single property value based on its context config."""
        type_def = config.get("@type") if isinstance(config, dict) else None
        local_ctx = config.get("@context", {}) if isinstance(config, dict) else {}

        # @vocab with local context → resolve enum value
        if type_def == "@vocab" and local_ctx:
            if isinstance(val, dict) and "@id" in val:
                return resolve_vocab_value(val["@id"], local_ctx)
            if isinstance(val, str):
                return resolve_vocab_value(val, local_ctx)

        # @type: @id → extract the IRI string
        if type_def == "@id":
            if isinstance(val, dict) and "@id" in val:
                return val["@id"]

        # Language-tagged literal → {language, text} object
        if isinstance(val, dict) and "@value" in val and "@language" in val:
            return {"language": val["@language"], "text": val["@value"]}

        # Plain literal with @value wrapper
        if isinstance(val, dict) and "@value" in val:
            return val["@value"]

        return val

    def compact_prop_value(v, config):
        """Compact a property value, handling containers (@set, @list, @language)."""
        container = config.get("@container") if isinstance(config, dict) else None

        # Transform individual values
        if isinstance(v, list):
            result = [compact_single_value(item, config) for item in v]
        else:
            result = compact_single_value(v, config)

        # Ensure container compliance
        if container in ("@set", "@list", "@language"):
            if not isinstance(result, list):
                result = [result]

        return result

    # --- 3. Compact all nodes ---
    def compact_node(node):
        result = {}
        for k, v in node.items():
            if k == "@id":
                result["@id"] = v
                continue
            if k == "@type":
                result["modelType"] = compact_type_value(v)
                continue
            short = compact_prop_name(k)
            config = name_to_config.get(short, {})
            result[short] = compact_prop_value(v, config)
        return result

    compacted = [compact_node(n) for n in graph_list]

    # --- 4. Build node map by @id ---
    nodes = {n["@id"]: n for n in compacted if "@id" in n}

    # --- 5. Identify root (Environment) ---
    root = next((n for n in compacted if n.get("modelType") == "Environment"), compacted[0])

    # --- 6. Recursive nesting ---
    def nest(item):
        # String that matches a node ID → resolve to that node's data
        if isinstance(item, str) and item in nodes:
            return nest(nodes.pop(item))

        # Dict with @id → resolve if we have data for it
        if isinstance(item, dict) and "@id" in item:
            nid = item["@id"]
            if nid in nodes:
                return nest(nodes.pop(nid))
            # Bare reference we don't have data for → return the IRI string
            if len(item) == 1:
                return nid

        # Recurse into dictionaries (drop @id since nodes are now nested)
        if isinstance(item, dict):
            result = {}
            for k, v in item.items():
                if k == "@id":
                    continue
                result[k] = nest(v)
            return result

        # Recurse into lists
        if isinstance(item, list):
            return [nest(i) for i in item]

        return item

    tree = nest(root)
    return {"@context": context, **tree}
@pytest.mark.parametrize("json_file", get_json_examples(), ids=lambda p: str(p.relative_to(JSON_BASE)))
def test_json_rdf_roundtrip(json_file: Path):
    # 1. Determine the output path (mirroring the folder structure)
    relative_path = json_file.relative_to(JSON_BASE)
    output_ttl_path = RDF_BASE / relative_path.with_suffix(".ttl")
    output_jsonld_raw_path = RDF_BASE / relative_path.with_suffix(".jsonld-raw.json")
    output_jsonld_with_context_path = RDF_BASE / relative_path.with_suffix(".jsonld-with-context.json")

    # Ensure directory exists
    output_ttl_path.parent.mkdir(parents=True, exist_ok=True)

    # 2. Load JSON source
    with open(json_file, "r", encoding="utf-8") as f:
        original_dict = json.load(f)

    # 3. Instantiate model and convert to RDF
    aas_env = Environment(**original_dict)
    graph, created_node = aas_env.to_rdf()



    # 4. Save the RDF (Turtle) to the mirrored folder
    with open(output_ttl_path, "w", encoding="utf-8") as f:
        f.write("# IRI of entities are not normative and can be modified according to your needs.\n")
        f.write(graph.serialize(format='turtle'))

    with open(output_jsonld_raw_path, "w", encoding="utf-8") as f:
        f.write(graph.serialize(format='json-ld', auto_compact=True))

    with open(output_jsonld_with_context_path, "w", encoding="utf-8") as f:
        # Get your context dictionary
        context_dict = json.loads(AASNameSpace.AAS_JSON_LD_CONTEXT_3).get("@context")

        # Step 1: Serialize with auto_compact to get ALL nodes (including blank nodes)
        raw_jsonld_str = graph.serialize(
            format='json-ld',
            auto_compact=True
        )

        # Step 2: Compact property names + nest blank nodes using context
        raw_data = json.loads(raw_jsonld_str)
        framed_json = frame_rdf_to_tree(raw_data, context_dict)

        # Step 3: Write the pretty-printed, framed JSON to the file
        json.dump(framed_json, f, indent=4, sort_keys=True)


    # Convert RDF back to Python Object
    re_created_env = Environment.from_rdf(graph, created_node)

    if aas_env != re_created_env:
        with open(output_ttl_path, "w", encoding="utf-8") as f:
            f.write("# Roundtrip failed")
            f.write(graph.serialize(format='turtle'))

    # todo: validate the generated graph against shacl shape
    SHACL_GRAPH = rdflib.Graph()
    SHACL_GRAPH.parse(data=AASNameSpace.AAS_SHACL_3, format="turtle")

    # Run the validation
    conforms, results_graph, results_text = validate(
        data_graph=graph,
        shacl_graph=SHACL_GRAPH,
        shacl_graph_format="turtle",  # Update this if your string is xml, json-ld, etc.
        inference="rdfs",  # Optional: use if your shape relies on subclassing
        advanced=True,
        debug=False
    )
    if conforms==False:
        with open(output_ttl_path, "w", encoding="utf-8") as f:
            print(f"validation failed for {relative_path}")
            f.write("# SHACL Validation failed")
            f.write(results_text)
            f.write("# Data")
            f.write(graph.serialize(format='turtle'))
    # Comparison logic
    # First: Compare model objects directly
    assert aas_env == re_created_env

    # Second: Compare serialized output
    # model_dump replaces dict(); model_dump_json replaces json()
    # exclude_none=True removes nulls, by_alias=True uses 'idShort' instead of 'id_short'
    roundtripped_dict = re_created_env.model_dump_json(exclude_none=True)

    # Re-verify against the original loaded JSON
    assert re_created_env == aas_env




def test_single_file_roundtrip_and_save():
    """
    Test a single file roundtrip:
    1. Load JSON -> Environment Object
    2. Environment Object -> RDF (Save to file with suffix)
    3. RDF -> Environment Object (Re-created)
    4. Assert Original == Re-created
    """
    # 1. Configuration: Path to your specific target file
    target_file = Path(
        r"C:\Users\hossein.rimaz\My Drive\Projects\AAS IDTA\DemoData\RUB\Vera-corrected-20260213.json")
    skolem_prefix = "urn:well-known:genid:"
    if not target_file.exists():
        pytest.fail(f"Source file not found: {target_file}")

    # Define output path: .../DigitalReference_Example.json.py-aas-rdf.ttl
    output_ttl_path = target_file.parent / (target_file.name + ".py-aas-rdf.ttl")

    # 2. Load Original JSON
    with open(target_file, "r", encoding="utf-8") as f:
        original_dict = json.load(f)

    # 3. Step 1: JSON -> Python Object
    aas_env = Environment(**original_dict)

    # 4. Step 2: Python Object -> RDF
    graph, created_node = aas_env.to_rdf()
    skolemized_graph = graph.skolemize(basepath=skolem_prefix)
    skolemized_graph.bind("aas-3", AASNameSpace.AAS_3)
    skolemized_graph.bind("aas-3-ex", AASNameSpace.AAS_3_EXTENDED)
    skolemized_graph.bind("aas-iec61360-3", AASNameSpace.IEC61360_3)
    # 4. Save the Skolemized RDF
    with open(output_ttl_path, "w", encoding="utf-8") as f:
        f.write(f"# Skolemized with prefix: {skolem_prefix}\n")
        f.write(skolemized_graph.serialize(format='turtle'))


    print(f"\n[1/3] RDF saved to: {output_ttl_path.name}")

    # 6. Step 3: RDF -> Python Object (The "Roundtrip" part)
    re_created_env = Environment.from_rdf(graph, created_node)
    print("[2/3] RDF successfully parsed back into Python object.")

    # 7. Step 4: Verification / Assertions
    # Check 1: Direct object equality (uses __eq__ logic)
    assert aas_env == re_created_env, "Roundtrip failed: The re-created Environment object is not equal to the original."

    # Check 2: Data comparison (helps identify exactly where the mismatch is)
    original_dump = aas_env.model_dump(exclude_none=True)
    recreated_dump = re_created_env.model_dump(exclude_none=True)

    if original_dump != recreated_dump:
        # If this fails, pytest will show a beautiful diff of the two dictionaries
        assert original_dump == recreated_dump

    print("[3/3] Roundtrip verified: Data matches perfectly!")
