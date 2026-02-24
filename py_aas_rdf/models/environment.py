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
from __future__ import annotations
from enum import Enum
from typing import Any, List, Optional, Union, Literal

import pydantic
import rdflib
from pydantic import BaseModel, Field, constr
from rdflib import RDF, Namespace

from py_aas_rdf.models import base_64_url_encode, url_encode
from py_aas_rdf.models.aas_namespace import AASNameSpace
from py_aas_rdf.models.asset_administraion_shell import AssetAdministrationShell
from py_aas_rdf.models.concept_description import ConceptDescription
from py_aas_rdf.models.entity import Entity, EntityType
from py_aas_rdf.models.has_data_specification import HasDataSpecification
from py_aas_rdf.models.has_semantics import HasSemantics
from py_aas_rdf.models.key_types import KeyTypes
from py_aas_rdf.models.qualifable import Qualifiable
from py_aas_rdf.models.qualifier import Qualifier
from py_aas_rdf.models.rdfiable import RDFiable
from py_aas_rdf.models.referable import Referable
from py_aas_rdf.models.reference import Reference
from py_aas_rdf.models.reference_types import ReferenceTypes
from py_aas_rdf.models.submodel import Submodel
from py_aas_rdf.models.util import from_unknown_rdf


def find_child_element_by_id_short(graph: rdflib.Graph, parent_node: rdflib.URIRef, key_type: str, key_value: str) -> \
    Optional[rdflib.URIRef]:
    """Finds a child element (like a Property) within a parent (like a Submodel) by its idShort."""
    # TODO: does not handle element within SML with index reference.
    id_short_literal = rdflib.Literal(key_value)
    # Elements within Submodel
    for child_node in graph.objects(parent_node, AASNameSpace.AAS_3["submodelElements"]):
        child_id_short = graph.value(child_node, AASNameSpace.AAS_3["idShort"])
        if child_id_short == id_short_literal:
            return child_node  # Found the matching child
    # Elements within Submodel
    for child_node in graph.objects(parent_node, AASNameSpace.AAS_3["value"]):
        child_id_short = graph.value(child_node, AASNameSpace.AAS_3["idShort"])
        if child_id_short == id_short_literal:
            return child_node  # Found the matching child
    return None


