==========
py-aas-rdf 
==========

py-aas-rdf allows you to convert AAS/JSON to AAS/RDF and vice versa according to the official RDF representaiton. 

Installation
===================

``!pip install git+https://github.com/mhrimaz/py-aas-rdf.git@main --quiet``


Python Code Example
===================
.. code-block:: python

    from py_aas_rdf.models.submodel import Submodel
    from py_aas_rdf.models.property import Property
    import json
    
    graph, node = Submodel(**{"id":"test", "modelType":"Submodel"}).to_rdf()
    print(graph.serialize(format="turtle_custom"))

Notebooks
=========

* **JSON-RDF Converter:** You can use this `Jupyter Notebook <https://colab.research.google.com/drive/14myWROAKKG_0LX_U4stohioPfAIrqGhY?usp=sharing>`_ that has a simple interface to convert JSON to RDF and vice versa.
* **SPARQL Example:** You can find in this `Jupyter Notebook <https://colab.research.google.com/drive/1CwNy18p6gSNmHWd4Ng6F7z0a0XRf3WjY?usp=sharing>`_ an example that showcases how SPARQL can be used to query the Asset Administration Shell.

Citation
========

If you use this tool in your research, please cite the following paper:

.. code-block:: bibtex

    @inproceedings{rimaz2024semantic,
      title        = {Semantic Asset Administration Shell for Circular Economy},
      author       = {Rimaz, Mohammad Hossein and Plociennik, Christiane and Ruskowski, Martin},
      booktitle    = {Proceedings of the 2nd International Workshop on Knowledge Graphs for Sustainability (KG4S 2024) co-located with 21st Extended Semantic Web Conference (ESWC 2024)},
      series       = {CEUR Workshop Proceedings},
      volume       = {3753},
      pages        = {1--11},
      year         = {2024},
      publisher    = {CEUR-WS.org},
      url          = {https://ceur-ws.org/Vol-3753/paper1.pdf}
    }

Background
==========

The Asset Administration Shell (AAS) officially defines three serialization formats: JSON, XML, and RDF.
While JSON is the most widely adopted format and XML is primarily used within the AASX package format for offline
data exchange, the RDF serialization (e.g., Turtle or JSON-LD) enables the use of Semantic Web technologies such as
SPARQL, SHACL, and rule-based reasoning on a fixed, interoperable graph structure.

This one-to-one RDF representation is formalized through an
`OWL ontology <https://github.com/admin-shell-io/aas-specs-metamodel/blob/master/schemas/rdf/rdf-ontology.ttl>`_
and is accompanied by SHACL shapes to validate metamodel-related constraints (e.g., ensuring that a property
contains only one value).

Currently, official AAS SDKs do not natively support the RDF serialization. **py-aas-rdf** bridges this gap by
providing a Python tool for lossless, round-trip transformations between AAS/JSON (or AAS/XML) and AAS/RDF.


Known Issues with the Official AAS Ontology and SHACL Shapes
=============================================================

Both the official AAS OWL ontology and its accompanying SHACL shapes have known usability issues in their current
state. A key limitation is the lack of a proper mechanism for handling **ordered lists** of elements. For example,
the keys within a ``Reference`` and the elements within a ``SubmodelElementList`` have a defined order, but the
official ontology does not include a dedicated mechanism (such as ``rdf:List`` or an explicit index property) to
preserve this ordering.

To address this, the ``main`` branch of py-aas-rdf introduces an additional ``aas:index`` attribute to maintain
element ordering while remaining otherwise compliant with AAS V3.0.

Open issues related to the RDF serialization are tracked in the official specification repository:
`RDF-labeled issues on aas-specs-metamodel <https://github.com/admin-shell-io/aas-specs-metamodel/issues?q=is%3Aissue+state%3Aopen+label%3ARDF>`_.

Notable open discussions include:

- `#383 <https://github.com/admin-shell-io/aas-specs-metamodel/issues/383>`_ — Applying Linked Data principles to the RDF rendition
- `#386 <https://github.com/admin-shell-io/aas-specs-metamodel/issues/386>`_ — JSON-LD context and frame for seamless JSON/RDF interoperability
- `#422 <https://github.com/admin-shell-io/aas-specs-metamodel/issues/422>`_ — ECLASS RDF representation and its impact on AAS semantics


Branches
========

``main``
  Compliant with **AAS V3.0** and the current official RDF representation, with an additional ``aas:index``
  attribute to handle ordered elements.

``experimental``
  Contains a `new representation <https://github.com/mhrimaz/py-aas-rdf/tree/experimental>`_ that is currently
  under discussion within the **IDTA Ontology Workgroup**. This representation aims to be more natural and better
  aligned with common industry practices. It is **not yet official** and may change as the standardization process
  evolves.


Representation Comparison
=========================

To illustrate the differences between the current and proposed RDF representations, consider a minimal ``Property``
inside a ``Submodel``.

Source: AAS/JSON
----------------

.. code-block:: json

   {
     "submodels": [
       {
         "id": "something_48c66017",
         "modelType": "Submodel",
         "submodelElements": [
           {
             "idShort": "something3fdd3eb4",
             "modelType": "Property",
             "valueType": "xs:decimal"
           }
         ]
       }
     ]
   }

Current Official RDF Representation (``main`` branch)
------------------------------------------------------

This is the representation defined by the
`official AAS ontology <https://github.com/admin-shell-io/aas-specs-metamodel/blob/master/schemas/rdf/examples/generated/Property/minimal.ttl>`_.
Note how every property is a fully qualified IRI prefixed by its owning class (e.g.,
``Identifiable/id``, ``Referable/idShort``, ``Property/valueType``), and submodel elements are embedded as
blank nodes.

.. code-block:: turtle

   @prefix aas: <https://admin-shell.io/aas/3/1/> .
   @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
   @prefix xs:  <http://www.w3.org/2001/XMLSchema#> .

   <something_48c66017> rdf:type aas:Submodel ;
       <https://admin-shell.io/aas/3/1/Identifiable/id> "something_48c66017"^^xs:string ;
       <https://admin-shell.io/aas/3/1/Submodel/submodelElements> [
           rdf:type aas:Property ;
           <https://admin-shell.io/aas/3/1/Referable/idShort> "something3fdd3eb4"^^xs:string ;
           <https://admin-shell.io/aas/3/1/Property/valueType>
               <https://admin-shell.io/aas/3/1/DataTypeDefXsd/Decimal> ;
       ] ;
   .

