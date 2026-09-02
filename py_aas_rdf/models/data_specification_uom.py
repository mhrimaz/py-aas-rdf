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

from typing import List, Literal, Optional

import rdflib
from pydantic import BaseModel, Field, constr

from py_aas_rdf.models.aas_namespace import AASNameSpace
from py_aas_rdf.models.abstract_lang_string import AbstractLangString
from py_aas_rdf.models.model_type import ModelType
from py_aas_rdf.models.rdfiable import RDFiable


class LangStringSetUoM(AbstractLangString):
    text: constr(min_length=1, max_length=256)


class LangStringDefinitionTypeUoM(AbstractLangString):
    text: constr(min_length=1, max_length=2048)


class DataSpecificationUom(BaseModel, RDFiable):
    preferredName: List[LangStringSetUoM] = Field(..., min_length=1)
    symbol: constr(min_length=1, max_length=256)
    specificUnitID: Optional[constr(min_length=1, max_length=256)] = None
    definition: Optional[List[LangStringDefinitionTypeUoM]] = Field(None, min_length=1)
    preferredNameQuantity: Optional[List[LangStringSetUoM]] = Field(None, min_length=1)
    quantityId: Optional[constr(min_length=1, max_length=2048)] = None
    classificationSystem: Optional[constr(min_length=1, max_length=256)] = None
    classificationSystemVersion: Optional[constr(min_length=1, max_length=256)] = None
    modelType: Literal["DataSpecificationUom"] = ModelType.DataSpecificationUom.value

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
            AASNameSpace.bind_prefixes(graph)

        node = rdflib.BNode()
        graph.add((node, rdflib.RDF.type, AASNameSpace.UOM_3["DataSpecificationUom"]))
        for preferredName in self.preferredName:
            graph.add((node, AASNameSpace.UOM_3["preferredName"], rdflib.Literal(preferredName.text, lang=preferredName.language)))

        graph.add((node, AASNameSpace.UOM_3["symbol"], rdflib.Literal(self.symbol)))

        if self.specificUnitID:
            graph.add((node, AASNameSpace.UOM_3["specificUnitID"], rdflib.Literal(self.specificUnitID)))

        if self.definition:
            for definition_lang_text in self.definition:
                graph.add(
                    (
                        node,
                        AASNameSpace.UOM_3["definition"],
                        rdflib.Literal(definition_lang_text.text, lang=definition_lang_text.language),
                    )
                )

        if self.preferredNameQuantity:
            for preferredNameQuantity in self.preferredNameQuantity:
                graph.add(
                    (
                        node,
                        AASNameSpace.UOM_3["preferredNameQuantity"],
                        rdflib.Literal(preferredNameQuantity.text, lang=preferredNameQuantity.language),
                    )
                )

        if self.quantityId:
            graph.add((node, AASNameSpace.UOM_3["quantityId"], rdflib.Literal(self.quantityId)))

        if self.classificationSystem:
            graph.add((node, AASNameSpace.UOM_3["classificationSystem"], rdflib.Literal(self.classificationSystem)))

        if self.classificationSystemVersion:
            graph.add(
                (
                    node,
                    AASNameSpace.UOM_3["classificationSystemVersion"],
                    rdflib.Literal(self.classificationSystemVersion),
                )
            )

        return graph, node

    @staticmethod
    def from_rdf(graph: rdflib.Graph, subject: rdflib.IdentifiedNode):
        pref_name_langs = []
        for lang in graph.objects(subject=subject, predicate=AASNameSpace.UOM_3["preferredName"]):
            pref_name_langs.append(LangStringSetUoM(language=lang.language, text=lang.value))

        symbol = None
        symbol_ref: rdflib.Literal = next(
            graph.objects(subject=subject, predicate=AASNameSpace.UOM_3["symbol"]),
            None,
        )
        if symbol_ref:
            symbol = symbol_ref.value

        specific_unit_id = None
        specific_unit_id_ref: rdflib.Literal = next(
            graph.objects(subject=subject, predicate=AASNameSpace.UOM_3["specificUnitID"]),
            None,
        )
        if specific_unit_id_ref:
            specific_unit_id = specific_unit_id_ref.value

        definition_langs = []
        for lang in graph.objects(subject=subject, predicate=AASNameSpace.UOM_3["definition"]):
            definition_langs.append(LangStringDefinitionTypeUoM(language=lang.language, text=lang.value))
        if len(definition_langs) == 0:
            definition_langs = None

        preferred_name_quantity_langs = []
        for lang in graph.objects(subject=subject, predicate=AASNameSpace.UOM_3["preferredNameQuantity"]):
            preferred_name_quantity_langs.append(LangStringSetUoM(language=lang.language, text=lang.value))
        if len(preferred_name_quantity_langs) == 0:
            preferred_name_quantity_langs = None

        quantity_id = None
        quantity_id_ref: rdflib.Literal = next(
            graph.objects(subject=subject, predicate=AASNameSpace.UOM_3["quantityId"]),
            None,
        )
        if quantity_id_ref:
            quantity_id = quantity_id_ref.value

        classification_system = None
        classification_system_ref: rdflib.Literal = next(
            graph.objects(subject=subject, predicate=AASNameSpace.UOM_3["classificationSystem"]),
            None,
        )
        if classification_system_ref:
            classification_system = classification_system_ref.value

        classification_system_version = None
        classification_system_version_ref: rdflib.Literal = next(
            graph.objects(subject=subject, predicate=AASNameSpace.UOM_3["classificationSystemVersion"]),
            None,
        )
        if classification_system_version_ref:
            classification_system_version = classification_system_version_ref.value

        return DataSpecificationUom(
            preferredName=pref_name_langs,
            symbol=symbol,
            specificUnitID=specific_unit_id,
            definition=definition_langs,
            preferredNameQuantity=preferred_name_quantity_langs,
            quantityId=quantity_id,
            classificationSystem=classification_system,
            classificationSystemVersion=classification_system_version,
        )