class Environment(BaseModel, RDFiable):
    submodels: Optional[List[Submodel]] = None
    assetAdministrationShells: Optional[List[AssetAdministrationShell]] = None
    conceptDescriptions: Optional[List[ConceptDescription]] = None

    def to_rdf(
        self,
        graph: rdflib.Graph = None,
        parent_node: rdflib.IdentifiedNode = None,
        prefix_uri: str = "",
        base_uri: str = "",
        id_strategy: str = "",
        shortcuts: bool = True,
    ) -> (rdflib.Graph, rdflib.IdentifiedNode):
        if graph is None:
            graph = rdflib.Graph()
            graph.bind("aas-3", AASNameSpace.AAS_3)
            graph.bind("aas-3-ex", AASNameSpace.AAS_3_EXTENDED)
            graph.bind("aas-iec61360-3", AASNameSpace.IEC61360_3)
        node = rdflib.BNode()
        graph.add((node, RDF.type, AASNameSpace.AAS_3["Environment"]))
        if self.submodels:
            for idx, submodel in enumerate(self.submodels):
                _, created_sub_node = submodel.to_rdf(graph, node, prefix_uri=prefix_uri, base_uri=base_uri,
                                                      id_strategy=id_strategy)

                graph.add((node, AASNameSpace.AAS_3["submodel"], created_sub_node))

        if self.assetAdministrationShells:
            for idx, aas in enumerate(self.assetAdministrationShells):
                _, created_sub_node = aas.to_rdf(graph, node, prefix_uri=prefix_uri, base_uri=base_uri,
                                                 id_strategy=id_strategy)

                graph.add((node, AASNameSpace.AAS_3["assetAdministrationShell"], created_sub_node))

        if self.conceptDescriptions:
            for idx, cd in enumerate(self.conceptDescriptions):
                _, created_sub_node = cd.to_rdf(graph, node, prefix_uri=prefix_uri, base_uri=base_uri,
                                                id_strategy=id_strategy)

                graph.add((node, AASNameSpace.AAS_3["conceptDescription"], created_sub_node))

        # Resolve entities and construct shortcuts
        if shortcuts:
            # Link from Submodel to AAS (and vice versa)
            if self.assetAdministrationShells:
                for idx, aas in enumerate(self.assetAdministrationShells):
                    aas_node = next(graph.subjects(AASNameSpace.AAS_3["id"], rdflib.Literal(aas.id)),
                                    None)
                    if aas.submodels:
                        for submodel_ref in aas.submodels:
                            submodel_id = submodel_ref.keys[0].value
                            submodel_node = next(
                                graph.subjects(AASNameSpace.AAS_3["id"], rdflib.Literal(submodel_id)), None)
                            if submodel_node:
                                graph.add((aas_node, AASNameSpace.AAS_3["submodel"], submodel_node))
                                graph.add((submodel_node, AASNameSpace.AAS_3["assetAdministrationShell"], aas_node))

            # Link all semanticId to ConceptDescription
            for element_node, semantic_id_node in graph.subject_objects(AASNameSpace.AAS_3["semanticId"]):
                reference_object = Reference.from_rdf(graph, semantic_id_node)
                if reference_object.type == ReferenceTypes.ModelReference:
                    cd_node = next(graph.subjects(AASNameSpace.AAS_3["id"],
                                                  rdflib.Literal(reference_object.keys[0].value)),
                                   None)
                    if cd_node:
                        graph.add((element_node, AASNameSpace.AAS_3["conceptDescription"], cd_node))

                if reference_object.type == ReferenceTypes.ExternalReference:
                    # ECLASS Has RDF Resrouces. here eclass needs version. A better eclass lookup required.
                    if len(reference_object.keys) == 1 and reference_object.keys[0].value.startswith("0173"):
                        graph.add((element_node, AASNameSpace.AAS_3_EXTENDED["eclass"],
                                   rdflib.URIRef("https://eclass-cdp.com/rdf/v1/eclass/15-0/" + reference_object.keys[
                                       0].value.replace("#", "-").replace("/", "-"))))
                    if len(reference_object.keys) == 1 and reference_object.keys[0].value.startswith("0112"):
                        unversioned_irdi = reference_object.keys[0].value[0:reference_object.keys[0].value.rfind("#")]
                        graph.add((element_node, AASNameSpace.AAS_3_EXTENDED["iec_cdd"],
                                   rdflib.URIRef(
                                       "https://cdd.iec.ch/cdd/iec61360/iec61360.nsf/PropertiesAllVersions/" + unversioned_irdi.replace(
                                           "#", "%23").replace("/", "-"))))
            # I don't feel good about this code :)
            # Link all ModelReferences
            for reference_node in graph.subjects(RDF.type, AASNameSpace.AAS_3["Reference"]):
                # iterate over keys in the order
                # Reconstruct the reference object
                reference_object = Reference.from_rdf(graph, reference_node)
                # only resolve model reference
                if reference_object.type == ReferenceTypes.ModelReference:
                    current_object = None
                    # getting the root element which should have an ID
                    current_node = next(
                        graph.subjects(AASNameSpace.AAS_3["id"], rdflib.Literal(reference_object.keys[0].value)), None)

                    # Process Subsequent Keys
                    for i in range(1, len(reference_object.keys)):
                        key = reference_object.keys[i]
                        next_node = find_child_element_by_id_short(graph, current_node, key.type, key.value)
                        if next_node:
                            current_node = next_node
                    if current_node:
                        graph.add((reference_node, AASNameSpace.AAS_3_EXTENDED["resolvesTo"], current_node))
            # we don't need to handle relat
            for relationshipElement_node in graph.subjects(RDF.type, AASNameSpace.AAS_3["RelationshipElement"]):
                pass
            for annotatedRelationshipElement_node in graph.subjects(RDF.type,
                                                                    AASNameSpace.AAS_3["AnnotatedRelationshipElement"]):
                pass
            # Link all Self-managed Entity via globalAssetId
            for entity_node in graph.subjects(RDF.type, AASNameSpace.AAS_3["Entity"]):
                # iterate over keys in the order
                # Reconstruct the reference object
                entity_object = Entity.from_rdf(graph, entity_node)
                # only resolve model reference
                if entity_object.entityType == EntityType.SelfManagedEntity:

                    resolvedAASs = []
                    globalAssetId = entity_object.globalAssetId
                    # Find all AAS that have the same globalAssetId
                    if globalAssetId:
                        for assetInformation in graph.subjects(AASNameSpace.AAS_3['globalAssetId'],
                                                               rdflib.Literal(globalAssetId)):
                            for aas in graph.subjects(AASNameSpace.AAS_3['assetInformation'], assetInformation):
                                resolvedAASs.append(aas)
                    print(globalAssetId, resolvedAASs)
                    for aas in resolvedAASs:
                        graph.add((entity_node, AASNameSpace.AAS_3["assetAdministrationShell"], aas))
        return graph, node

    @staticmethod
    def from_rdf(graph: rdflib.Graph, subject: rdflib.IdentifiedNode) -> "Environment":
        # This implementation is probably wrong.
        submodels_subjects = [subject for subject in
                              graph.subjects(predicate=RDF.type, object=AASNameSpace.AAS_3["Submodel"])]
        assetadministrationshell_subjects = [subject for subject in
                                             graph.subjects(predicate=RDF.type,
                                                            object=AASNameSpace.AAS_3["AssetAdministrationShell"])]
        conceptdescription_subjects = [subject for subject in
                                       graph.subjects(predicate=RDF.type,
                                                      object=AASNameSpace.AAS_3["ConceptDescription"])]
        shells = []
        for subject in assetadministrationshell_subjects:
            shells.append(AssetAdministrationShell.from_rdf(graph, subject))
        if len(shells) == 0:
            shells = None
        submodels = []
        for subject in submodels_subjects:
            submodels.append(Submodel.from_rdf(graph, subject))
        if len(submodels) == 0:
            submodels = None
        concept_descriptions = []
        for subject in conceptdescription_subjects:
            concept_descriptions.append(ConceptDescription.from_rdf(graph, subject))
        if len(concept_descriptions) == 0:
            concept_descriptions = None
        return Environment(
            submodels=submodels,
            assetAdministrationShells=shells,
            conceptDescriptions=concept_descriptions
        )