Proposed New RDF Representation (``experimental`` branch)
----------------------------------------------------------

This is the representation under discussion in the
`IDTA Ontology Workgroup <https://github.com/mhrimaz/aas-specs/tree/WG/new-examples>`_.
Key differences from the current representation:

- **Shorter, prefix-friendly property names.** Properties use concise names (``aas-3:id``, ``aas-3:idShort``,
  ``aas-3:valueType``) instead of class-prefixed IRIs (``Identifiable/id``, ``Referable/idShort``).
- **Named nodes instead of blank nodes.** Submodel elements are identified by their own IRIs derived from the
  parent path (e.g., ``<something_48c66017/submodel-elements/something3fdd3eb4>``), making them directly
  addressable and queryable.
- **Native XSD datatypes.** Value types reference XSD datatypes directly (``xsd:decimal``) instead of
  custom AAS-specific named individuals (``DataTypeDefXsd/Decimal``).
- **Explicit ordering.** An ``aas-3:index`` property is included to preserve element order where needed.
- **Environment envelope.** An ``aas-3:Environment`` blank node groups top-level entities, mirroring
  the JSON envelope structure.
- **Version annotation.** An ``aas-3:modelVersion`` property explicitly marks the metamodel version.
- **IRI flexibility.** Entity IRIs are explicitly non-normative and can be customized to your deployment needs.

.. code-block:: turtle

   @prefix aas-3: <https://admin-shell.io/aas/3/> .
   @prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .

   <something_48c66017> a aas-3:Submodel ;
       aas-3:id "something_48c66017" ;
       aas-3:modelVersion "3.1" ;
       aas-3:submodelElements
           <something_48c66017/submodel-elements/something3fdd3eb4> .

   <something_48c66017/submodel-elements/something3fdd3eb4> a aas-3:Property ;
       aas-3:idShort "something3fdd3eb4" ;
       aas-3:index 0 ;
       aas-3:valueType xsd:decimal .

   [] a aas-3:Environment ;
       aas-3:submodel <something_48c66017> .


Design Philosophy
=================

**py-aas-rdf** implements a strict one-to-one mapping between the AAS metamodel and its RDF representation.
It is important to understand the following design choices:

- **Metamodel ontology, not a domain ontology.** The AAS ontology is a metamodel ontology as intended in the
  original specification. The resulting RDF graph is a structural representation that retains the data structures
  of the AAS. It is not intended to be a "natural" domain-specific semantic knowledge graph.

- **No OWL DL reasoning.** The representation intentionally does not utilize OWL axioms and is not designed for
  typical OWL DL reasoning. It does not import or align with external ontologies.

- **Semantic lifting is a separate concern.** You can perform an additional semantic lift to represent the same
  information in a richer, domain-specific ontology (e.g., IDO, BFO, or other upper/domain ontologies). This
  can be done manually or semi-automatically. However, if full round-trippability cannot be achieved, you must
  decide which version is the source of truth: the semantically lifted version or the original AAS content. This
  becomes a practical issue when you need to synchronize data between a pure AAS system (such as
  `Eclipse BaSyx <https://github.com/eclipse-basyx>`_ with its API and viewer) and your enriched semantic
  representation.

.. code-block:: mermaid

   graph TD
       DO["Domain Ontology (IDO, BFO, ...)"]
       AAS["Pure AAS RDF (+ ECLASS/SAMM)"]
       AASX["AASX"]
       JSON["JSON (REST API)"]

       AAS -- "Ontology Lifting" --> DO
       DO -- "Transformation" --> AAS
       AAS --- AASX
       AAS --- JSON

       style DO fill:#FFF2CC,stroke:#D6B656
       style AAS fill:#DAE8FC,stroke:#6C8EBF

- **Coexistence with other semantic artifacts.** Storing AAS data as an RDF graph makes it possible to place it
  alongside other semantic artifacts such as `SAMM Aspect Models <https://eclipse-esmf.github.io/samm-specification/>`_
  and `ECLASS <https://eclass.eu/>`_, both of which now provide RDF representations. The AAS links to these
  external vocabularies through its ``semanticId`` mechanism. This paves the way for integrated queries and
  reasoning across heterogeneous data sources.

.. code-block:: mermaid

   graph TD
       AAS["AAS"]
       ECLASS["ECLASS"]
       DM["Domain Models (TBox)/SAMM Aspects"]

       AAS -- "semantic id" --> ECLASS
       AAS -- "semantic id" --> DM

       subgraph Semantic Layer
           ECLASS
           DM
       end

       style AAS fill:#DAE8FC,stroke:#6C8EBF
       style ECLASS fill:#D5E8D4,stroke:#82B366
       style DM fill:#E1D5E7,stroke:#9673A6

