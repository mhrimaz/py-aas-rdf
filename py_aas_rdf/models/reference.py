#  MIT License
#
#  Copyright (c) 2023. Mohammad Hossein Rimaz
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy of
#  this software and associated documentation files (the “Software”), to deal in
#  the Software without restriction, including without limitation the rights to use,
#  copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the
#  Software, and to permit persons to whom the Software is furnished to do so, subject
#   to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
#  INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
#  PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
#  HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
#  CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
#  OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from typing import Any, List, Optional, Union, Literal

import rdflib
from pydantic import BaseModel, Field, conlist

from py_aas_rdf.models.aas_namespace import AASNameSpace
from py_aas_rdf.models.key import Key, SubmodelKey
from py_aas_rdf.models.rdfiable import RDFiable
from py_aas_rdf.models.reference_types import ReferenceTypes


class Reference(BaseModel, RDFiable):
    type: ReferenceTypes
    # At least one key should be there
    keys: conlist(Key, min_length=1)
    # this is not a mistake, since it is a recursive structure, we need to define it in this way.
    referredSemanticId: "Reference" = None

    def to_rdf(
        self,
        graph: rdflib.Graph = None,
        parent_node: rdflib.IdentifiedNode = None,
        prefix_uri: str = "",
        base_uri: str = "",
        id_strategy: str = "",
    ) -> (rdflib.Graph, rdflib.IdentifiedNode):
        if graph == None:
            graph = rdflib.Graph()
            graph.bind("aas-3", AASNameSpace.AAS_3)
            graph.bind("aas-3-ex", AASNameSpace.AAS_3_EXTENDED)
            graph.bind("aas-iec61360-3", AASNameSpace.IEC61360_3)

        node = rdflib.BNode()
        graph.add((node, rdflib.RDF.type, AASNameSpace.AAS_3["Reference"]))

        graph.add((node, AASNameSpace.AAS_3["referenceType"], AASNameSpace.AAS_3[f"ReferenceType_{self.type.value}"]))
        for idx, key in enumerate(self.keys):
            sub_graph, created_key_node = key.to_rdf(graph=graph, parent_node=node)
            graph.add((created_key_node, AASNameSpace.AAS_3["index"], rdflib.Literal(idx)))
            graph.add((node, AASNameSpace.AAS_3["key"], created_key_node))
        if self.referredSemanticId:
            sub_graph, created_reference_node = self.referredSemanticId.to_rdf(graph=graph, parent_node=node)
            graph.add((node, AASNameSpace.AAS_3["referredSemanticId"], created_reference_node))
        return graph, node

    @staticmethod
    def from_rdf(graph: rdflib.Graph, subject: rdflib.IdentifiedNode):
        payload = {}
        key_type: rdflib.URIRef = next(
            graph.objects(subject=subject, predicate=AASNameSpace.AAS_3["referenceType"]),
            None,
        )
        payload["type"] = key_type[key_type.rfind("_") + 1 :]

        keys_content = graph.objects(subject=subject, predicate=AASNameSpace.AAS_3["key"])
        keys = {}
        for key in keys_content:
            created_key: Key = Key.from_rdf(graph, key)
            key_index_ref: rdflib.Literal = next(graph.objects(subject=key, predicate=AASNameSpace.AAS_3["index"]), None)
            keys[key_index_ref.value] = created_key
            # TODO: make sure about the order
        referred_semantic_id: rdflib.IdentifiedNode = next(
            graph.objects(subject=subject, predicate=AASNameSpace.AAS_3["referredSemanticId"]),
            None,
        )
        referred_semantic_id_created = None
        if referred_semantic_id:
            referred_semantic_id_created = Reference.from_rdf(graph, referred_semantic_id)
        payload["keys"] = [keys[i] for i in range(len(keys.items()))]
        return Reference.model_construct(
            type=ReferenceTypes(payload["type"]), keys=payload["keys"], referredSemanticId=referred_semantic_id_created
        )

