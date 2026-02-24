import json
from pathlib import Path
import pytest

from py_aas_rdf.models.aas_namespace import AASNameSpace
from py_aas_rdf.models.environment import Environment
from py_aas_rdf.models import make_uri, is_irdi
from py_aas_rdf.models.data_specification_iec_61360 import ValueList, ValueReferencePair, DataSpecificationIec61360
from py_aas_rdf.models.environment import Environment
from py_aas_rdf.models.key import Key
from py_aas_rdf.models.multi_language_property import MultiLanguageProperty
from py_aas_rdf.models.property import Property
from py_aas_rdf.models.submodel import Submodel
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
    # 1. Normalize input to a list of nodes
    if isinstance(raw_jsonld, dict) and "@graph" in raw_jsonld:
        graph_list = raw_jsonld["@graph"]
    else:
        graph_list = raw_jsonld

    # 2. Build the Lookup Map (The "Brain" of the operation)
    # This stores every node, including Blank Nodes (_:...)
    nodes = {node["@id"]: node for node in graph_list if "@id" in node}

    # 3. Identify the true root (Environment)
    root = next((n for n in graph_list if n.get("@type") == "aas-3:Environment"), graph_list[0])

    def nest_recursive(item):
        # --- BLANK NODE & IRI RESOLUTION ---
        # If the item is a string (like "_:Na5c...") AND it exists in our node map
        if isinstance(item, str) and item in nodes:
            # Pop the data out of the map and resolve its children
            node_data = nodes.pop(item)
            return nest_recursive(node_data)

        # --- REFERENCE DICT RESOLUTION ---
        # If the item is {"@id": "_:Na5c..."}
        if isinstance(item, dict) and "@id" in item:
            node_id = item["@id"]
            # If we have the data for this ID, replace the whole dict with the data
            if node_id in nodes:
                node_data = nodes.pop(node_id)
                return nest_recursive(node_data)
            # If it's a reference we don't have data for (like an external IRI),
            # keep it but remove the @id key if it's the only key
            if len(item) == 1:
                return item["@id"]

        # --- RECURSIVE DICTIONARY TRAVERSAL ---
        if isinstance(item, dict):
            new_obj = {}
            for k, v in item.items():
                if k == "@id": continue  # Drop the IDs now that they are nested
                new_obj[k] = nest_recursive(v)
            return new_obj

        # --- LIST TRAVERSAL ---
        if isinstance(item, list):
            return [nest_recursive(i) for i in item]

        return item

    # 4. Generate the final hierarchy
    tree = nest_recursive(root)

    # 5. Attach context
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

        # Step 1: Serialize with rdflib to get the initial compacted JSON
        raw_jsonld_str = graph.serialize(
            format='json-ld',
            context=context_dict
        )

        # Step 2: Call the manual framing function
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
