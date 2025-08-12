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

from enum import Enum
from typing import Any, List, Optional, Union, Literal

import pydantic
import rdflib
from pydantic import BaseModel, Field, constr

from py_aas_rdf.models.aas_namespace import AASNameSpace
from py_aas_rdf.models.has_extensions import HasExtensions
from py_aas_rdf.models.lang_string_name_type import LangStringNameType
from py_aas_rdf.models.lang_string_text_type import LangStringTextType
from py_aas_rdf.models.model_type import ModelType


class Referable(HasExtensions):
    category: Optional[constr(min_length=1, max_length=128, strip_whitespace=True)] = None
    idShort: Optional[constr(min_length=1, max_length=128, pattern=r"^[a-zA-Z][a-zA-Z0-9_]*$")] = None
    displayName: Optional[List[LangStringNameType]] = Field(None, min_length=0)
    description: Optional[List[LangStringTextType]] = Field(None, min_length=0)
    # modelType: ModelType
    # according to the openapi schema referable has model type but I removed it.
    # TODO: pattern for category and idShort

    @staticmethod
    def append_as_rdf(instance: "Referable", graph: rdflib.Graph, parent_node: rdflib.IdentifiedNode):
        # HasExtensions
        HasExtensions.append_as_rdf(instance, graph, parent_node)

        if instance.category:
            graph.add((parent_node, AASNameSpace.AAS["Referable_category"], rdflib.Literal(instance.category)))
        if instance.idShort:
            graph.add((parent_node, AASNameSpace.AAS["Referable_idShort"], rdflib.Literal(instance.idShort)))
        if instance.displayName:
            for idx, display_name_lan in enumerate(instance.displayName):
                graph.add((parent_node, AASNameSpace.AAS["Referable_displayName"], rdflib.Literal(display_name_lan.text,lang=display_name_lan.language)))

        if instance.description:
            for idx, description_lan in enumerate(instance.description):
                graph.add((parent_node, AASNameSpace.AAS["Referable_description"], rdflib.Literal(description_lan.text,lang=description_lan.language)))

    @staticmethod
    def from_rdf(graph: rdflib.Graph, subject: rdflib.IdentifiedNode):
        # HasExtension
        hasExtension = HasExtensions.from_rdf(graph, subject)

        category_value = None
        category_ref: rdflib.Literal = next(
            graph.objects(subject=subject, predicate=AASNameSpace.AAS["Referable_category"]),
            None,
        )
        if category_ref:
            category_value = category_ref.value

        id_short_value = None
        id_short_ref: rdflib.Literal = next(
            graph.objects(subject=subject, predicate=AASNameSpace.AAS["Referable_idShort"]),
            None,
        )
        if id_short_ref:
            id_short_value = id_short_ref.value

        display_name_value = []
        for display_ref in graph.objects(subject=subject, predicate=AASNameSpace.AAS["Referable_displayName"]):

            display_name_value.append(LangStringNameType(language=display_ref.language, text=display_ref.value))

        if len(display_name_value) == 0:
            display_name_value = None

        description_value = []
        for description_ref in graph.objects(subject=subject, predicate=AASNameSpace.AAS["Referable_description"]):


            description_value.append(LangStringTextType(language=description_ref.language, text=description_ref.value))

        if len(description_value) == 0:
            description_value = None
        return Referable(
            category=category_value,
            idShort=id_short_value,
            displayName=display_name_value,
            description=description_value,
            extensions=hasExtension.extensions,
        )
