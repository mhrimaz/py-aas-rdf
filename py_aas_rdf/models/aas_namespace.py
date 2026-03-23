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

import rdflib
from rdflib.namespace import DefinedNamespace, Namespace


class AASNameSpace:
    AAS_3 = Namespace("https://admin-shell.io/aas/3/")
    AAS_3_EXTENDED = Namespace("https://admin-shell.io/aas/3/extended/")
    IEC61360_3 = Namespace("https://admin-shell.io/DataSpecificationTemplates/DataSpecificationIec61360/3/")
    # Ontology & SHACL are WiP
    AAS_ONTOLOGY_3_1 = """
@prefix aas-3: <https://admin-shell.io/aas/3/> .
@prefix aas-iec61360-3: <https://admin-shell.io/DataSpecificationTemplates/DataSpecificationIec61360/3/> .
@prefix aas-3-ex: <https://admin-shell.io/aas/3/extended/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix dct: <http://purl.org/dc/terms/> .

aas-3: a owl:Ontology ;
    dct:title "Asset Administration Shell Metamodel Ontology"@en ;
    rdfs:label "AAS ontology"@en ;
    dct:description "Asset Administration Shell Metamodel Ontology contains the definition of metamodel elements and how they are connected to each other"@en ;
    dct:license <https://creativecommons.org/licenses/by/4.0/> ;
    dct:modified "2025-10-08"^^xsd:date ;
    dct:publisher <https://industrialdigitaltwin.org/> ;
    owl:versionInfo "3.1" ;
    rdfs:comment "This ontology represents the data model for the Asset Administration Shell according to the specification version V3.1."@en ;
    rdfs:isDefinedBy <https://admin-shell.io/aas/3/> ;
.

###  https://admin-shell.io/aas/3/AasSubmodelElements
###  https://admin-shell.io/aas/3/AasSubmodelElements/AnnotatedRelationshipElement
###  https://admin-shell.io/aas/3/AasSubmodelElements/BasicEventElement
###  https://admin-shell.io/aas/3/AasSubmodelElements/Blob
###  https://admin-shell.io/aas/3/AasSubmodelElements/Capability
###  https://admin-shell.io/aas/3/AasSubmodelElements/DataElement
###  https://admin-shell.io/aas/3/AasSubmodelElements/Entity
###  https://admin-shell.io/aas/3/AasSubmodelElements/EventElement
###  https://admin-shell.io/aas/3/AasSubmodelElements/File
###  https://admin-shell.io/aas/3/AasSubmodelElements/MultiLanguageProperty
###  https://admin-shell.io/aas/3/AasSubmodelElements/Operation
###  https://admin-shell.io/aas/3/AasSubmodelElements/Property
###  https://admin-shell.io/aas/3/AasSubmodelElements/Range
###  https://admin-shell.io/aas/3/AasSubmodelElements/ReferenceElement
###  https://admin-shell.io/aas/3/AasSubmodelElements/RelationshipElement
###  https://admin-shell.io/aas/3/AasSubmodelElements/SubmodelElement
###  https://admin-shell.io/aas/3/AasSubmodelElements/SubmodelElementCollection
###  https://admin-shell.io/aas/3/AasSubmodelElements/SubmodelElementList
# removed intentionally as we simply use aas-3:Range instead of yet another IRI to denote this type

###  https://admin-shell.io/aas/3/AbstractLangString
###  https://admin-shell.io/aas/3/AbstractLangString_language
###  was https://admin-shell.io/aas/3/AbstractLangString_text
# removed because redundant, we use rdfLangString

###  was https://admin-shell.io/aas/3/AdministrativeInformation
aas-3:AdministrativeInformation a owl:Class ;
    rdfs:subClassOf aas-3:HasDataSpecification ;
    rdfs:label "Administrative Information"@en ;
    rdfs:comment "Administrative meta-information for an element like version information."@en ;
.

###  was https://admin-shell.io/aas/3/AdministrativeInformation/creator
aas-3:creator a owl:ObjectProperty ;
    rdfs:label "has creator"@en ;
    rdfs:domain aas-3:AdministrativeInformation ;
    rdfs:range aas-3:Reference ;
    rdfs:comment "The subject ID of the subject responsible for making the element."@en ;
.

###  was https://admin-shell.io/aas/3/AdministrativeInformation/revision
aas-3:revision a owl:DatatypeProperty ;
    rdfs:label "has revision"@en ;
    rdfs:domain aas-3:AdministrativeInformation ;
    rdfs:range xsd:string ;
    rdfs:comment "Revision of the element."@en ;
.

###  was https://admin-shell.io/aas/3/AdministrativeInformation/templateId
aas-3:templateId a owl:DatatypeProperty ;
    rdfs:label "has template ID"@en ;
    rdfs:domain aas-3:AdministrativeInformation ;
    rdfs:range xsd:string ;
    rdfs:comment "Identifier of the template that guided the creation of the element."@en ;
.

###  was https://admin-shell.io/aas/3/AdministrativeInformation/version
aas-3:version a owl:DatatypeProperty ;
    rdfs:label "has version"@en ;
    rdfs:domain aas-3:AdministrativeInformation ;
    rdfs:range xsd:string ;
    rdfs:comment "Version of the element."@en ;
.

###  was https://admin-shell.io/aas/3/AnnotatedRelationshipElement
aas-3:AnnotatedRelationshipElement a owl:Class , owl:NamedIndividual ;
    rdfs:subClassOf aas-3:RelationshipElement ;
    rdfs:label "Annotated Relationship Element"@en ;
    rdfs:comment "An annotated relationship element is a relationship element that can be annotated with additional data elements."@en ;
.

###  was https://admin-shell.io/aas/3/annotations
# use singular form
aas-3:annotation a owl:ObjectProperty ;
    rdfs:label "has annotation"@en ;
    rdfs:domain aas-3:AnnotatedRelationshipElement ;
    rdfs:range aas-3:DataElement ;
    rdfs:comment "A data element that represents an annotation that holds for the relationship between the two elements"@en ;
.

###  was https://admin-shell.io/aas/3/AssetAdministrationShell
aas-3:AssetAdministrationShell a owl:Class ;
    rdfs:subClassOf aas-3:Identifiable ;
    rdfs:subClassOf aas-3:HasDataSpecification ;
    rdfs:label "Asset Administration Shell"@en ;
    rdfs:comment "An asset administration shell."@en ;
.

###  was https://admin-shell.io/aas/3/assetInformation
aas-3:assetInformation a owl:ObjectProperty ;
    rdfs:label "has asset information"@en ;
    rdfs:domain aas-3:AssetAdministrationShell ;
    rdfs:range aas-3:AssetInformation ;
    rdfs:comment "Meta-information about the asset the AAS is representing."@en ;
.

###  was https://admin-shell.io/aas/3/derivedFrom
aas-3:derivedFrom a owl:ObjectProperty ;
    rdfs:label "has derived from"@en ;
    rdfs:domain aas-3:AssetAdministrationShell ;
    rdfs:range aas-3:Reference ;
    rdfs:comment "The reference to the AAS the AAS was derived from."@en ;
.

###  was https://admin-shell.io/aas/3/submodels
# renamed to submodelReference
aas-3:submodelReference a owl:ObjectProperty ;
    rdfs:label "has submodel reference"@en ;
    rdfs:domain aas-3:AssetAdministrationShell ;
    rdfs:range aas-3:Reference ;
    rdfs:comment "Reference to submodels of the AAS."@en ;
.

###  was https://admin-shell.io/aas/3/AssetInformation
aas-3:AssetInformation a owl:Class ;
    rdfs:label "Asset Information"@en ;
    rdfs:comment "In 'AssetInformation' identifying meta data of the asset that is represented by an AAS is defined."@en ;
.

###  was https://admin-shell.io/aas/3/assetKind
aas-3:assetKind a owl:ObjectProperty ;
    rdfs:label "has asset kind"@en ;
    rdfs:domain aas-3:AssetInformation ;
    rdfs:range aas-3:AssetKind ;
    rdfs:comment "Denotes whether the Asset is of kind 'Type' or 'Instance' or 'Role' or 'Not Applicable'."@en ;
.

###  was https://admin-shell.io/aas/3/assetType
aas-3:assetType a owl:DatatypeProperty ;
    rdfs:label "has asset type"@en ;
    rdfs:domain aas-3:AssetInformation ;
    rdfs:range xsd:string ;
    rdfs:comment "In case 'assetKind' is applicable the 'assetType' is the asset ID of the type asset of the asset under consideration as identified by 'globalAssetId'."@en ;
.

###  was https://admin-shell.io/aas/3/defaultThumbnail
aas-3:defaultThumbnail a owl:ObjectProperty ;
    rdfs:label "has default thumbnail"@en ;
    rdfs:domain aas-3:AssetInformation ;
    rdfs:range aas-3:Resource ;
    rdfs:comment "Thumbnail of the asset represented by the Asset Administration Shell."@en ;
.

###  was https://admin-shell.io/aas/3/globalAssetId
aas-3:globalAssetId a owl:DatatypeProperty ;
    rdfs:label "has global asset ID"@en ;
    rdfs:domain [ a owl:Class ;
                       owl:unionOf ( aas-3:AssetInformation aas-3:Entity ) ] ;
    rdfs:range xsd:string ;
    rdfs:comment "Global identifier of the represented asset."@en ;
.

###  was https://admin-shell.io/aas/3/specificAssetIds
#singular form
aas-3:specificAssetId a owl:ObjectProperty ;
    rdfs:label "has specific asset ID"@en ;
    rdfs:domain [ a owl:Class ;
                       owl:unionOf ( aas-3:AssetInformation aas-3:Entity ) ] ;
    rdfs:range aas-3:SpecificAssetId ;
    rdfs:comment "Additional domain-specific, typically proprietary identifier for the asset like e.g., serial number etc."@en ;
.

###  was https://admin-shell.io/aas/3/AssetKind
aas-3:AssetKind a owl:Class ;
    rdfs:label "Asset Kind"@en ;
    rdfs:comment "Enumeration for denoting whether an asset is a type asset or an instance asset."@en ;
    owl:oneOf (
        aas-3:AssetKind_Instance
        aas-3:AssetKind_NotApplicable
        aas-3:AssetKind_Type
        aas-3:AssetKind_Role
    ) ;
.

###  was https://admin-shell.io/aas/3/AssetKind/Instance
aas-3:AssetKind_Instance a aas-3:AssetKind ;
    rdfs:label "Instance"@en ;
    rdfs:comment "Instance asset"@en ;
.

###  was https://admin-shell.io/aas/3/AssetKind/NotApplicable
aas-3:AssetKind_NotApplicable a aas-3:AssetKind ;
    rdfs:label "Not Applicable"@en ;
    rdfs:comment "Neither a type asset nor an instance asset"@en ;
.

###  was https://admin-shell.io/aas/3/AssetKind/Type
aas-3:AssetKind_Type a aas-3:AssetKind ;
    rdfs:label "Type"@en ;
    rdfs:comment "Type asset"@en ;
.

###  was https://admin-shell.io/aas/3/AssetKind/Role
aas-3:AssetKind_Role a aas-3:AssetKind ;
    rdfs:label "Role"@en ;
    rdfs:comment "Role asset"@en ;
.

###  was https://admin-shell.io/aas/3/BasicEventElement
aas-3:BasicEventElement a owl:Class, owl:NamedIndividual ;
    rdfs:subClassOf aas-3:EventElement ;
    rdfs:label "Basic Event Element"@en ;
    rdfs:comment "A basic event element."@en ;
.

###  was https://admin-shell.io/aas/3/BasicEventElement/direction
aas-3:direction a owl:ObjectProperty ;
    rdfs:label "has direction"@en ;
    rdfs:domain aas-3:BasicEventElement ;
    rdfs:range aas-3:Direction ;
    rdfs:comment "Direction of event."@en ;
.

###  was https://admin-shell.io/aas/3/BasicEventElement/lastUpdate
# UTC check should be in SHACL
aas-3:lastUpdate a owl:DatatypeProperty ;
    rdfs:label "has last update"@en ;
    rdfs:domain aas-3:BasicEventElement ;
    rdfs:range xsd:dateTimeStamp ;
    rdfs:comment "Timestamp in UTC, when the last event was received (input direction) or sent (output direction)."@en ;
.

###  was https://admin-shell.io/aas/3/BasicEventElement/maxInterval
# changed the datatype to xsd:duration instead of string
aas-3:maxInterval a owl:DatatypeProperty ;
    rdfs:label "has max interval"@en ;
    rdfs:domain aas-3:BasicEventElement ;
    rdfs:range xsd:duration ;
    rdfs:comment "For input direction: not applicable."@en ;
.

###  was https://admin-shell.io/aas/3/BasicEventElement/messageBroker
aas-3:messageBroker a owl:ObjectProperty ;
    rdfs:label "has message broker"@en ;
    rdfs:domain aas-3:BasicEventElement ;
    rdfs:range aas-3:Reference ;
    rdfs:comment "Information, which outer message infrastructure shall handle messages for the 'EventElement'. Refers to a 'Submodel', 'SubmodelElementList', 'SubmodelElementCollection' or 'Entity', which contains 'DataElement''s describing the proprietary specification for the message broker."@en ;
.

###  was https://admin-shell.io/aas/3/BasicEventElement/messageTopic
aas-3:messageTopic a owl:DatatypeProperty ;
    rdfs:label "has message topic"@en ;
    rdfs:domain aas-3:BasicEventElement ;
    rdfs:range xsd:string ;
    rdfs:comment "Information for the outer message infrastructure for scheduling the event to the respective communication channel."@en ;
.

###  was https://admin-shell.io/aas/3/BasicEventElement/minInterval
aas-3:minInterval a owl:DatatypeProperty ;
    rdfs:label "has min interval"@en ;
    rdfs:domain aas-3:BasicEventElement ;
    rdfs:range xsd:duration ;
    rdfs:comment "For input direction, reports on the maximum frequency, the software entity behind the respective Referable can handle input events."@en ;
.

###  was https://admin-shell.io/aas/3/BasicEventElement/observed
aas-3:observed a owl:ObjectProperty ;
    rdfs:label "has observed"@en ;
    rdfs:domain aas-3:BasicEventElement ;
    rdfs:range aas-3:Reference ;
    rdfs:comment "Reference to the 'Referable', which defines the scope of the event. Can be 'AssetAdministrationShell', 'Submodel', or 'SubmodelElement'."@en ;
.

###  was https://admin-shell.io/aas/3/BasicEventElement/state
aas-3:state a owl:ObjectProperty ;
    rdfs:label "has state"@en ;
    rdfs:domain aas-3:BasicEventElement ;
    rdfs:range aas-3:StateOfEvent ;
    rdfs:comment "State of event."@en ;
.

###  was https://admin-shell.io/aas/3/Blob
aas-3:Blob a owl:Class, owl:NamedIndividual ;
    rdfs:subClassOf aas-3:DataElement ;
    rdfs:label "Blob"@en ;
    rdfs:comment "A 'Blob' is a data element that represents a file that is contained with its source code in the value attribute."@en ;
.

###  was https://admin-shell.io/aas/3/Blob/contentType
aas-3:contentType a owl:DatatypeProperty ;
    rdfs:label "has content type"@en ;
    rdfs:domain [ a owl:Class ;
                       owl:unionOf ( aas-3:Blob aas-3:File aas-3:Resource ) ] ;
    rdfs:range xsd:string ;
    rdfs:comment "Content type."@en ;
.



# Notice that value is a generic rdf:Property or declared as both owl:DatatypeProperty , owl:ObjectProperty
# marking something as a owl:DatatypeProperty , owl:ObjectProperty is against OWL-DL. In OWL-FULL this is equivalent
# to marking something as rdf:Property
# https://www.w3.org/TR/owl-ref/ - Section 4 --> NOTE: In OWL Full, object properties and datatype properties are not disjoint.
# Because data values can be treated as individuals, datatype properties are effectively
# subclasses of object properties. In OWL Full owl:ObjectProperty is equivalent to rdf:Property
# In practice, this mainly has consequences for the use of owl:InverseFunctionalProperty.
# See also the OWL Full characterization in Sec. 8.1.
# Note: In AAS, we don't do OWL reasoning, as we deal with a an RDF graph and no complex owl axiom can exist
# as we don't have OWL-Ontological realism. Rule-based reasoning is the suitable reasoning approach for AAS.
# otherwise, a re-semantic-lift required to transfrom pure AAS/RDF graph into an ontologically realistic OWL-TBOX/ABOX
# RDF Graph (which you can't ever do it in a generic way, an only opinionated with information loss and sync capability)
# both word can't coexist
# Domain and range validation will happen in SHACL
aas-3:value a owl:ObjectProperty, owl:DatatypeProperty  ;
    rdfs:label "has value"@en ;
    rdfs:comment "The value of the element."@en ;
.

###  was https://admin-shell.io/aas/3/Blob/value
# replaced with generic aas-3:value

###  was https://admin-shell.io/aas/3/Capability
aas-3:Capability a owl:Class, owl:NamedIndividual ;
    rdfs:subClassOf aas-3:SubmodelElement ;
    rdfs:label "Capability"@en ;
    rdfs:comment "A capability is the implementation-independent description of the potential of an asset to achieve a certain effect in the physical or virtual world."@en ;
.

###  was https://admin-shell.io/aas/3/ConceptDescription
aas-3:ConceptDescription a owl:Class ;
    rdfs:subClassOf aas-3:Identifiable ;
    rdfs:subClassOf aas-3:HasDataSpecification ;
    rdfs:label "Concept Description"@en ;
    rdfs:comment "The semantics of a property or other elements that may have a semantic description is defined by a concept description."@en ;
.

###  was https://admin-shell.io/aas/3/ConceptDescription/isCaseOf
aas-3:isCaseOf a owl:ObjectProperty ;
    rdfs:label "has is case of"@en ;
    rdfs:domain aas-3:ConceptDescription ;
    rdfs:range aas-3:Reference ;
    rdfs:comment "Reference to an external definition the concept is compatible to or was derived from."@en ;
.

###  was https://admin-shell.io/aas/3/DataElement
aas-3:DataElement a owl:Class, owl:NamedIndividual ;
    rdfs:subClassOf aas-3:SubmodelElement ;
    rdfs:label "Data Element"@en ;
    rdfs:comment "A data element is a submodel element that is not further composed out of other submodel elements."@en ;
.

###  was https://admin-shell.io/aas/3/DataSpecificationContent
aas-3:DataSpecificationContent a owl:Class ;
    rdfs:label "Data Specification Content"@en ;
    rdfs:comment "Data specification content is part of a data specification template and defines which additional attributes shall be added to the element instance that references the data specification template and meta information about the template itself."@en ;
.

###  was https://admin-shell.io/aas/3/DataSpecificationIec61360
# rather than choosing <https://admin-shell.io/DataSpecificationTemplates/DataSpecificationIec61360>
# which requires additional namespace, templates live in aas namespace, as they should be unique anyway
aas-3:DataSpecificationIec61360 a owl:Class ;
    rdfs:subClassOf aas-3:DataSpecificationContent ;
    rdfs:label "Data Specification IEC 61360"@en ;
    rdfs:comment "Content of data specification template for concept descriptions for properties, values and value lists conformant to IEC 61360."@en ;
.

###  was https://admin-shell.io/aas/3/DataSpecificationIec61360/dataType
aas-iec61360-3:dataType a owl:ObjectProperty ;
    rdfs:label "has data type"@en ;
    rdfs:domain aas-3:DataSpecificationIec61360 ;
    rdfs:range aas-iec61360-3:DataTypeIec61360 ;
    rdfs:comment "Data Type"@en ;
.

###  was https://admin-shell.io/aas/3/DataSpecificationIec61360/definition
aas-iec61360-3:definition a owl:DatatypeProperty ;
    rdfs:label "has definition"@en ;
    rdfs:domain aas-3:DataSpecificationIec61360 ;
    rdfs:range rdf:langString ;
    rdfs:comment "Definition in different languages"@en ;
.

###  was https://admin-shell.io/aas/3/DataSpecificationIec61360/levelType
aas-iec61360-3:levelType a owl:ObjectProperty ;
    rdfs:label "has level type"@en ;
    rdfs:domain aas-3:DataSpecificationIec61360 ;
    rdfs:range aas-iec61360-3:LevelType ;
    rdfs:comment "Set of levels."@en ;
.

###  was https://admin-shell.io/aas/3/DataSpecificationIec61360/preferredName
aas-iec61360-3:preferredName a owl:DatatypeProperty ;
    rdfs:label "has preferred name"@en ;
    rdfs:domain aas-3:DataSpecificationIec61360 ;
    rdfs:range rdf:langString ;
    rdfs:comment "Preferred name"@en ;
.

###  was https://admin-shell.io/aas/3/DataSpecificationIec61360/shortName
aas-iec61360-3:shortName a owl:DatatypeProperty ;
    rdfs:label "has short name"@en ;
    rdfs:domain aas-3:DataSpecificationIec61360 ;
    rdfs:range rdf:langString ;
    rdfs:comment "Short name"@en ;
.

###  was https://admin-shell.io/aas/3/DataSpecificationIec61360/sourceOfDefinition
aas-iec61360-3:sourceOfDefinition a owl:DatatypeProperty ;
    rdfs:label "has source of definition"@en ;
    rdfs:domain aas-3:DataSpecificationIec61360 ;
    rdfs:range xsd:string ;
    rdfs:comment "Source of definition"@en ;
.

###  was https://admin-shell.io/aas/3/DataSpecificationIec61360/symbol
aas-iec61360-3:symbol a owl:DatatypeProperty ;
    rdfs:label "has symbol"@en ;
    rdfs:domain aas-3:DataSpecificationIec61360 ;
    rdfs:range xsd:string ;
    rdfs:comment "Symbol"@en ;
.

###  was https://admin-shell.io/aas/3/DataSpecificationIec61360/unit
aas-iec61360-3:unit a owl:DatatypeProperty ;
    rdfs:label "has unit"@en ;
    rdfs:domain aas-3:DataSpecificationIec61360 ;
    rdfs:range xsd:string ;
    rdfs:comment "Unit"@en ;
.

###  was https://admin-shell.io/aas/3/DataSpecificationIec61360/unitId
aas-iec61360-3:unitId a owl:ObjectProperty ;
    rdfs:label "has unit ID"@en ;
    rdfs:domain aas-3:DataSpecificationIec61360 ;
    rdfs:range aas-3:Reference ;
    rdfs:comment "Unique unit id"@en ;
.

###  was https://admin-shell.io/aas/3/DataSpecificationIec61360/value
# intentionally did not mix with aas-3:value
aas-iec61360-3:value a owl:DatatypeProperty ;
    rdfs:label "has value"@en ;
    rdfs:domain aas-3:DataSpecificationIec61360 ;
    rdfs:range xsd:string ;
    rdfs:comment "Value"@en ;
.

###  was https://admin-shell.io/aas/3/DataSpecificationIec61360/valueFormat
aas-iec61360-3:valueFormat a owl:DatatypeProperty ;
    rdfs:label "has value format"@en ;
    rdfs:domain aas-3:DataSpecificationIec61360 ;
    rdfs:range xsd:string ;
    rdfs:comment "Value Format"@en ;
.

###  was https://admin-shell.io/aas/3/DataSpecificationIec61360/valueList
aas-iec61360-3:valueList a owl:ObjectProperty ;
    rdfs:label "has value list"@en ;
    rdfs:domain aas-3:DataSpecificationIec61360 ;
    rdfs:range aas-iec61360-3:ValueList ;
    rdfs:comment "List of allowed values"@en ;
.

###  was https://admin-shell.io/aas/3/DataTypeDefXsd
###  was https://admin-shell.io/aas/3/DataTypeDefXsd/AnyUri
###  was https://admin-shell.io/aas/3/DataTypeDefXsd/Base64Binary
###  was https://admin-shell.io/aas/3/DataTypeDefXsd/Boolean
###  was https://admin-shell.io/aas/3/DataTypeDefXsd/Byte
###  was https://admin-shell.io/aas/3/DataTypeDefXsd/Date
###  was https://admin-shell.io/aas/3/DataTypeDefXsd/DateTime
###  was https://admin-shell.io/aas/3/DataTypeDefXsd/Decimal
###  was https://admin-shell.io/aas/3/DataTypeDefXsd/Double
###  was https://admin-shell.io/aas/3/DataTypeDefXsd/Duration
###  was https://admin-shell.io/aas/3/DataTypeDefXsd/Float
###  was https://admin-shell.io/aas/3/DataTypeDefXsd/GDay
###  was https://admin-shell.io/aas/3/DataTypeDefXsd/GMonth
###  was https://admin-shell.io/aas/3/DataTypeDefXsd/GMonthDay
###  was https://admin-shell.io/aas/3/DataTypeDefXsd/GYear
###  was https://admin-shell.io/aas/3/DataTypeDefXsd/GYearMonth
###  was https://admin-shell.io/aas/3/DataTypeDefXsd/HexBinary
###  was https://admin-shell.io/aas/3/DataTypeDefXsd/Int
###  was https://admin-shell.io/aas/3/DataTypeDefXsd/Integer
###  was https://admin-shell.io/aas/3/DataTypeDefXsd/Long
###  was https://admin-shell.io/aas/3/DataTypeDefXsd/NegativeInteger
###  was https://admin-shell.io/aas/3/DataTypeDefXsd/NonNegativeInteger
###  was https://admin-shell.io/aas/3/DataTypeDefXsd/NonPositiveInteger
###  was https://admin-shell.io/aas/3/DataTypeDefXsd/PositiveInteger
###  was https://admin-shell.io/aas/3/DataTypeDefXsd/Short
###  was https://admin-shell.io/aas/3/DataTypeDefXsd/String
###  was https://admin-shell.io/aas/3/DataTypeDefXsd/Time
###  was https://admin-shell.io/aas/3/DataTypeDefXsd/UnsignedByte
###  was https://admin-shell.io/aas/3/DataTypeDefXsd/UnsignedInt
###  was https://admin-shell.io/aas/3/DataTypeDefXsd/UnsignedLong
###  was https://admin-shell.io/aas/3/DataTypeDefXsd/UnsignedShort
# intentionally removed, as we will use xsd: datatypes instead of reintroduce new IRIs to denote the same concept

###  was https://admin-shell.io/aas/3/DataTypeIec61360
aas-iec61360-3:DataTypeIec61360 a owl:Class ;
    rdfs:label "Data Type IEC 61360"@en ;
    owl:oneOf (
        aas-iec61360-3:DataTypeIec61360_Blob
        aas-iec61360-3:DataTypeIec61360_Boolean
        aas-iec61360-3:DataTypeIec61360_Date
        aas-iec61360-3:DataTypeIec61360_File
        aas-iec61360-3:DataTypeIec61360_Html
        aas-iec61360-3:DataTypeIec61360_IntegerCount
        aas-iec61360-3:DataTypeIec61360_IntegerCurrency
        aas-iec61360-3:DataTypeIec61360_IntegerMeasure
        aas-iec61360-3:DataTypeIec61360_Irdi
        aas-iec61360-3:DataTypeIec61360_Iri
        aas-iec61360-3:DataTypeIec61360_Rational
        aas-iec61360-3:DataTypeIec61360_RationalMeasure
        aas-iec61360-3:DataTypeIec61360_RealCount
        aas-iec61360-3:DataTypeIec61360_RealCurrency
        aas-iec61360-3:DataTypeIec61360_RealMeasure
        aas-iec61360-3:DataTypeIec61360_String
        aas-iec61360-3:DataTypeIec61360_StringTranslatable
        aas-iec61360-3:DataTypeIec61360_Time
        aas-iec61360-3:DataTypeIec61360_Timestamp
    ) ;
.

###  was https://admin-shell.io/aas/3/DataTypeIec61360/Blob
aas-iec61360-3:DataTypeIec61360_Blob a aas-iec61360-3:DataTypeIec61360 ;
    rdfs:label "Blob"@en ;
    rdfs:comment "values containing the content of a file. Values may be binaries."@en ;
.

###  was https://admin-shell.io/aas/3/DataTypeIec61360/Boolean
aas-iec61360-3:DataTypeIec61360_Boolean a aas-iec61360-3:DataTypeIec61360  ;
    rdfs:label "Boolean"@en ;
    rdfs:comment "values representing truth of logic or Boolean algebra (TRUE, FALSE)"@en ;
.

###  was https://admin-shell.io/aas/3/DataTypeIec61360/Date
aas-iec61360-3:DataTypeIec61360_Date a aas-iec61360-3:DataTypeIec61360  ;
    rdfs:label "Date"@en ;
    rdfs:comment "values containing a calendar date, conformant to ISO 8601:2004 Format yyyy-mm-dd Example from IEC 61360-1:2017: \"1999-05-31\" is the [DATE] representation of: \"31 May 1999\"."@en ;
.

###  was https://admin-shell.io/aas/3/DataTypeIec61360/File
aas-iec61360-3:DataTypeIec61360_File a aas-iec61360-3:DataTypeIec61360  ;
    rdfs:label "File"@en ;
    rdfs:comment "values containing an address to a file. The values are of type URI and can represent an absolute or relative path."@en ;
.

###  was https://admin-shell.io/aas/3/DataTypeIec61360/Html
aas-iec61360-3:DataTypeIec61360_Html a aas-iec61360-3:DataTypeIec61360  ;
    rdfs:label "HTML"@en ;
    rdfs:comment "Values containing string with any sequence of characters, using the syntax of HTML5 (see W3C Recommendation 28:2014)"@en ;
.

###  was https://admin-shell.io/aas/3/DataTypeIec61360/IntegerCount
aas-iec61360-3:DataTypeIec61360_IntegerCount a aas-iec61360-3:DataTypeIec61360  ;
    rdfs:label "Integer Count"@en ;
    rdfs:comment "values containing values of type INTEGER but are no currencies or measures"@en ;
.

###  was https://admin-shell.io/aas/3/DataTypeIec61360/IntegerCurrency
aas-iec61360-3:DataTypeIec61360_IntegerCurrency a aas-iec61360-3:DataTypeIec61360  ;
    rdfs:label "Integer Currency"@en ;
    rdfs:comment "values containing values of type INTEGER that are currencies"@en ;
.

###  was https://admin-shell.io/aas/3/DataTypeIec61360/IntegerMeasure
aas-iec61360-3:DataTypeIec61360_IntegerMeasure a aas-iec61360-3:DataTypeIec61360  ;
    rdfs:label "Integer Measure"@en ;
    rdfs:comment "values containing values that are measure of type INTEGER. In addition such a value comes with a physical unit."@en ;
.

###  was https://admin-shell.io/aas/3/DataTypeIec61360/Irdi
aas-iec61360-3:DataTypeIec61360_Irdi a aas-iec61360-3:DataTypeIec61360  ;
    rdfs:label "IRDI"@en ;
    rdfs:comment "values conforming to ISO/IEC 11179 series global identifier sequences"@en ;
.

###  was https://admin-shell.io/aas/3/DataTypeIec61360/Iri
aas-iec61360-3:DataTypeIec61360_Iri a aas-iec61360-3:DataTypeIec61360  ;
    rdfs:label "IRI"@en ;
    rdfs:comment "values containing values of type STRING conformant to Rfc 3987"@en ;
.

###  was https://admin-shell.io/aas/3/DataTypeIec61360/Rational
aas-iec61360-3:DataTypeIec61360_Rational a aas-iec61360-3:DataTypeIec61360  ;
    rdfs:label "Rational"@en ;
    rdfs:comment "values containing values of type rational"@en ;
.

###  was https://admin-shell.io/aas/3/DataTypeIec61360/RationalMeasure
aas-iec61360-3:DataTypeIec61360_RationalMeasure a aas-iec61360-3:DataTypeIec61360  ;
    rdfs:label "Rational Measure"@en ;
    rdfs:comment "values containing values of type rational. In addition such a value comes with a physical unit."@en ;
.

###  was https://admin-shell.io/aas/3/DataTypeIec61360/RealCount
aas-iec61360-3:DataTypeIec61360_RealCount a aas-iec61360-3:DataTypeIec61360  ;
    rdfs:label "Real Count"@en ;
    rdfs:comment "values containing numbers that can be written as a terminating or non-terminating decimal; a rational or irrational number but are no currencies or measures"@en ;
.

###  was https://admin-shell.io/aas/3/DataTypeIec61360/RealCurrency
aas-iec61360-3:DataTypeIec61360_RealCurrency a aas-iec61360-3:DataTypeIec61360  ;
    rdfs:label "Real Currency"@en ;
    rdfs:comment "values containing values of type REAL that are currencies"@en ;
.

###  was https://admin-shell.io/aas/3/DataTypeIec61360/RealMeasure
aas-iec61360-3:DataTypeIec61360_RealMeasure a aas-iec61360-3:DataTypeIec61360  ;
    rdfs:label "Real Measure"@en ;
    rdfs:comment "values containing values that are measures of type REAL. In addition such a value comes with a physical unit."@en ;
.

###  was https://admin-shell.io/aas/3/DataTypeIec61360/String
aas-iec61360-3:DataTypeIec61360_String a aas-iec61360-3:DataTypeIec61360  ;
    rdfs:label "String"@en ;
    rdfs:comment "values consisting of sequence of characters but cannot be translated into other languages"@en ;
.

###  was https://admin-shell.io/aas/3/DataTypeIec61360/StringTranslatable
aas-iec61360-3:DataTypeIec61360_StringTranslatable a aas-iec61360-3:DataTypeIec61360  ;
    rdfs:label "String Translatable"@en ;
    rdfs:comment "values containing string but shall be represented as different string in different languages"@en ;
.

###  was https://admin-shell.io/aas/3/DataTypeIec61360/Time
aas-iec61360-3:DataTypeIec61360_Time a aas-iec61360-3:DataTypeIec61360  ;
    rdfs:label "Time"@en ;
    rdfs:comment "values containing a time, conformant to ISO 8601:2004 but restricted to what is allowed in the corresponding type in xml."@en ;
.

###  was https://admin-shell.io/aas/3/DataTypeIec61360/Timestamp
aas-iec61360-3:DataTypeIec61360_Timestamp a aas-iec61360-3:DataTypeIec61360  ;
    rdfs:label "Timestamp"@en ;
    rdfs:comment "values containing a time, conformant to ISO 8601:2004 but restricted to what is allowed in the corresponding type in xml."@en ;
.

###  was https://admin-shell.io/aas/3/Direction
aas-3:Direction a owl:Class ;
    rdfs:label "Direction"@en ;
    rdfs:comment "Direction"@en ;
    owl:oneOf (
        aas-3:Direction_Input
        aas-3:Direction_Output
    ) ;
.

###  was https://admin-shell.io/aas/3/Direction/Input
aas-3:Direction_Input a aas-3:Direction ;
    rdfs:label "Input"@en ;
    rdfs:comment "Input direction."@en ;
.

###  was https://admin-shell.io/aas/3/Direction/Output
aas-3:Direction_Output a aas-3:Direction ;
    rdfs:label "Output"@en ;
    rdfs:comment "Output direction"@en ;
.

###  was https://admin-shell.io/aas/3/EmbeddedDataSpecification
aas-3:EmbeddedDataSpecification a owl:Class ;
    rdfs:label "Embedded Data Specification"@en ;
    rdfs:comment "Embed the content of a data specification."@en ;
.

###  was https://admin-shell.io/aas/3/EmbeddedDataSpecification/dataSpecification
aas-3:dataSpecification a owl:ObjectProperty ;
    rdfs:label "has data specification"@en ;
    rdfs:domain aas-3:EmbeddedDataSpecification ;
    rdfs:range aas-3:Reference ;
    rdfs:comment "Reference to the data specification"@en ;
.

###  was https://admin-shell.io/aas/3/EmbeddedDataSpecification/dataSpecificationContent
aas-3:dataSpecificationContent a owl:ObjectProperty ;
    rdfs:label "has data specification content"@en ;
    rdfs:domain aas-3:EmbeddedDataSpecification ;
    rdfs:range aas-3:DataSpecificationContent ;
    rdfs:comment "Actual content of the data specification"@en ;
.

###  was https://admin-shell.io/aas/3/Entity
aas-3:Entity a owl:Class, owl:NamedIndividual ;
    rdfs:subClassOf aas-3:SubmodelElement ;
    rdfs:label "Entity"@en ;
    rdfs:comment "An entity is a submodel element that is used to model entities."@en ;
.

###  was https://admin-shell.io/aas/3/Entity/entityType
aas-3:entityType a owl:ObjectProperty ;
    rdfs:label "has entity type"@en ;
    rdfs:domain aas-3:Entity ;
    rdfs:range aas-3:EntityType ;
    rdfs:comment "Describes whether the entity is a co-managed entity or a self-managed entity."@en ;
.



###  was https://admin-shell.io/aas/3/Entity/statements
# to singular
aas-3:statement a owl:ObjectProperty ;
    rdfs:label "has statement"@en ;
    rdfs:domain aas-3:Entity ;
    rdfs:range aas-3:SubmodelElement ;
    rdfs:comment "Describes statements applicable to the entity by a set of submodel elements, typically with a qualified value."@en ;
.

###  was https://admin-shell.io/aas/3/EntityType
aas-3:EntityType a owl:Class ;
    rdfs:label "Entity Type"@en ;
    rdfs:comment "Enumeration for denoting whether an entity is a self-managed entity or a co-managed entity."@en ;
    owl:oneOf (
        aas-3:EntityType_CoManagedEntity
        aas-3:EntityType_SelfManagedEntity
    ) ;
.

###  was https://admin-shell.io/aas/3/EntityType/CoManagedEntity
aas-3:EntityType_CoManagedEntity a aas-3:EntityType ;
    rdfs:label "Co Managed Entity"@en ;
    rdfs:comment "For co-managed entities there is no separate AAS. Co-managed entities need to be part of a self-managed entity."@en ;
.

###  was https://admin-shell.io/aas/3/EntityType/SelfManagedEntity
aas-3:EntityType_SelfManagedEntity a aas-3:EntityType ;
    rdfs:label "Self Managed Entity"@en ;
    rdfs:comment "Self-Managed Entities have their own AAS but can be part of the bill of material of a composite self-managed entity."@en ;
.

###  was https://admin-shell.io/aas/3/Environment
aas-3:Environment a owl:Class ;
    rdfs:label "Environment"@en ;
    rdfs:comment "Container for the sets of different identifiables."@en ;
.

###  was https://admin-shell.io/aas/3/Environment/assetAdministrationShells
# to singular form
# also use this as a shortcut from Submodel and SubmodelElements to its AAS.
aas-3:assetAdministrationShell a owl:ObjectProperty ;
    rdfs:label "has asset administration shell"@en ;
    rdfs:range aas-3:AssetAdministrationShell ;
    rdfs:comment "Asset administration shell"@en ;
.

###  was https://admin-shell.io/aas/3/Environment/conceptDescriptions
# to singular form
aas-3:conceptDescription a owl:ObjectProperty ;
    rdfs:label "has concept description"@en ;
    rdfs:range aas-3:ConceptDescription ;
    rdfs:comment "Concept description"@en ;
.

###  was https://admin-shell.io/aas/3/Environment/submodels
# to singular form
# Also use this to point submodel element to its submodel that it is located in as a shortcut
aas-3:submodel a owl:ObjectProperty ;
    rdfs:label "has submodel"@en ;
    rdfs:range aas-3:Submodel ;
    rdfs:comment "Submodel"@en ;
.

###  was https://admin-shell.io/aas/3/EventElement
aas-3:EventElement a owl:Class, owl:NamedIndividual ;
    rdfs:subClassOf aas-3:SubmodelElement ;
    rdfs:label "Event Element"@en ;
    rdfs:comment "An event element."@en ;
.

###  was https://admin-shell.io/aas/3/EventPayload
aas-3:EventPayload a owl:Class ;
    rdfs:label "Event Payload"@en ;
    rdfs:comment "Defines the necessary information of an event instance sent out or received."@en ;
.

###  was https://admin-shell.io/aas/3/EventPayload/observableReference
aas-3:observableReference a owl:ObjectProperty ;
    rdfs:label "has observable reference"@en ;
    rdfs:domain aas-3:EventPayload ;
    rdfs:range aas-3:Reference ;
    rdfs:comment "Reference to the referable, which defines the scope of the event."@en ;
.

###  was https://admin-shell.io/aas/3/EventPayload/observableSemanticId
aas-3:observableSemanticId a owl:ObjectProperty ;
    rdfs:label "has observable semantic ID"@en ;
    rdfs:domain aas-3:EventPayload ;
    rdfs:range aas-3:Reference ;
    rdfs:comment "'semanticId' of the referable which defines the scope of the event, if available."@en ;
.

###  was https://admin-shell.io/aas/3/EventPayload/payload
aas-3:payload a owl:DatatypeProperty ;
    rdfs:label "has payload"@en ;
    rdfs:domain aas-3:EventPayload ;
    rdfs:range xsd:base64Binary ;
    rdfs:comment "Event specific payload."@en ;
.

###  was https://admin-shell.io/aas/3/EventPayload/source
aas-3:source a owl:ObjectProperty ;
    rdfs:label "has source"@en ;
    rdfs:domain aas-3:EventPayload ;
    rdfs:range aas-3:Reference ;
    rdfs:comment "Reference to the source event element, including identification of 'AssetAdministrationShell', 'Submodel', 'SubmodelElement''s."@en ;
.

###  was https://admin-shell.io/aas/3/EventPayload_sourceSemanticId
aas-3:sourceSemanticId a owl:ObjectProperty ;
    rdfs:label "has source semantic ID"@en ;
    rdfs:domain aas-3:EventPayload ;
    rdfs:range aas-3:Reference ;
    rdfs:comment "'semanticId' of the source event element, if available"@en ;
.

###  was https://admin-shell.io/aas/3/EventPayload_subjectId
aas-3:subjectId a owl:ObjectProperty ;
    rdfs:label "has subject ID"@en ;
    rdfs:domain aas-3:EventPayload ;
    rdfs:range aas-3:Reference ;
    rdfs:comment "Subject, who/which initiated the creation."@en ;
.

###  was https://admin-shell.io/aas/3/EventPayload_timeStamp
# UTC constraint should be in SHACL
aas-3:timeStamp a owl:DatatypeProperty ;
    rdfs:label "has time stamp"@en ;
    rdfs:domain aas-3:EventPayload ;
    rdfs:range xsd:dateTimeStamp ;
    rdfs:comment "Timestamp in UTC, when this event was triggered."@en ;
.

###  was https://admin-shell.io/aas/3/EventPayload_topic
aas-3:topic a owl:DatatypeProperty ;
    rdfs:label "has topic"@en ;
    rdfs:domain aas-3:EventPayload ;
    rdfs:range xsd:string ;
    rdfs:comment "Information for the outer message infrastructure for scheduling the event to the respective communication channel."@en ;
.

###  was https://admin-shell.io/aas/3/Extension
aas-3:Extension a owl:Class ;
    rdfs:subClassOf aas-3:HasSemantics ;
    rdfs:label "Extension"@en ;
    rdfs:comment "Single extension of an element."@en ;
.

###  was https://admin-shell.io/aas/3/Extension_name
# merged into one name property

###  was https://admin-shell.io/aas/3/Extension_refersTo
aas-3:refersTo a owl:ObjectProperty ;
    rdfs:label "has refers to"@en ;
    rdfs:domain aas-3:Extension ;
    rdfs:range aas-3:Reference ;
    rdfs:comment "Reference to an element the extension refers to."@en ;
.

###  was https://admin-shell.io/aas/3/Extension/value
# replaced with generic aas-3:value

###  was https://admin-shell.io/aas/3/Extension/valueType
aas-3:valueType a owl:ObjectProperty ;
    rdfs:label "has value type"@en ;
    rdfs:domain [ a owl:Class ;
                       owl:unionOf ( aas-3:Extension aas-3:Range aas-3:Qualifier aas-3:Property aas-3:SubmodelElementList  ) ] ;
    rdfs:range rdfs:Datatype ;
    rdfs:comment "Type of the value of the extension."@en ;
.

###  was https://admin-shell.io/aas/3/File
aas-3:File a owl:Class, owl:NamedIndividual ;
    rdfs:subClassOf aas-3:DataElement ;
    rdfs:label "File"@en ;
    rdfs:comment "A File is a data element that represents an address to a file (a locator)."@en ;
.


###  was https://admin-shell.io/aas/3/File/value
# replaced with generic aas-3:value

###  was https://admin-shell.io/aas/3/HasDataSpecification
aas-3:HasDataSpecification a owl:Class ;
    rdfs:label "Has Data Specification"@en ;
    rdfs:comment "Element that can be extended by using data specification templates."@en ;
.

###  was https://admin-shell.io/aas/3/HasDataSpecification/embeddedDataSpecifications
# to singular form
aas-3:embeddedDataSpecification a owl:ObjectProperty ;
    rdfs:label "has embedded data specification"@en ;
    rdfs:domain aas-3:HasDataSpecification ;
    rdfs:range aas-3:EmbeddedDataSpecification ;
    rdfs:comment "Embedded data specification."@en ;
.

###  was https://admin-shell.io/aas/3/HasExtensions
aas-3:HasExtensions a owl:Class ;
    rdfs:label "Has Extensions"@en ;
    rdfs:comment "Element that can be extended by proprietary extensions."@en ;
.

###  was https://admin-shell.io/aas/3/HasExtensions/extensions
# to singular form
aas-3:extension a owl:ObjectProperty ;
    rdfs:label "has extension"@en ;
    rdfs:domain aas-3:HasExtensions ;
    rdfs:range aas-3:Extension ;
    rdfs:comment "An extension of the element."@en ;
.

###  was https://admin-shell.io/aas/3/HasKind
aas-3:HasKind a owl:Class ;
    rdfs:label "Has Kind"@en ;
    rdfs:comment "An element with a kind is an element that can either represent a template or an instance."@en ;
.

###  was https://admin-shell.io/aas/3/HasKind/kind
# called modelingKind to not mix with assetKind
aas-3:modelingKind a owl:ObjectProperty ;
    rdfs:label "has modeling kind"@en ;
    rdfs:domain aas-3:HasKind ;
    rdfs:range aas-3:ModellingKind ;
    rdfs:comment "Kind of the element: either type or instance."@en ;
.

###  was https://admin-shell.io/aas/3/HasSemantics
aas-3:HasSemantics a owl:Class ;
    rdfs:label "Has Semantics"@en ;
    rdfs:comment "Element that can have a semantic definition plus some supplemental semantic definitions."@en ;
.

###  was https://admin-shell.io/aas/3/HasSemantics/semanticId
aas-3:semanticId a owl:ObjectProperty ;
    rdfs:label "has semantic ID"@en ;
    rdfs:domain aas-3:HasSemantics ;
    rdfs:range aas-3:Reference ;
    rdfs:comment "Identifier of the semantic definition of the element. It is called semantic ID of the element or also main semantic ID of the element."@en ;
.

###  was https://admin-shell.io/aas/3/HasSemantics/supplementalSemanticIds
# use singular form
aas-3:supplementalSemanticId a owl:ObjectProperty ;
    rdfs:label "has supplemental semantic ID"@en ;
    rdfs:domain aas-3:HasSemantics ;
    rdfs:range aas-3:Reference ;
    rdfs:comment "Identifier of a supplemental semantic definition of the element. It is called supplemental semantic ID of the element."@en ;
.

###  was https://admin-shell.io/aas/3/Identifiable
aas-3:Identifiable a owl:Class ;
    rdfs:subClassOf aas-3:Referable ;
    rdfs:label "Identifiable"@en ;
    rdfs:comment "An element that has a globally unique identifier."@en ;
.

###  was https://admin-shell.io/aas/3/Identifiable/administration
aas-3:administration a owl:ObjectProperty ;
    rdfs:label "has administration"@en ;
    rdfs:domain aas-3:Identifiable ;
    rdfs:range aas-3:AdministrativeInformation ;
    rdfs:comment "Administrative information of an identifiable element."@en ;
.

###  was https://admin-shell.io/aas/3/Identifiable/id
aas-3:id a owl:DatatypeProperty ;
    rdfs:label "has ID"@en ;
    rdfs:domain aas-3:Identifiable ;
    rdfs:range xsd:string ;
    rdfs:comment "The globally unique identification of the element."@en ;
.

###  was https://admin-shell.io/aas/3/Key
aas-3:Key a owl:Class ;
    rdfs:label "Key"@en ;
    rdfs:comment "A key is a reference to an element by its ID."@en ;
.

###  was https://admin-shell.io/aas/3/Key_type
# rename for better semantic
aas-3:keyType a owl:ObjectProperty ;
    rdfs:label "has key type"@en ;
    rdfs:domain aas-3:Key ;
    rdfs:range aas-3:KeyType ;
    rdfs:comment "Denotes which kind of entity is referenced."@en ;
.

###  was https://admin-shell.io/aas/3/Key_value
# replaced with generic aas-3:value

###  was https://admin-shell.io/aas/3/KeyTypes
# here we drop the s for consistency
# to singular form
aas-3:KeyType a owl:Class ;
    rdfs:label "Key Type"@en ;
    rdfs:comment "Enumeration of different key value types within a key."@en ;
    owl:oneOf (
        aas-3:KeyType_AnnotatedRelationshipElement
        aas-3:KeyType_AssetAdministrationShell
        aas-3:KeyType_BasicEventElement
        aas-3:KeyType_Blob
        aas-3:KeyType_Capability
        aas-3:KeyType_ConceptDescription
        aas-3:KeyType_DataElement
        aas-3:KeyType_Entity
        aas-3:KeyType_EventElement
        aas-3:KeyType_File
        aas-3:KeyType_FragmentReference
        aas-3:KeyType_GlobalReference
        aas-3:KeyType_Identifiable
        aas-3:KeyType_MultiLanguageProperty
        aas-3:KeyType_Operation
        aas-3:KeyType_Property
        aas-3:KeyType_Range
        aas-3:KeyType_Referable
        aas-3:KeyType_ReferenceElement
        aas-3:KeyType_RelationshipElement
        aas-3:KeyType_Submodel
        aas-3:KeyType_SubmodelElement
        aas-3:KeyType_SubmodelElementCollection
        aas-3:KeyType_SubmodelElementList
    ) ;
.

###  was https://admin-shell.io/aas/3/KeyTypes/AnnotatedRelationshipElement
aas-3:KeyType_AnnotatedRelationshipElement a aas-3:KeyType ;
    rdfs:label "Annotated Relationship Element"@en ;
.

###  was https://admin-shell.io/aas/3/KeyTypes/AssetAdministrationShell
aas-3:KeyType_AssetAdministrationShell a aas-3:KeyType ;
    rdfs:label "Asset Administration Shell"@en ;
.

###  was https://admin-shell.io/aas/3/KeyTypes/BasicEventElement
aas-3:KeyType_BasicEventElement a aas-3:KeyType ;
    rdfs:label "Basic Event Element"@en ;
.

###  was https://admin-shell.io/aas/3/KeyTypes/Blob
aas-3:KeyType_Blob a aas-3:KeyType ;
    rdfs:label "Blob"@en ;
.

###  was https://admin-shell.io/aas/3/KeyTypes/Capability
aas-3:KeyType_Capability a aas-3:KeyType ;
    rdfs:label "Capability"@en ;
.

###  was https://admin-shell.io/aas/3/KeyTypes/ConceptDescription
aas-3:KeyType_ConceptDescription a aas-3:KeyType ;
    rdfs:label "Concept Description"@en ;
.

###  was https://admin-shell.io/aas/3/KeyTypes/DataElement
aas-3:KeyType_DataElement a aas-3:KeyType ;
    rdfs:label "Data Element"@en ;
    rdfs:comment "Data element."@en ;
.

###  was https://admin-shell.io/aas/3/KeyTypes/Entity
aas-3:KeyType_Entity a aas-3:KeyType ;
    rdfs:label "Entity"@en ;
.

###  was https://admin-shell.io/aas/3/KeyTypes/EventElement
aas-3:KeyType_EventElement a aas-3:KeyType ;
    rdfs:label "Event Element"@en ;
    rdfs:comment "Event."@en ;
.

###  was https://admin-shell.io/aas/3/KeyTypes/File
aas-3:KeyType_File a aas-3:KeyType ;
    rdfs:label "File"@en ;
.

###  was https://admin-shell.io/aas/3/KeyTypes/FragmentReference
aas-3:KeyType_FragmentReference a aas-3:KeyType ;
    rdfs:label "Fragment Reference"@en ;
    rdfs:comment "Bookmark or a similar local identifier of a subordinate part of a primary resource"@en ;
.

###  was https://admin-shell.io/aas/3/KeyTypes/GlobalReference
aas-3:KeyType_GlobalReference a aas-3:KeyType ;
    rdfs:label "Global Reference"@en ;
.

###  was https://admin-shell.io/aas/3/KeyTypes/Identifiable
aas-3:KeyType_Identifiable a aas-3:KeyType ;
    rdfs:label "Identifiable"@en ;
    rdfs:comment "Identifiable."@en ;
.

###  was https://admin-shell.io/aas/3/KeyTypes/MultiLanguageProperty
aas-3:KeyType_MultiLanguageProperty a aas-3:KeyType ;
    rdfs:label "Multi Language Property"@en ;
    rdfs:comment "Property with a value that can be provided in multiple languages"@en ;
.

###  was https://admin-shell.io/aas/3/KeyTypes/Operation
aas-3:KeyType_Operation a aas-3:KeyType ;
    rdfs:label "Operation"@en ;
.

###  was https://admin-shell.io/aas/3/KeyTypes/Property
aas-3:KeyType_Property a aas-3:KeyType ;
    rdfs:label "Property"@en ;
.

###  was https://admin-shell.io/aas/3/KeyTypes/Range
aas-3:KeyType_Range a aas-3:KeyType ;
    rdfs:label "Range"@en ;
    rdfs:comment "Range with min and max"@en ;
.

###  was https://admin-shell.io/aas/3/KeyTypes/Referable
aas-3:KeyType_Referable a aas-3:KeyType ;
    rdfs:label "Referable"@en ;
.

###  was https://admin-shell.io/aas/3/KeyTypes/ReferenceElement
aas-3:KeyType_ReferenceElement a aas-3:KeyType ;
    rdfs:label "Reference Element"@en ;
    rdfs:comment "Reference"@en ;
.

###  was https://admin-shell.io/aas/3/KeyTypes/RelationshipElement
aas-3:KeyType_RelationshipElement a aas-3:KeyType ;
    rdfs:label "Relationship Element"@en ;
    rdfs:comment "Relationship"@en ;
.

###  was https://admin-shell.io/aas/3/KeyTypes/Submodel
aas-3:KeyType_Submodel a aas-3:KeyType ;
    rdfs:label "Submodel"@en ;
.

###  was https://admin-shell.io/aas/3/KeyTypes/SubmodelElement
aas-3:KeyType_SubmodelElement a aas-3:KeyType ;
    rdfs:label "Submodel Element"@en ;
    rdfs:comment "Submodel Element"@en ;
.

###  was https://admin-shell.io/aas/3/KeyTypes/SubmodelElementCollection
aas-3:KeyType_SubmodelElementCollection a aas-3:KeyType ;
    rdfs:label "Submodel Element Collection"@en ;
    rdfs:comment "Struct of Submodel Elements"@en ;
.

###  was https://admin-shell.io/aas/3/KeyTypes/SubmodelElementList
aas-3:KeyType_SubmodelElementList a aas-3:KeyType ;
    rdfs:label "Submodel Element List"@en ;
    rdfs:comment "List of Submodel Elements"@en ;
.

###  was https://admin-shell.io/aas/3/LangStringDefinitionTypeIec61360
# removed, used lang string and constraints checks should be in shacl


###  was https://admin-shell.io/aas/3/LangStringNameType
# removed, used lang string and constraints checks should be in shacl

###  was https://admin-shell.io/aas/3/LangStringPreferredNameTypeIec61360
# removed, used lang string and constraints checks should be in shacl


###  was https://admin-shell.io/aas/3/LangStringShortNameTypeIec61360
# removed, used lang string and constraints checks should be in shacl

###  was https://admin-shell.io/aas/3/LangStringTextType
# removed, used lang string and constraints checks should be in shacl


###  was https://admin-shell.io/aas/3/LevelType
### this is specific for iec61360
aas-iec61360-3:LevelType a owl:Class ;
    rdfs:label "Level Type"@en ;
    rdfs:comment "Value represented by up to four variants of a numeric value in a specific role: MIN, NOM, TYP and MAX. True means that the value is available, false means the value is not available."@en ;
.

###  was https://admin-shell.io/aas/3/LevelType/max
### this is specific for iec61360
aas-iec61360-3:max a owl:DatatypeProperty ;
    rdfs:label "has max"@en ;
    rdfs:domain aas-iec61360-3:LevelType ;
    rdfs:range xsd:boolean ;
    rdfs:comment "Maximum of the value"@en ;
.

###  was https://admin-shell.io/aas/3/LevelType/min
aas-iec61360-3:min a owl:DatatypeProperty ;
    rdfs:label "has min"@en ;
    rdfs:domain aas-iec61360-3:LevelType ;
    rdfs:range xsd:boolean ;
    rdfs:comment "Minimum of the value"@en ;
.

###  was https://admin-shell.io/aas/3/LevelType/nom
aas-iec61360-3:nom a owl:DatatypeProperty ;
    rdfs:label "has nom"@en ;
    rdfs:domain aas-iec61360-3:LevelType ;
    rdfs:range xsd:boolean ;
    rdfs:comment "Nominal value (value as designated)"@en ;
.

###  was https://admin-shell.io/aas/3/LevelType/typ
aas-iec61360-3:typ a owl:DatatypeProperty ;
    rdfs:label "has typ"@en ;
    rdfs:domain aas-iec61360-3:LevelType ;
    rdfs:range xsd:boolean ;
    rdfs:comment "Value as typically present"@en ;
.

###  was https://admin-shell.io/aas/3/ModellingKind
aas-3:ModellingKind a owl:Class ;
    rdfs:label "Modelling Kind"@en ;
    rdfs:comment "Enumeration for denoting whether an element is a template or an instance."@en ;
    owl:oneOf (
        aas-3:ModellingKind_Instance
        aas-3:ModellingKind_Template
    ) ;
.

###  was https://admin-shell.io/aas/3/ModellingKind/Instance
aas-3:ModellingKind_Instance a aas-3:ModellingKind ;
    rdfs:label "Instance"@en ;
    rdfs:comment "Concrete, clearly identifiable element instance. Its creation and validation may be guided by a corresponding element template."@en ;
.

###  was https://admin-shell.io/aas/3/ModellingKind/Template
aas-3:ModellingKind_Template a aas-3:ModellingKind ;
    rdfs:label "Template"@en ;
    rdfs:comment "Specification of the common features of a structured element in sufficient detail that such a instance can be instantiated using it"@en ;
.

###  was https://admin-shell.io/aas/3/MultiLanguageProperty
aas-3:MultiLanguageProperty a owl:Class, owl:NamedIndividual ;
    rdfs:subClassOf aas-3:DataElement ;
    rdfs:label "Multi Language Property"@en ;
    rdfs:comment "A property is a data element that has a multi-language value."@en ;
.

###  was https://admin-shell.io/aas/3/MultiLanguageProperty/value
# replaced with generic aas-3:value,
# range will be rdf:langString and will be checked with SHACL

###  was https://admin-shell.io/aas/3/MultiLanguageProperty/valueId
# replaced with generic aas-3:valueId

###  was https://admin-shell.io/aas/3/Operation
aas-3:Operation a owl:Class, owl:NamedIndividual ;
    rdfs:subClassOf aas-3:SubmodelElement ;
    rdfs:label "Operation"@en ;
    rdfs:comment "An operation is a submodel element with input and output variables."@en ;
.

###  was https://admin-shell.io/aas/3/Operation/inoutputVariables
# to singular form
aas-3:inoutputVariable a owl:ObjectProperty ;
    rdfs:label "has inoutput variable"@en ;
    rdfs:domain aas-3:Operation ;
    rdfs:range aas-3:OperationVariable ;
    rdfs:comment "Parameter that is input and output of the operation."@en ;
.

###  was https://admin-shell.io/aas/3/Operation/inputVariables
# to singular form
aas-3:inputVariable a owl:ObjectProperty ;
    rdfs:label "has input variable"@en ;
    rdfs:domain aas-3:Operation ;
    rdfs:range aas-3:OperationVariable ;
    rdfs:comment "Input parameter of the operation."@en ;
.

###  was https://admin-shell.io/aas/3/Operation/outputVariables
# to singular form
aas-3:outputVariable a owl:ObjectProperty ;
    rdfs:label "has output variable"@en ;
    rdfs:domain aas-3:Operation ;
    rdfs:range aas-3:OperationVariable ;
    rdfs:comment "Output parameter of the operation."@en ;
.

###  was https://admin-shell.io/aas/3/OperationVariable
aas-3:OperationVariable a owl:Class ;
    rdfs:label "Operation Variable"@en ;
    rdfs:comment "The value of an operation variable is a submodel element that is used as input and_or output variable of an operation."@en ;
.

###  was https://admin-shell.io/aas/3/OperationVariable/value
# replaced with generic aas-3:value

###  was https://admin-shell.io/aas/3/Property
aas-3:Property a owl:Class, owl:NamedIndividual ;
    rdfs:subClassOf aas-3:DataElement ;
    rdfs:label "Property"@en ;
    rdfs:comment "A property is a data element that has a single value."@en ;
.

###  was https://admin-shell.io/aas/3/Property/value
# replaced with generic aas-3:value

###  was https://admin-shell.io/aas/3/valueId
aas-3:valueId a owl:ObjectProperty ;
    rdfs:label "has value ID"@en ;
    rdfs:domain [ a owl:Class ;
                       owl:unionOf ( aas-3:Property aas-3:Qualifier aas-3:MultiLanguageProperty aas-iec61360-3:ValueReferencePair ) ] ;
    rdfs:range aas-3:Reference ;
    rdfs:comment "Reference to the global unique ID of a coded value."@en ;
.

###  was https://admin-shell.io/aas/3/Property_valueId
#replaced with generic valueId

###  was https://admin-shell.io/aas/3/Property/valueType
# reusing aas-3:valueType

###  was https://admin-shell.io/aas/3/Qualifiable
aas-3:Qualifiable a owl:Class ;
    rdfs:label "Qualifiable"@en ;
    rdfs:comment "The value of a qualifiable element may be further qualified by one or more qualifiers."@en ;
.

###  was https://admin-shell.io/aas/3/qualifiers
# to singular form
aas-3:qualifier a owl:ObjectProperty ;
    rdfs:label "has qualifier"@en ;
    rdfs:domain aas-3:Qualifiable ;
    rdfs:range aas-3:Qualifier ;
    rdfs:comment "Additional qualification of a qualifiable element."@en ;
.

###  was https://admin-shell.io/aas/3/Qualifier
aas-3:Qualifier a owl:Class ;
    rdfs:subClassOf aas-3:HasSemantics ;
    rdfs:label "Qualifier"@en ;
    rdfs:comment "A qualifier is a type-value-pair that makes additional statements w.r.t. the value of the element."@en ;
.

###  was https://admin-shell.io/aas/3/Qualifier_kind
# renamed to not mix with assetkind
aas-3:qualifierKind a owl:ObjectProperty ;
    rdfs:label "has qualifier kind"@en ;
    rdfs:domain aas-3:Qualifier ;
    rdfs:range aas-3:QualifierKind ;
    rdfs:comment "The qualifier kind describes the kind of the qualifier that is applied to the element."@en ;
.

###  was https://admin-shell.io/aas/3/Qualifier_type
# aas-3:type is too generic
aas-3:qualifierType a owl:DatatypeProperty ;
    rdfs:label "has qualifier type"@en ;
    rdfs:domain aas-3:Qualifier ;
    rdfs:range xsd:string ;
    rdfs:comment "The qualifier type describes the type of the qualifier that is applied to the element."@en ;
.

###  was https://admin-shell.io/aas/3/Qualifier_value
# replaced with generic aas-3:value

###  was https://admin-shell.io/aas/3/Qualifier/valueId
# replaced with generic valueId

###  was https://admin-shell.io/aas/3/Qualifier/valueType
# using aas-3:valueType

###  was https://admin-shell.io/aas/3/QualifierKind
aas-3:QualifierKind a owl:Class ;
    rdfs:label "Qualifier Kind"@en ;
    rdfs:comment "Enumeration for kinds of qualifiers."@en ;
    owl:oneOf (
        aas-3:QualifierKind_ConceptQualifier
        aas-3:QualifierKind_TemplateQualifier
        aas-3:QualifierKind_ValueQualifier
    ) ;
.

###  was https://admin-shell.io/aas/3/QualifierKind/ConceptQualifier
aas-3:QualifierKind_ConceptQualifier a aas-3:QualifierKind ;
    rdfs:label "Concept Qualifier"@en ;
    rdfs:comment "qualifies the semantic definition the element is referring to ('semanticId')"@en ;
.

###  was https://admin-shell.io/aas/3/QualifierKind/TemplateQualifier
aas-3:QualifierKind_TemplateQualifier a aas-3:QualifierKind ;
    rdfs:label "Template Qualifier"@en ;
    rdfs:comment "qualifies the elements within a specific submodel on concept level."@en ;
.

###  was https://admin-shell.io/aas/3/QualifierKind/ValueQualifier
aas-3:QualifierKind_ValueQualifier a aas-3:QualifierKind ;
    rdfs:label "Value Qualifier"@en ;
    rdfs:comment "qualifies the value of the element and can change during run-time."@en ;
.

###  was https://admin-shell.io/aas/3/Range
aas-3:Range a owl:Class, owl:NamedIndividual ;
    rdfs:subClassOf aas-3:DataElement ;
    rdfs:label "Range"@en ;
    rdfs:comment "A range data element is a data element that defines a range with min and max."@en ;
.

###  was https://admin-shell.io/aas/3/Range/max
# range is determined by valueType
aas-3:max a owl:DatatypeProperty ;
    rdfs:label "has max"@en ;
    rdfs:domain aas-3:Range ;
    rdfs:comment "The maximum value of the range."@en ;
.

###  was https://admin-shell.io/aas/3/Range/min
# range is determined by valueType
aas-3:min a owl:DatatypeProperty ;
    rdfs:label "has min"@en ;
    rdfs:domain aas-3:Range ;
    rdfs:comment "The minimum value of the range."@en ;
.

###  was https://admin-shell.io/aas/3/Range/valueType
# reusing aas-3:valueType

###  was https://admin-shell.io/aas/3/Referable
aas-3:Referable a owl:Class ;
    rdfs:subClassOf aas-3:HasExtensions ;
    rdfs:label "Referable"@en ;
    rdfs:comment "An element that is referable by its 'idShort'."@en ;
.

###  was https://admin-shell.io/aas/3/Referable/category
aas-3:category a owl:DatatypeProperty ;
    rdfs:label "has category"@en ;
    rdfs:domain aas-3:Referable ;
    rdfs:range xsd:string ;
    rdfs:comment "The category is a value that gives further meta information w.r.t. to the class of the element. It affects the expected existence of attributes and the applicability of constraints."@en ;
.

###  was https://admin-shell.io/aas/3/Referable/description
aas-3:description a owl:DatatypeProperty ;
    rdfs:label "has description"@en ;
    rdfs:domain aas-3:Referable ;
    rdfs:range rdf:langString ;
    rdfs:comment "Description or comments on the element."@en ;
.

###  was https://admin-shell.io/aas/3/Referable/displayName
aas-3:displayName a owl:DatatypeProperty ;
    rdfs:label "has display name"@en ;
    rdfs:domain aas-3:Referable ;
    rdfs:range rdf:langString ;
    rdfs:comment "Display name. Can be provided in several languages."@en ;
.

###  was https://admin-shell.io/aas/3/Referable/idShort
aas-3:idShort a owl:DatatypeProperty ;
    rdfs:label "has ID short"@en ;
    rdfs:domain aas-3:Referable ;
    rdfs:range xsd:string ;
    rdfs:comment "In case of identifiables this attribute is a short name of the element. In case of referable this ID is an identifying string of the element within its name space."@en ;
.

###  was https://admin-shell.io/aas/3/Reference
aas-3:Reference a owl:Class ;
    rdfs:label "Reference"@en ;
    rdfs:comment "Reference to either a model element of the same or another AAS or to an external entity."@en ;
.

###  was https://admin-shell.io/aas/3/Reference/keys
# use singular form and range is a list. SHACL check required to check all elements of the list
aas-3:key a owl:ObjectProperty ;
    rdfs:label "has key"@en ;
    rdfs:domain aas-3:Reference ;
    rdfs:range rdf:List ;
    rdfs:comment "Unique references in their name space."@en ;
.

###  was https://admin-shell.io/aas/3/Reference/referredSemanticId
aas-3:referredSemanticId a owl:ObjectProperty ;
    rdfs:label "has referred semantic ID"@en ;
    rdfs:domain aas-3:Reference ;
    rdfs:range aas-3:Reference ;
    rdfs:comment "'semanticId' of the referenced model element ('type' = 'ModelReference')."@en ;
.

###  was https://admin-shell.io/aas/3/Reference/type
# type is too generic
aas-3:referenceType a owl:ObjectProperty ;
    rdfs:label "has reference type"@en ;
    rdfs:domain aas-3:Reference ;
    rdfs:range aas-3:ReferenceType ;
    rdfs:comment "Type of the reference."@en ;
.

###  was https://admin-shell.io/aas/3/ReferenceElement
aas-3:ReferenceElement a owl:Class, owl:NamedIndividual ;
    rdfs:subClassOf aas-3:DataElement ;
    rdfs:label "Reference Element"@en ;
    rdfs:comment "A reference element is a data element that defines a logical reference to another element within the same or another AAS or a reference to an external object or entity."@en ;
.

###  was https://admin-shell.io/aas/3/ReferenceElement_value
# replaced with generic aas-3:value

###  was https://admin-shell.io/aas/3/ReferenceType
# singular form
aas-3:ReferenceType a owl:Class ;
    rdfs:label "Reference Type"@en ;
    rdfs:comment "Reference type"@en ;
    owl:oneOf (
        aas-3:ReferenceType_ExternalReference
        aas-3:ReferenceType_ModelReference
    ) ;
.

###  was https://admin-shell.io/aas/3/ReferenceTypes/ExternalReference
aas-3:ReferenceType_ExternalReference a aas-3:ReferenceType ;
    rdfs:label "External Reference"@en ;
    rdfs:comment "External reference."@en ;
.

###  was https://admin-shell.io/aas/3/ReferenceTypes/ModelReference
aas-3:ReferenceType_ModelReference a aas-3:ReferenceType ;
    rdfs:label "Model Reference"@en ;
    rdfs:comment "Model reference."@en ;
.

###  was https://admin-shell.io/aas/3/RelationshipElement
aas-3:RelationshipElement a owl:Class, owl:NamedIndividual;
    rdfs:subClassOf aas-3:SubmodelElement ;
    rdfs:label "Relationship Element"@en ;
    rdfs:comment "A relationship element is used to define a relationship between two elements being either referable (model reference) or external (global reference)."@en ;
.

###  was https://admin-shell.io/aas/3/RelationshipElement/first
aas-3:first a owl:ObjectProperty ;
    rdfs:label "has first"@en ;
    rdfs:domain aas-3:RelationshipElement ;
    rdfs:range aas-3:Reference ;
    rdfs:comment "Reference to the first element in the relationship taking the role of the subject."@en ;
.

###  was https://admin-shell.io/aas/3/RelationshipElement/second
aas-3:second a owl:ObjectProperty ;
    rdfs:label "has second"@en ;
    rdfs:domain aas-3:RelationshipElement ;
    rdfs:range aas-3:Reference ;
    rdfs:comment "Reference to the second element in the relationship taking the role of the object."@en ;
.

###  was https://admin-shell.io/aas/3/Resource
aas-3:Resource a owl:Class ;
    rdfs:label "Resource"@en ;
    rdfs:comment "Resource represents an address to a file (a locator). The value is an URI that can represent an absolute or relative path"@en ;
.


###  was https://admin-shell.io/aas/3/Resource/path
aas-3:path a owl:DatatypeProperty ;
    rdfs:label "has path"@en ;
    rdfs:domain aas-3:Resource ;
    rdfs:range xsd:string ;
    rdfs:comment "Path and name of the resource (with file extension)."@en ;
.

###  was https://admin-shell.io/aas/3/SpecificAssetId
aas-3:SpecificAssetId a owl:Class ;
    rdfs:subClassOf aas-3:HasSemantics ;
    rdfs:label "Specific Asset ID"@en ;
    rdfs:comment "A specific asset ID describes a generic supplementary identifying attribute of the asset."@en ;
.

###  was https://admin-shell.io/aas/3/SpecificAssetId/externalSubjectId
aas-3:externalSubjectId a owl:ObjectProperty ;
    rdfs:label "has external subject ID"@en ;
    rdfs:domain aas-3:SpecificAssetId ;
    rdfs:range aas-3:Reference ;
    rdfs:comment "The (external) subject the key belongs to or has meaning to."@en ;
.

###  was https://admin-shell.io/aas/3/SpecificAssetId/name
aas-3:name a owl:DatatypeProperty ;
    rdfs:label "has name"@en ;
    rdfs:domain [ a owl:Class ;
                  owl:unionOf ( aas-3:SpecificAssetId aas-3:Extension ) ] ;
    rdfs:range xsd:string ;
    rdfs:comment "Name of the identifier or extension"@en ;
.

###  was https://admin-shell.io/aas/3/SpecificAssetId/value
# replaced with generic aas-3:value

###  was https://admin-shell.io/aas/3/StateOfEvent
aas-3:StateOfEvent a owl:Class ;
    rdfs:label "State Of Event"@en ;
    rdfs:comment "State of an event"@en ;
    owl:oneOf (
        aas-3:StateOfEvent_Off
        aas-3:StateOfEvent_On
    ) ;
.

###  was https://admin-shell.io/aas/3/StateOfEvent_Off
aas-3:StateOfEvent_Off a aas-3:StateOfEvent ;
    rdfs:label "Off"@en ;
    rdfs:comment "Event is off."@en ;
.

###  was https://admin-shell.io/aas/3/StateOfEvent_On
aas-3:StateOfEvent_On a aas-3:StateOfEvent ;
    rdfs:label "On"@en ;
    rdfs:comment "Event is on"@en ;
.

###  was https://admin-shell.io/aas/3/Submodel
aas-3:Submodel a owl:Class  ;
    rdfs:subClassOf aas-3:Identifiable ;
    rdfs:subClassOf aas-3:HasKind ;
    rdfs:subClassOf aas-3:HasSemantics ;
    rdfs:subClassOf aas-3:Qualifiable ;
    rdfs:subClassOf aas-3:HasDataSpecification ;
    rdfs:label "Submodel"@en ;
    rdfs:comment "A submodel defines a specific aspect of the asset represented by the AAS."@en ;
.

###  was https://admin-shell.io/aas/3/Submodel/submodelElements
# renamed to submodelElement
aas-3:submodelElement a owl:ObjectProperty ;
    rdfs:label "has submodel element"@en ;
    rdfs:domain aas-3:Submodel ;
    rdfs:range aas-3:SubmodelElement ;
    rdfs:comment "A submodel consists of zero or more submodel elements."@en ;
.

###  was https://admin-shell.io/aas/3/SubmodelElement
aas-3:SubmodelElement a owl:Class, owl:NamedIndividual ;
    rdfs:subClassOf aas-3:Referable ;
    rdfs:subClassOf aas-3:HasSemantics ;
    rdfs:subClassOf aas-3:Qualifiable ;
    rdfs:subClassOf aas-3:HasDataSpecification ;
    rdfs:label "Submodel Element"@en ;
    rdfs:comment "A submodel element is an element suitable for the description and differentiation of assets."@en ;
.

###  was https://admin-shell.io/aas/3/SubmodelElementCollection
aas-3:SubmodelElementCollection a owl:Class, owl:NamedIndividual ;
    rdfs:subClassOf aas-3:SubmodelElement ;
    rdfs:label "Submodel Element Collection"@en ;
    rdfs:comment "A submodel element collection is a kind of struct, i.e. a a logical encapsulation of multiple named values. It has a fixed number of submodel elements."@en ;
.

###  was https://admin-shell.io/aas/3/SubmodelElementCollection/value
# replaced with generic aas-3:value

###  was https://admin-shell.io/aas/3/SubmodelElementList
aas-3:SubmodelElementList a owl:Class, owl:NamedIndividual ;
    rdfs:subClassOf aas-3:SubmodelElement ;
	rdfs:subClassOf [
        a owl:Restriction ;
        owl:onProperty aas-3:typeValueListElement ;
        owl:allValuesFrom [
            a owl:Class ;
            owl:oneOf (
                aas-3:AnnotatedRelationshipElement
                aas-3:BasicEventElement
                aas-3:Blob
                aas-3:Capability
                aas-3:DataElement
                aas-3:Entity
                aas-3:EventElement
                aas-3:File
                aas-3:MultiLanguageProperty
                aas-3:Operation
                aas-3:Property
                aas-3:Range
                aas-3:ReferenceElement
                aas-3:RelationshipElement
                aas-3:SubmodelElement
                aas-3:SubmodelElementCollection
                aas-3:SubmodelElementList
            )
        ]
    ] ;
    rdfs:label "Submodel Element List"@en ;
    rdfs:comment "A submodel element list is an ordered list of submodel elements."@en ;
.

###  was https://admin-shell.io/aas/3/SubmodelElementList/orderRelevant
aas-3:orderRelevant a owl:DatatypeProperty ;
    rdfs:label "has order relevant"@en ;
    rdfs:domain aas-3:SubmodelElementList ;
    rdfs:range xsd:boolean ;
    rdfs:comment "Defines whether order in list is relevant. If 'orderRelevant' = False then the list is representing a set or a bag."@en ;
.

###  was https://admin-shell.io/aas/3/SubmodelElementList/semanticIdListElement

aas-3:semanticIdListElement a owl:ObjectProperty ;
    rdfs:label "has semantic ID list element"@en ;
    rdfs:domain aas-3:SubmodelElementList ;
    rdfs:range aas-3:Reference ;
    rdfs:comment "Semantic ID the submodel elements contained in the list match to."@en ;
.

###  was https://admin-shell.io/aas/3/SubmodelElementList/typeValueListElement
# drop ListElement from the name. It should be one of AAS:SubmodelElement items
aas-3:typeValueListElement a owl:ObjectProperty ;
    rdfs:label "has type value list element"@en ;
    rdfs:domain aas-3:SubmodelElementList ;
    rdfs:range owl:Class ;
    rdfs:comment "The submodel element type of the submodel elements contained in the list."@en ;
.

###  was https://admin-shell.io/aas/3/SubmodelElementList/value
# replaced with generic aas-3:value

###  was https://admin-shell.io/aas/3/valueTypeListElement
# drop ListElement from the name, merge with aas-3:valueType


###  was https://admin-shell.io/aas/3/ValueList
aas-iec61360-3:ValueList a owl:Class ;
    rdfs:label "Value List"@en ;
    rdfs:comment "A set of value reference pairs."@en ;
.

###  was https://admin-shell.io/aas/3/ValueList/valueReferencePairs
# to singular form
# note that we have a tight namespace couple between aas and iec61360. this is also one reason that they
# are not separate ontology but separate namespace, as that would end up having a circular dependency
aas-iec61360-3:valueReferencePair a owl:ObjectProperty ;
    rdfs:label "has value reference pair"@en ;
    rdfs:domain aas-iec61360-3:ValueList ;
    rdfs:range aas-iec61360-3:ValueReferencePair ;
    rdfs:comment "A pair of a value together with its global unique id."@en ;
.

###  was https://admin-shell.io/aas/3/ValueReferencePair
aas-iec61360-3:ValueReferencePair a owl:Class ;
    rdfs:label "Value Reference Pair"@en ;
    rdfs:comment "A value reference pair within a value list. Each value has a global unique id defining its semantic."@en ;
.

###  was https://admin-shell.io/aas/3/ValueReferencePair_value
# replaced with generic aas-3:value

###  was https://admin-shell.io/aas/3/ValueReferencePair_valueId
# replaced with generic valueId

################################ Extra additions
aas-3:modelVersion a owl:DatatypeProperty ;
    rdfs:label "has model version"@en ;
    rdfs:domain [ a owl:Class ;
                  owl:unionOf ( aas-3:Submodel aas-3:ConceptDescription aas-3:AssetAdministrationShell ) ] ;
    rdfs:range xsd:string ;
    rdfs:comment "storing exact model version helps validators and other components to correctly work https://github.com/admin-shell-io/aas-specs-metamodel/issues/615"@en ;
.
###AAS_3_EXTENDED
aas-3-ex:eclass a owl:ObjectProperty ;
    rdfs:label "has ECLASS"@en ;
    rdfs:domain [ a owl:Class ;
                  owl:unionOf ( aas-3:Submodel aas-3:ConceptDescription aas-3:AssetAdministrationShell ) ] ;
    rdfs:range rdfs:Resource ;
    rdfs:comment "connects a concept description to ECLASS (can be ECLASS RDF)"@en ;
.
aas-3-ex:iec_cdd a owl:ObjectProperty ;
    rdfs:label "has IEC CDD"@en ;
    rdfs:domain aas-3:ConceptDescription;
    rdfs:range rdfs:Resource ;
    rdfs:comment "connects a concept description to IEC CDD resource"@en ;
.

aas-3-ex:resolvesTo a owl:ObjectProperty ;
    rdfs:label "resolves to"@en ;
    rdfs:domain aas-3:Reference;
    rdfs:range rdfs:Resource ;
    rdfs:comment "after resolving the keys path, here we store resolves to shortcut. Typically applicable to ModelReference"@en ;
.

aas-3-ex:resource a owl:ObjectProperty ;
    rdfs:label "resource"@en ;
    rdfs:range rdfs:Resource ;
    rdfs:comment "Certain element in AAS refer to other resources, here we store resolves to shortcut. Typically applicable to ModelReference"@en ;
.


    """
    AAS_ONTOLOGY_3 = AAS_ONTOLOGY_3_1

    AAS_SHACL_3_1 = r'''
    # SHACL Shapes for Asset Administration Shell V3.1
    # Aligned with ontology namespace conventions (aas-3: prefix)
    @prefix aas-3: <https://admin-shell.io/aas/3/> .
    @prefix aas-iec61360-3: <https://admin-shell.io/DataSpecificationTemplates/DataSpecificationIec61360/3/> .
    @prefix aas-3-ex: <https://admin-shell.io/aas/3/extended/> .
    @prefix owl: <http://www.w3.org/2002/07/owl#> .
    @prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
    @prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
    @prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
    @prefix dct: <http://purl.org/dc/terms/> .
    @prefix sh: <http://www.w3.org/ns/shacl#> .

    aas-3:AdministrativeInformationShape a sh:NodeShape ;
        sh:description "AASd-005: If AdministrativeInformation/version is empty, AdministrativeInformation/revision shall also be empty." ;
        sh:targetClass aas-3:AdministrativeInformation ;
        sh:sparql [
            a sh:SPARQLConstraint ;
            sh:message "AASd-005: If AdministrativeInformation/version is empty, AdministrativeInformation/revision shall also be empty."@en ;
            sh:select """
                SELECT ?this ?revision
                WHERE {
                    ?this <https://admin-shell.io/aas/3/revision> ?revision .
                    FILTER NOT EXISTS { ?this <https://admin-shell.io/aas/3/version> ?version }
                }
            """ ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:version ;
            sh:message "version: must be of datatype string; at most one value allowed; length must be between 1 and 4; must match the required pattern."@en ;
            sh:datatype xsd:string ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
            sh:minLength 1 ;
            sh:maxLength 4 ;
            sh:pattern "^(0|[1-9][0-9]*)$" ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:revision ;
            sh:message "revision: must be of datatype string; at most one value allowed; length must be between 1 and 4; must match the required pattern."@en ;
            sh:datatype xsd:string ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
            sh:minLength 1 ;
            sh:maxLength 4 ;
            sh:pattern "^(0|[1-9][0-9]*)$" ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:creator ;
            sh:message "creator: must be of type Reference; at most one value allowed."@en ;
            sh:class aas-3:Reference ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:templateId ;
            sh:message "templateId: must be of datatype string; at most one value allowed; length must be between 1 and 2048; must match the required pattern."@en ;
            sh:datatype xsd:string ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
            sh:minLength 1 ;
            sh:maxLength 2048 ;
            sh:pattern "^([\\u0009\\u000a\\u000d\\u0020-\\ud7ff\\ue000-\\ufffd]|\\ud800[\\udc00-\\udfff]|[\\ud801-\\udbfe][\\udc00-\\udfff]|\\udbff[\\udc00-\\udfff])*$" ;
        ] ;
    .

    aas-3:AnnotatedRelationshipElementShape a sh:NodeShape ;
        sh:targetClass aas-3:AnnotatedRelationshipElement ;
        sh:node aas-3:RelationshipElementShape ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:annotation ;
            sh:message "annotation: must be of type DataElement."@en ;
            sh:or (
                [ sh:class aas-3:DataElement ]
                [ sh:class aas-3:Blob ]
                [ sh:class aas-3:File ]
                [ sh:class aas-3:MultiLanguageProperty ]
                [ sh:class aas-3:Property ]
                [ sh:class aas-3:Range ]
                [ sh:class aas-3:ReferenceElement ]
            ) ;
            sh:minCount 0 ;
        ] ;
    .

    aas-3:AssetAdministrationShellShape a sh:NodeShape ;
        sh:targetClass aas-3:AssetAdministrationShell ;
        sh:node aas-3:IdentifiableShape ;
        sh:node aas-3:HasDataSpecificationShape ;
        sh:sparql [
            a sh:SPARQLConstraint ;
            sh:message "Each submodelReference of an AssetAdministrationShell must be a ModelReference with at least one Key whose keyType is Submodel."@en ;
            sh:select """
                SELECT ?this ?ref
                WHERE {
                    ?this <https://admin-shell.io/aas/3/submodelReference> ?ref .
                    {
                        ?ref <https://admin-shell.io/aas/3/referenceType> ?refType .
                        FILTER (?refType != <https://admin-shell.io/aas/3/ModelReference>)
                    }
                    UNION
                    {
                        FILTER NOT EXISTS {
                            ?ref <https://admin-shell.io/aas/3/key> ?key .
                            ?key <https://admin-shell.io/aas/3/keyType> <https://admin-shell.io/aas/3/Submodel> .
                        }
                    }
                }
            """ ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:derivedFrom ;
            sh:message "derivedFrom: must be of type Reference; at most one value allowed."@en ;
            sh:class aas-3:Reference ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:assetInformation ;
            sh:message "assetInformation: must be of type AssetInformation; exactly one value required."@en ;
            sh:class aas-3:AssetInformation ;
            sh:minCount 1 ;
            sh:maxCount 1 ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:submodelReference ;
            sh:message "submodelReference: must be of type Reference."@en ;
            sh:class aas-3:Reference ;
            sh:minCount 0 ;
        ] ;
    .

    aas-3:AssetInformationShape a sh:NodeShape ;
        sh:targetClass aas-3:AssetInformation ;
        sh:sparql [
            a sh:SPARQLConstraint ;
            sh:message "AASd-131: The globalAssetId or at least one specificAssetId shall be defined for AssetInformation."@en ;
            sh:select """
                SELECT ?this
                WHERE {
                    ?this <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> <https://admin-shell.io/aas/3/AssetInformation> .
                    FILTER NOT EXISTS { ?this <https://admin-shell.io/aas/3/globalAssetId> ?gaid }
                    FILTER NOT EXISTS { ?this <https://admin-shell.io/aas/3/specificAssetId> ?said }
                }
            """ ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:assetKind ;
            sh:message "assetKind: must be of type AssetKind; exactly one value required."@en ;
            sh:or (
                [ sh:class aas-3:AssetKind ]
                [ sh:in ( aas-3:AssetKind_Type aas-3:AssetKind_Instance aas-3:AssetKind_NotApplicable aas-3:AssetKind_Role ) ]
            ) ;
            sh:minCount 1 ;
            sh:maxCount 1 ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:globalAssetId ;
            sh:message "globalAssetId: must be of datatype string; at most one value allowed; length must be between 1 and 2048; must match the required pattern."@en ;
            sh:datatype xsd:string ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
            sh:minLength 1 ;
            sh:maxLength 2048 ;
            sh:pattern "^([\\u0009\\u000a\\u000d\\u0020-\\ud7ff\\ue000-\\ufffd]|\\ud800[\\udc00-\\udfff]|[\\ud801-\\udbfe][\\udc00-\\udfff]|\\udbff[\\udc00-\\udfff])*$" ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:specificAssetId ;
            sh:message "specificAssetId: must be of type SpecificAssetId."@en ;
            sh:class aas-3:SpecificAssetId ;
            sh:minCount 0 ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:assetType ;
            sh:message "assetType: must be of datatype string; at most one value allowed; length must be between 1 and 2048; must match the required pattern."@en ;
            sh:datatype xsd:string ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
            sh:minLength 1 ;
            sh:maxLength 2048 ;
            sh:pattern "^([\\u0009\\u000a\\u000d\\u0020-\\ud7ff\\ue000-\\ufffd]|\\ud800[\\udc00-\\udfff]|[\\ud801-\\udbfe][\\udc00-\\udfff]|\\udbff[\\udc00-\\udfff])*$" ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:defaultThumbnail ;
            sh:message "defaultThumbnail: must be of type Resource; at most one value allowed."@en ;
            sh:class aas-3:Resource ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
        ] ;
    .

    aas-3:BasicEventElementShape a sh:NodeShape ;
        sh:targetClass aas-3:BasicEventElement ;
        sh:node aas-3:EventElementShape ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:observed ;
            sh:message "observed: must be of type Reference; exactly one value required."@en ;
            sh:class aas-3:Reference ;
            sh:minCount 1 ;
            sh:maxCount 1 ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:direction ;
            sh:message "direction: must be of type Direction; exactly one value required."@en ;
            sh:or (
                [ sh:class aas-3:Direction ]
                [ sh:in ( aas-3:Direction_Input aas-3:Direction_Output ) ]
            ) ;
            sh:minCount 1 ;
            sh:maxCount 1 ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:state ;
            sh:message "state: must be of type StateOfEvent; exactly one value required."@en ;
            sh:or (
                [ sh:class aas-3:StateOfEvent ]
                [ sh:in ( aas-3:StateOfEvent_Off aas-3:StateOfEvent_On ) ]
            ) ;
            sh:minCount 1 ;
            sh:maxCount 1 ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:messageTopic ;
            sh:message "messageTopic: must be of datatype string; at most one value allowed; length must be between 1 and 255; must match the required pattern."@en ;
            sh:datatype xsd:string ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
            sh:minLength 1 ;
            sh:maxLength 255 ;
            sh:pattern "^([\\u0009\\u000a\\u000d\\u0020-\\ud7ff\\ue000-\\ufffd]|\\ud800[\\udc00-\\udfff]|[\\ud801-\\udbfe][\\udc00-\\udfff]|\\udbff[\\udc00-\\udfff])*$" ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:messageBroker ;
            sh:message "messageBroker: must be of type Reference; at most one value allowed."@en ;
            sh:class aas-3:Reference ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:lastUpdate ;
            sh:message "lastUpdate: must be of datatype dateTimeStamp in UTC; at most one value allowed."@en ;
            sh:datatype xsd:dateTimeStamp ;
            # be careful with negative values as rdflib shacl validator will complain against negative values
            sh:minCount 0 ;
            sh:maxCount 1 ;
        ] ;
        sh:sparql [
            a sh:SPARQLConstraint ;
            sh:message "lastUpdate: timestamp must be in UTC (ending with Z, +00:00, or -00:00)."@en ;
            sh:select """
                SELECT ?this ?lastUpdate
                WHERE {
                    ?this <https://admin-shell.io/aas/3/lastUpdate> ?lastUpdate .
                    FILTER (!REGEX(STR(?lastUpdate), "(Z|\\\\+00:00|-00:00)$"))
                }
            """ ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:minInterval ;
            sh:message "minInterval: must be of datatype duration; at most one value allowed; must match the required pattern."@en ;
            sh:datatype xsd:duration ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:maxInterval ;
            sh:message "maxInterval: must be of datatype duration; at most one value allowed; must match the required pattern."@en ;
            sh:datatype xsd:duration ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
        ] ;
    .

    aas-3:BlobShape a sh:NodeShape ;
        sh:targetClass aas-3:Blob ;
        sh:node aas-3:DataElementShape ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:value ;
            sh:message "value: must be of datatype base64Binary; at most one value allowed."@en ;
            sh:datatype xsd:base64Binary ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:contentType ;
            sh:message "contentType: must be of datatype string; at most one value allowed; length must be between 1 and 128; must match the required pattern."@en ;
            sh:datatype xsd:string ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
            sh:minLength 1 ;
            sh:maxLength 128 ;
            sh:pattern "^([!#$%&'*+\\-.^_`|~0-9a-zA-Z])+/([!#$%&'*+\\-.^_`|~0-9a-zA-Z])+([ \\t]*;[ \\t]*([!#$%&'*+\\-.^_`|~0-9a-zA-Z])+=(([!#$%&'*+\\-.^_`|~0-9a-zA-Z])+|\"(([\\t !#-\\[\\]-~]|[\\x80-\\xff])|\\\\([\\t !-~]|[\\x80-\\xff]))*\"))*$" ;
        ] ;
    .

    aas-3:CapabilityShape a sh:NodeShape ;
        sh:targetClass aas-3:Capability ;
        sh:node aas-3:SubmodelElementShape ;
    .

    aas-3:ConceptDescriptionShape a sh:NodeShape ;
        sh:targetClass aas-3:ConceptDescription ;
        sh:node aas-3:IdentifiableShape ;
        sh:node aas-3:HasDataSpecificationShape ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:isCaseOf ;
            sh:message "isCaseOf: must be of type Reference."@en ;
            sh:class aas-3:Reference ;
            sh:minCount 0 ;
        ] ;
    .

    aas-3:DataElementShape a sh:NodeShape ;
        sh:targetClass aas-3:DataElement ;
        sh:node aas-3:SubmodelElementShape ;
        sh:sparql [
            a sh:SPARQLConstraint ;
            sh:message "(DataElementShape): An aas-3:DataElement is an abstract class. Please use one of the subclasses for the generation of instances."@en ;
            sh:select """
                SELECT ?this ?type
                WHERE {
                    ?this <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ?type .
                    FILTER (?type = <https://admin-shell.io/aas/3/DataElement>)
                }
            """ ;
        ] ;
    .

    aas-3:DataSpecificationContentShape a sh:NodeShape ;
        sh:targetClass aas-3:DataSpecificationContent ;
        sh:sparql [
            a sh:SPARQLConstraint ;
            sh:message "(DataSpecificationContentShape): An aas-3:DataSpecificationContent is an abstract class. Please use one of the subclasses for the generation of instances."@en ;
            sh:select """
                SELECT ?this ?type
                WHERE {
                    ?this <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ?type .
                    FILTER (?type = <https://admin-shell.io/aas/3/DataSpecificationContent>)
                }
            """ ;
        ] ;
    .

    aas-3:DataSpecificationIec61360Shape a sh:NodeShape ;
        sh:targetClass aas-3:DataSpecificationIec61360 ;
        sh:node aas-3:DataSpecificationContentShape ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-iec61360-3:preferredName ;
            sh:message "preferredName: must be of datatype rdf:langString; at least 1 value(s) required; max length 255."@en ;
            sh:datatype rdf:langString ;
            sh:maxLength 255 ;
            sh:minCount 1 ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-iec61360-3:shortName ;
            sh:message "shortName: must be of datatype rdf:langString; max length 18."@en ;
            sh:datatype rdf:langString ;
            sh:maxLength 18 ;
            sh:minCount 0 ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-iec61360-3:unit ;
            sh:message "unit: must be of datatype string; at most one value allowed; must match the required pattern."@en ;
            sh:datatype xsd:string ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
            sh:minLength 1 ;
            sh:pattern "^([\\u0009\\u000a\\u000d\\u0020-\\ud7ff\\ue000-\\ufffd]|\\ud800[\\udc00-\\udfff]|[\\ud801-\\udbfe][\\udc00-\\udfff]|\\udbff[\\udc00-\\udfff])*$" ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-iec61360-3:unitId ;
            sh:message "unitId: must be of type Reference; at most one value allowed."@en ;
            sh:class aas-3:Reference ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-iec61360-3:sourceOfDefinition ;
            sh:message "sourceOfDefinition: must be of datatype string; at most one value allowed; must match the required pattern."@en ;
            sh:datatype xsd:string ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
            sh:minLength 1 ;
            sh:pattern "^([\\u0009\\u000a\\u000d\\u0020-\\ud7ff\\ue000-\\ufffd]|\\ud800[\\udc00-\\udfff]|[\\ud801-\\udbfe][\\udc00-\\udfff]|\\udbff[\\udc00-\\udfff])*$" ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-iec61360-3:symbol ;
            sh:message "symbol: must be of datatype string; at most one value allowed; must match the required pattern."@en ;
            sh:datatype xsd:string ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
            sh:minLength 1 ;
            sh:pattern "^([\\u0009\\u000a\\u000d\\u0020-\\ud7ff\\ue000-\\ufffd]|\\ud800[\\udc00-\\udfff]|[\\ud801-\\udbfe][\\udc00-\\udfff]|\\udbff[\\udc00-\\udfff])*$" ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-iec61360-3:dataType ;
            sh:message "dataType: must be of type DataTypeIec61360; at most one value allowed."@en ;
            sh:or (
                [ sh:class aas-iec61360-3:DataTypeIec61360 ]
                [ sh:in ( aas-iec61360-3:DataTypeIec61360_Blob aas-iec61360-3:DataTypeIec61360_Boolean aas-iec61360-3:DataTypeIec61360_Date aas-iec61360-3:DataTypeIec61360_File aas-iec61360-3:DataTypeIec61360_Html aas-iec61360-3:DataTypeIec61360_IntegerCount aas-iec61360-3:DataTypeIec61360_IntegerCurrency aas-iec61360-3:DataTypeIec61360_IntegerMeasure aas-iec61360-3:DataTypeIec61360_Irdi aas-iec61360-3:DataTypeIec61360_Iri aas-iec61360-3:DataTypeIec61360_Rational aas-iec61360-3:DataTypeIec61360_RationalMeasure aas-iec61360-3:DataTypeIec61360_RealCount aas-iec61360-3:DataTypeIec61360_RealCurrency aas-iec61360-3:DataTypeIec61360_RealMeasure aas-iec61360-3:DataTypeIec61360_String aas-iec61360-3:DataTypeIec61360_StringTranslatable aas-iec61360-3:DataTypeIec61360_Time aas-iec61360-3:DataTypeIec61360_Timestamp ) ]
            ) ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-iec61360-3:definition ;
            sh:message "definition: must be of datatype rdf:langString; max length 1023."@en ;
            sh:datatype rdf:langString ;
            sh:maxLength 1023 ;
            sh:minCount 0 ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-iec61360-3:valueFormat ;
            sh:message "valueFormat: must be of datatype string; at most one value allowed; must match the required pattern."@en ;
            sh:datatype xsd:string ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
            sh:minLength 1 ;
            sh:pattern "^([\\u0009\\u000a\\u000d\\u0020-\\ud7ff\\ue000-\\ufffd]|\\ud800[\\udc00-\\udfff]|[\\ud801-\\udbfe][\\udc00-\\udfff]|\\udbff[\\udc00-\\udfff])*$" ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-iec61360-3:valueList ;
            sh:message "valueList: must be of type ValueList; at most one value allowed."@en ;
            sh:class aas-iec61360-3:ValueList ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-iec61360-3:value ;
            sh:message "value: must be of datatype string; at most one value allowed; length must be between 1 and 2048; must match the required pattern."@en ;
            sh:datatype xsd:string ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
            sh:minLength 1 ;
            sh:maxLength 2048 ;
            sh:pattern "^([\\u0009\\u000a\\u000d\\u0020-\\ud7ff\\ue000-\\ufffd]|\\ud800[\\udc00-\\udfff]|[\\ud801-\\udbfe][\\udc00-\\udfff]|\\udbff[\\udc00-\\udfff])*$" ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-iec61360-3:levelType ;
            sh:message "levelType: must be of type LevelType; at most one value allowed."@en ;
            sh:class aas-iec61360-3:LevelType ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
        ] ;
    .

    aas-3:EmbeddedDataSpecificationShape a sh:NodeShape ;
        sh:targetClass aas-3:EmbeddedDataSpecification ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:dataSpecification ;
            sh:message "dataSpecification: must be of type Reference; exactly one value required."@en ;
            sh:class aas-3:Reference ;
            sh:minCount 1 ;
            sh:maxCount 1 ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:dataSpecificationContent ;
            sh:message "dataSpecificationContent: must be of type DataSpecificationContent; exactly one value required. Currently only aas-iec61360-3:DataSpecificationIec61360."@en ;

            sh:or (
                [ sh:class aas-3:DataSpecificationContent ]
                [ sh:class aas-iec61360-3:DataSpecificationIec61360 ]
            );
            sh:minCount 1 ;
            sh:maxCount 1 ;
        ] ;
    .

    aas-3:EntityShape a sh:NodeShape ;
        sh:description "AASd-014: Either the attribute globalAssetId or specificAssetId of an Entity must be set if Entity/entityType is SelfManagedEntity." ;
        sh:targetClass aas-3:Entity ;
        sh:node aas-3:SubmodelElementShape ;
        sh:sparql [
            a sh:SPARQLConstraint ;
            sh:message "AASd-014: Either globalAssetId or specificAssetId must be set if entityType is SelfManagedEntity."@en ;
            sh:select """
                SELECT ?this
                WHERE {
                    ?this <https://admin-shell.io/aas/3/entityType> <https://admin-shell.io/aas/3/SelfManagedEntity> .
                    FILTER NOT EXISTS { ?this <https://admin-shell.io/aas/3/globalAssetId> ?gaid }
                    FILTER NOT EXISTS { ?this <https://admin-shell.io/aas/3/specificAssetId> ?said }
                }
            """ ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:statement ;
            sh:message "statement: must be of type SubmodelElement."@en ;
            sh:or (
                [ sh:class aas-3:SubmodelElement ]
                [ sh:class aas-3:AnnotatedRelationshipElement ]
                [ sh:class aas-3:BasicEventElement ]
                [ sh:class aas-3:Blob ]
                [ sh:class aas-3:Capability ]
                [ sh:class aas-3:DataElement ]
                [ sh:class aas-3:Entity ]
                [ sh:class aas-3:EventElement ]
                [ sh:class aas-3:File ]
                [ sh:class aas-3:MultiLanguageProperty ]
                [ sh:class aas-3:Operation ]
                [ sh:class aas-3:Property ]
                [ sh:class aas-3:Range ]
                [ sh:class aas-3:ReferenceElement ]
                [ sh:class aas-3:RelationshipElement ]
                [ sh:class aas-3:SubmodelElementCollection ]
                [ sh:class aas-3:SubmodelElementList ]
            ) ;
            sh:minCount 0 ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:entityType ;
            sh:message "entityType: must be of type EntityType; at most one value allowed."@en ;
            sh:or (
                [ sh:class aas-3:EntityType ]
                [ sh:in ( aas-3:EntityType_CoManagedEntity aas-3:EntityType_SelfManagedEntity ) ]
            ) ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:globalAssetId ;
            sh:message "globalAssetId: must be of datatype string; at most one value allowed; length must be between 1 and 2048; must match the required pattern."@en ;
            sh:datatype xsd:string ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
            sh:minLength 1 ;
            sh:maxLength 2048 ;
            sh:pattern "^([\\u0009\\u000a\\u000d\\u0020-\\ud7ff\\ue000-\\ufffd]|\\ud800[\\udc00-\\udfff]|[\\ud801-\\udbfe][\\udc00-\\udfff]|\\udbff[\\udc00-\\udfff])*$" ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:specificAssetId ;
            sh:message "specificAssetId: must be of type SpecificAssetId."@en ;
            sh:class aas-3:SpecificAssetId ;
            sh:minCount 0 ;
        ] ;
    .

    aas-3:EnvironmentShape a sh:NodeShape ;
        sh:targetClass aas-3:Environment ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:assetAdministrationShell ;
            sh:message "assetAdministrationShell: must be of type AssetAdministrationShell."@en ;
            sh:class aas-3:AssetAdministrationShell ;
            sh:minCount 0 ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:submodel ;
            sh:message "submodel: must be of type Submodel."@en ;
            sh:class aas-3:Submodel ;
            sh:minCount 0 ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:conceptDescription ;
            sh:message "conceptDescription: must be of type ConceptDescription."@en ;
            sh:class aas-3:ConceptDescription ;
            sh:minCount 0 ;
        ] ;
    .

    aas-3:EventElementShape a sh:NodeShape ;
        sh:targetClass aas-3:EventElement ;
        sh:node aas-3:SubmodelElementShape ;
        sh:sparql [
            a sh:SPARQLConstraint ;
            sh:message "(EventElementShape): An aas-3:EventElement is an abstract class. Please use one of the subclasses for the generation of instances."@en ;
            sh:select """
                SELECT ?this ?type
                WHERE {
                    ?this <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ?type .
                    FILTER (?type = <https://admin-shell.io/aas/3/EventElement>)
                }
            """ ;
        ] ;
    .

    aas-3:EventPayloadShape a sh:NodeShape ;
        sh:targetClass aas-3:EventPayload ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:source ;
            sh:message "source: must be of type Reference; exactly one value required."@en ;
            sh:class aas-3:Reference ;
            sh:minCount 1 ;
            sh:maxCount 1 ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:sourceSemanticId ;
            sh:message "sourceSemanticId: must be of type Reference; at most one value allowed."@en ;
            sh:class aas-3:Reference ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:observableReference ;
            sh:message "observableReference: must be of type Reference; exactly one value required."@en ;
            sh:class aas-3:Reference ;
            sh:minCount 1 ;
            sh:maxCount 1 ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:observableSemanticId ;
            sh:message "observableSemanticId: must be of type Reference; at most one value allowed."@en ;
            sh:class aas-3:Reference ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:topic ;
            sh:message "topic: must be of datatype string; at most one value allowed; length must be between 1 and 255; must match the required pattern."@en ;
            sh:datatype xsd:string ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
            sh:minLength 1 ;
            sh:maxLength 255 ;
            sh:pattern "^([\\u0009\\u000a\\u000d\\u0020-\\ud7ff\\ue000-\\ufffd]|\\ud800[\\udc00-\\udfff]|[\\ud801-\\udbfe][\\udc00-\\udfff]|\\udbff[\\udc00-\\udfff])*$" ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:subjectId ;
            sh:message "subjectId: must be of type Reference; at most one value allowed."@en ;
            sh:class aas-3:Reference ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:timeStamp ;
            sh:message "timeStamp: must be of datatype string; exactly one value required; must match the required pattern."@en ;
            sh:datatype xsd:string ;
            sh:minCount 1 ;
            sh:maxCount 1 ;
            sh:pattern "^-?(([1-9][0-9][0-9][0-9]+)|(0[0-9][0-9][0-9]))-((0[1-9])|(1[0-2]))-((0[1-9])|([12][0-9])|(3[01]))T(((([01][0-9])|(2[0-3])):[0-5][0-9]:([0-5][0-9])(\\.[0-9]+)?)|24:00:00(\\.0+)?)(Z|\\+00:00|-00:00)$" ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:payload ;
            sh:message "payload: must be of datatype base64Binary; at most one value allowed."@en ;
            sh:datatype xsd:base64Binary ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
        ] ;
    .

    aas-3:ExtensionShape a sh:NodeShape ;
        sh:targetClass aas-3:Extension ;
        sh:node aas-3:HasSemanticsShape ;
        sh:sparql [
            a sh:SPARQLConstraint ;
            sh:message "The literal value of Extension/value should be consistent with the data type defined in Extension/valueType."@en ;
            sh:select """
                SELECT ?this ?value ?valueType
                WHERE {
                    ?this <https://admin-shell.io/aas/3/value> ?value .
                    ?this <https://admin-shell.io/aas/3/valueType> ?valueType .
                    FILTER (isLiteral(?value) && DATATYPE(?value) != ?valueType)
                }
            """ ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:name ;
            sh:message "name: must be of datatype string; exactly one value required; length must be between 1 and 128; must match the required pattern."@en ;
            sh:datatype xsd:string ;
            sh:minCount 1 ;
            sh:maxCount 1 ;
            sh:minLength 1 ;
            sh:maxLength 128 ;
            sh:pattern "^([\\u0009\\u000a\\u000d\\u0020-\\ud7ff\\ue000-\\ufffd]|\\ud800[\\udc00-\\udfff]|[\\ud801-\\udbfe][\\udc00-\\udfff]|\\udbff[\\udc00-\\udfff])*$" ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:valueType ;
            sh:message "valueType: must be a valid XSD datatype; at most one value allowed."@en ;
            sh:in ( xsd:anyURI xsd:base64Binary xsd:boolean xsd:byte xsd:date xsd:dateTime xsd:decimal xsd:double xsd:duration xsd:float xsd:gDay xsd:gMonth xsd:gMonthDay xsd:gYear xsd:gYearMonth xsd:hexBinary xsd:int xsd:integer xsd:long xsd:negativeInteger xsd:nonNegativeInteger xsd:nonPositiveInteger xsd:positiveInteger xsd:short xsd:string xsd:time xsd:unsignedByte xsd:unsignedInt xsd:unsignedLong xsd:unsignedShort ) ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:value ;
            sh:message "value: must be of matching datatype to valueType; at most one value allowed; must match the required pattern."@en ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:refersTo ;
            sh:message "refersTo: must be of type Reference."@en ;
            sh:class aas-3:Reference ;
            sh:minCount 0 ;
        ] ;
    .

    aas-3:FileShape a sh:NodeShape ;
        sh:targetClass aas-3:File ;
        sh:node aas-3:DataElementShape ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:value ;
            sh:message "value: must be of datatype string in base64; at most one value allowed; length must be at least 1."@en ;
            sh:datatype xsd:string ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
            sh:minLength 1 ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:contentType ;
            sh:message "contentType: must be of datatype string; at most one value allowed; length must be between 1 and 128; must match the required pattern."@en ;
            sh:datatype xsd:string ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
            sh:minLength 1 ;
            sh:maxLength 128 ;
            sh:pattern "^([!#$%&'*+\\-.^_`|~0-9a-zA-Z])+/([!#$%&'*+\\-.^_`|~0-9a-zA-Z])+([ \\t]*;[ \\t]*([!#$%&'*+\\-.^_`|~0-9a-zA-Z])+=(([!#$%&'*+\\-.^_`|~0-9a-zA-Z])+|\"(([\\t !#-\\[\\]-~]|[\\x80-\\xff])|\\\\([\\t !-~]|[\\x80-\\xff]))*\"))*$" ;
        ] ;
    .

    aas-3:HasDataSpecificationShape a sh:NodeShape ;
        sh:targetClass aas-3:HasDataSpecification ;
        sh:sparql [
            a sh:SPARQLConstraint ;
            sh:message "(HasDataSpecificationShape): An aas-3:HasDataSpecification is an abstract class. Please use one of the subclasses for the generation of instances."@en ;
            sh:select """
                SELECT ?this ?type
                WHERE {
                    ?this <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ?type .
                    FILTER (?type = <https://admin-shell.io/aas/3/HasDataSpecification>)
                }
            """ ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:embeddedDataSpecification ;
            sh:message "embeddedDataSpecification: must be of type EmbeddedDataSpecification."@en ;
            sh:class aas-3:EmbeddedDataSpecification ;
            sh:minCount 0 ;
        ] ;
    .

    aas-3:HasExtensionsShape a sh:NodeShape ;
        sh:description "AASd-077: The name of an extension within HasExtensions needs to be unique."@en ;
        sh:targetClass aas-3:HasExtensions ;
        sh:sparql [
            a sh:SPARQLConstraint ;
            sh:message "(HasExtensionsShape): An aas-3:HasExtensions is an abstract class. Please use one of the subclasses for the generation of instances."@en ;
            sh:select """
                SELECT ?this ?type
                WHERE {
                    ?this <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ?type .
                    FILTER (?type = <https://admin-shell.io/aas/3/HasExtensions>)
                }
            """ ;
        ] ;
        sh:sparql [
            a sh:SPARQLConstraint ;
            sh:message "AASd-077: The name of an extension within HasExtensions needs to be unique."@en ;
            sh:select """
                SELECT ?this ?name
                WHERE {
                    ?this <https://admin-shell.io/aas/3/extension> ?ext1 .
                    ?ext1 <https://admin-shell.io/aas/3/name> ?name .
                    ?this <https://admin-shell.io/aas/3/extension> ?ext2 .
                    ?ext2 <https://admin-shell.io/aas/3/name> ?name .
                    FILTER (?ext1 != ?ext2)
                }
            """ ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:extension ;
            sh:message "extension: must be of type Extension."@en ;
            sh:class aas-3:Extension ;
            sh:minCount 0 ;
        ] ;
    .

    aas-3:HasKindShape a sh:NodeShape ;
        sh:targetClass aas-3:HasKind ;
        sh:sparql [
            a sh:SPARQLConstraint ;
            sh:message "(HasKindShape): An aas-3:HasKind is an abstract class. Please use one of the subclasses for the generation of instances."@en ;
            sh:select """
                SELECT ?this ?type
                WHERE {
                    ?this <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ?type .
                    FILTER (?type = <https://admin-shell.io/aas/3/HasKind>)
                }
            """ ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:modelingKind ;
            sh:message "modelingKind: must be of type ModellingKind; at most one value allowed."@en ;
            sh:or (
                [ sh:class aas-3:ModellingKind ]
                [ sh:in ( aas-3:ModellingKind_Instance aas-3:ModellingKind_Template ) ]
            ) ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
        ] ;
    .

    aas-3:HasSemanticsShape a sh:NodeShape ;
        sh:description "AASd-118: If supplementalSemanticIds are used, semanticId shall also be present." ;
        sh:targetClass aas-3:HasSemantics ;
        sh:sparql [
            a sh:SPARQLConstraint ;
            sh:message "(HasSemanticsShape): An aas-3:HasSemantics is an abstract class. Please use one of the subclasses for the generation of instances."@en ;
            sh:select """
                SELECT ?this ?type
                WHERE {
                    ?this <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ?type .
                    FILTER (?type = <https://admin-shell.io/aas/3/HasSemantics>)
                }
            """ ;
        ] ;
        sh:sparql [
            a sh:SPARQLConstraint ;
            sh:message "AASd-118: If supplementalSemanticIds are used, semanticId shall also be present."@en ;
            sh:select """
                SELECT ?this
                WHERE {
                    ?this <https://admin-shell.io/aas/3/supplementalSemanticId> ?supp .
                    FILTER NOT EXISTS { ?this <https://admin-shell.io/aas/3/semanticId> ?sem }
                }
            """ ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:semanticId ;
            sh:message "semanticId: must be of type Reference; at most one value allowed."@en ;
            sh:class aas-3:Reference ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:supplementalSemanticId ;
            sh:message "supplementalSemanticId: must be of type Reference."@en ;
            sh:class aas-3:Reference ;
            sh:minCount 0 ;
        ] ;
    .

    aas-3:IdentifiableShape a sh:NodeShape ;
        sh:targetClass aas-3:Identifiable ;
        sh:node aas-3:ReferableShape ;
        sh:sparql [
            a sh:SPARQLConstraint ;
            sh:message "(IdentifiableShape): An aas-3:Identifiable is an abstract class. Please use one of the subclasses for the generation of instances."@en ;
            sh:select """
                SELECT ?this ?type
                WHERE {
                    ?this <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ?type .
                    FILTER (?type = <https://admin-shell.io/aas/3/Identifiable>)
                }
            """ ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:administration ;
            sh:message "administration: must be of type AdministrativeInformation; at most one value allowed."@en ;
            sh:class aas-3:AdministrativeInformation ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:id ;
            sh:message "id: must be of datatype string; exactly one value required; length must be between 1 and 2048; must match the required pattern."@en ;
            sh:datatype xsd:string ;
            sh:minCount 1 ;
            sh:maxCount 1 ;
            sh:minLength 1 ;
            sh:maxLength 2048 ;
            sh:pattern "^([\\u0009\\u000a\\u000d\\u0020-\\ud7ff\\ue000-\\ufffd]|\\ud800[\\udc00-\\udfff]|[\\ud801-\\udbfe][\\udc00-\\udfff]|\\udbff[\\udc00-\\udfff])*$" ;
        ] ;
    .

    aas-3:KeyShape a sh:NodeShape ;
        sh:targetClass aas-3:Key ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:keyType ;
            sh:message "keyType: must be of type KeyType; exactly one value required."@en ;
            sh:or (
                [ sh:class aas-3:KeyType ]
                [ sh:in ( aas-3:KeyType_AnnotatedRelationshipElement aas-3:KeyType_AssetAdministrationShell aas-3:KeyType_BasicEventElement aas-3:KeyType_Blob aas-3:KeyType_Capability aas-3:KeyType_ConceptDescription aas-3:KeyType_DataElement aas-3:KeyType_Entity aas-3:KeyType_EventElement aas-3:KeyType_File aas-3:KeyType_FragmentReference aas-3:KeyType_GlobalReference aas-3:KeyType_Identifiable aas-3:KeyType_MultiLanguageProperty aas-3:KeyType_Operation aas-3:KeyType_Property aas-3:KeyType_Range aas-3:KeyType_Referable aas-3:KeyType_ReferenceElement aas-3:KeyType_RelationshipElement aas-3:KeyType_Submodel aas-3:KeyType_SubmodelElement aas-3:KeyType_SubmodelElementCollection aas-3:KeyType_SubmodelElementList ) ]
            ) ;
            sh:minCount 1 ;
            sh:maxCount 1 ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:value ;
            sh:message "value: must be of datatype string; exactly one value required; length must be between 1 and 2048; must match the required pattern."@en ;
            sh:datatype xsd:string ;
            sh:minCount 1 ;
            sh:maxCount 1 ;
            sh:minLength 1 ;
            sh:maxLength 2048 ;
            sh:pattern "^([\\u0009\\u000a\\u000d\\u0020-\\ud7ff\\ue000-\\ufffd]|\\ud800[\\udc00-\\udfff]|[\\ud801-\\udbfe][\\udc00-\\udfff]|\\udbff[\\udc00-\\udfff])*$" ;
        ] ;
    .

    ### LangString NodeShapes removed — these types are now simply rdf:langString.
    ### Constraints (maxLength) are enforced inline in the property shapes that use them.

    aas-3:LevelTypeShape a sh:NodeShape ;
        sh:targetClass aas-iec61360-3:LevelType ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-iec61360-3:min ;
            sh:message "min: must be of datatype boolean; exactly one value required."@en ;
            sh:datatype xsd:boolean ;
            sh:minCount 1 ;
            sh:maxCount 1 ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-iec61360-3:nom ;
            sh:message "nom: must be of datatype boolean; exactly one value required."@en ;
            sh:datatype xsd:boolean ;
            sh:minCount 1 ;
            sh:maxCount 1 ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-iec61360-3:typ ;
            sh:message "typ: must be of datatype boolean; exactly one value required."@en ;
            sh:datatype xsd:boolean ;
            sh:minCount 1 ;
            sh:maxCount 1 ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-iec61360-3:max ;
            sh:message "max: must be of datatype boolean; exactly one value required."@en ;
            sh:datatype xsd:boolean ;
            sh:minCount 1 ;
            sh:maxCount 1 ;
        ] ;
    .

    aas-3:MultiLanguagePropertyShape a sh:NodeShape ;
        sh:targetClass aas-3:MultiLanguageProperty ;
        sh:node aas-3:DataElementShape ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:value ;
            sh:message "value: must be of datatype rdf:langString;"@en ;
            sh:datatype rdf:langString ;
            sh:minCount 0 ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:valueId ;
            sh:message "valueId: must be of type Reference; at most one value allowed."@en ;
            sh:class aas-3:Reference ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
        ] ;
    .

    aas-3:OperationShape a sh:NodeShape ;
        sh:description "AASd-134: For an Operation, the idShort of all inputVariable/value, outputVariable/value, and inoutputVariable/value shall be unique." ;
        sh:targetClass aas-3:Operation ;
        sh:node aas-3:SubmodelElementShape ;
        sh:sparql [
            a sh:SPARQLConstraint ;
            sh:message "AASd-134: For an Operation, the idShort of all inputVariable/value, outputVariable/value, and inoutputVariable/value shall be unique."@en ;
            sh:select """
                SELECT ?this ?idShort
                WHERE {
                    {
                        { ?this <https://admin-shell.io/aas/3/inputVariable> ?var1 . ?var1 <https://admin-shell.io/aas/3/value> ?val1 . }
                        UNION
                        { ?this <https://admin-shell.io/aas/3/outputVariable> ?var1 . ?var1 <https://admin-shell.io/aas/3/value> ?val1 . }
                        UNION
                        { ?this <https://admin-shell.io/aas/3/inoutputVariable> ?var1 . ?var1 <https://admin-shell.io/aas/3/value> ?val1 . }
                    }
                    ?val1 <https://admin-shell.io/aas/3/idShort> ?idShort .
                    {
                        { ?this <https://admin-shell.io/aas/3/inputVariable> ?var2 . ?var2 <https://admin-shell.io/aas/3/value> ?val2 . }
                        UNION
                        { ?this <https://admin-shell.io/aas/3/outputVariable> ?var2 . ?var2 <https://admin-shell.io/aas/3/value> ?val2 . }
                        UNION
                        { ?this <https://admin-shell.io/aas/3/inoutputVariable> ?var2 . ?var2 <https://admin-shell.io/aas/3/value> ?val2 . }
                    }
                    ?val2 <https://admin-shell.io/aas/3/idShort> ?idShort .
                    FILTER (?val1 != ?val2)
                }
            """ ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:inputVariable ;
            sh:message "inputVariable: must be of type OperationVariable."@en ;
            sh:class aas-3:OperationVariable ;
            sh:minCount 0 ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:outputVariable ;
            sh:message "outputVariable: must be of type OperationVariable."@en ;
            sh:class aas-3:OperationVariable ;
            sh:minCount 0 ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:inoutputVariable ;
            sh:message "inoutputVariable: must be of type OperationVariable."@en ;
            sh:class aas-3:OperationVariable ;
            sh:minCount 0 ;
        ] ;
    .

    aas-3:OperationVariableShape a sh:NodeShape ;
        sh:targetClass aas-3:OperationVariable ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:value ;
            sh:message "value: must be of type SubmodelElement; exactly one value required."@en ;
            sh:or (
                [ sh:class aas-3:SubmodelElement ]
                [ sh:class aas-3:AnnotatedRelationshipElement ]
                [ sh:class aas-3:BasicEventElement ]
                [ sh:class aas-3:Blob ]
                [ sh:class aas-3:Capability ]
                [ sh:class aas-3:DataElement ]
                [ sh:class aas-3:Entity ]
                [ sh:class aas-3:EventElement ]
                [ sh:class aas-3:File ]
                [ sh:class aas-3:MultiLanguageProperty ]
                [ sh:class aas-3:Operation ]
                [ sh:class aas-3:Property ]
                [ sh:class aas-3:Range ]
                [ sh:class aas-3:ReferenceElement ]
                [ sh:class aas-3:RelationshipElement ]
                [ sh:class aas-3:SubmodelElementCollection ]
                [ sh:class aas-3:SubmodelElementList ]
            ) ;
            sh:minCount 1 ;
            sh:maxCount 1 ;
        ] ;
    .

    aas-3:PropertyShape a sh:NodeShape ;
        sh:description "AASd-007: If both Property/value and Property/valueId are present, the value of Property/value needs to be identical to the value of the referenced coded value in Property/valueId." ;
        sh:targetClass aas-3:Property ;
        sh:node aas-3:DataElementShape ;
        sh:sparql [
            a sh:SPARQLConstraint ;
            sh:message "The literal value of Property/value should be consistent with the data type defined in Property/valueType."@en ;
            sh:select """
                SELECT ?this ?value ?valueType
                WHERE {
                    ?this <https://admin-shell.io/aas/3/value> ?value .
                    ?this <https://admin-shell.io/aas/3/valueType> ?valueType .
                    FILTER (isLiteral(?value) && DATATYPE(?value) != ?valueType)
                }
            """ ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:valueType ;
            sh:message "valueType: must be a valid XSD datatype; exactly one value required."@en ;
            sh:in ( xsd:anyURI xsd:base64Binary xsd:boolean xsd:byte xsd:date xsd:dateTime xsd:decimal xsd:double xsd:duration xsd:float xsd:gDay xsd:gMonth xsd:gMonthDay xsd:gYear xsd:gYearMonth xsd:hexBinary xsd:int xsd:integer xsd:long xsd:negativeInteger xsd:nonNegativeInteger xsd:nonPositiveInteger xsd:positiveInteger xsd:short xsd:string xsd:time xsd:unsignedByte xsd:unsignedInt xsd:unsignedLong xsd:unsignedShort ) ;
            sh:minCount 1 ;
            sh:maxCount 1 ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:value ;
            sh:message "value: must be of matching datatype to valueType; at most one value allowed."@en ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:valueId ;
            sh:message "valueId: must be of type Reference; at most one value allowed."@en ;
            sh:class aas-3:Reference ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
        ] ;
    .

    aas-3:QualifiableShape a sh:NodeShape ;
        sh:description "AASd-021: Every Qualifiable can only have one Qualifier with the same Qualifier/type." ;
        sh:targetClass aas-3:Qualifiable ;
        sh:sparql [
            a sh:SPARQLConstraint ;
            sh:message "(QualifiableShape): An aas-3:Qualifiable is an abstract class. Please use one of the subclasses for the generation of instances."@en ;
            sh:select """
                SELECT ?this ?type
                WHERE {
                    ?this <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ?type .
                    FILTER (?type = <https://admin-shell.io/aas/3/Qualifiable>)
                }
            """ ;
        ] ;
        sh:sparql [
            a sh:SPARQLConstraint ;
            sh:message "AASd-021: Every Qualifiable can only have one Qualifier with the same Qualifier/type."@en ;
            sh:select """
                SELECT ?this ?qualType
                WHERE {
                    ?this <https://admin-shell.io/aas/3/qualifier> ?q1 .
                    ?q1 <https://admin-shell.io/aas/3/qualifierType> ?qualType .
                    ?this <https://admin-shell.io/aas/3/qualifier> ?q2 .
                    ?q2 <https://admin-shell.io/aas/3/qualifierType> ?qualType .
                    FILTER (?q1 != ?q2)
                }
            """ ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:qualifier ;
            sh:message "qualifier: must be of type Qualifier."@en ;
            sh:class aas-3:Qualifier ;
            sh:minCount 0 ;
        ] ;
    .

    aas-3:QualifierShape a sh:NodeShape ;
        sh:description "AASd-006: If both Qualifier/value and Qualifier/valueId are present, the value shall be identical. AASd-020: The value of Qualifier/value shall be consistent with the data type as defined in Qualifier/valueType." ;
        sh:targetClass aas-3:Qualifier ;
        sh:node aas-3:HasSemanticsShape ;
        sh:sparql [
            a sh:SPARQLConstraint ;
            sh:message "AASd-020: The literal value of Qualifier/value should be consistent with the data type defined in Qualifier/valueType."@en ;
            sh:select """
                SELECT ?this ?value ?valueType
                WHERE {
                    ?this <https://admin-shell.io/aas/3/value> ?value .
                    ?this <https://admin-shell.io/aas/3/valueType> ?valueType .
                    FILTER (isLiteral(?value) && DATATYPE(?value) != ?valueType)
                }
            """ ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:qualifierKind ;
            sh:message "qualifierKind: must be of type QualifierKind; at most one value allowed."@en ;
            sh:or (
                [ sh:class aas-3:QualifierKind ]
                [ sh:in ( aas-3:QualifierKind_ConceptQualifier aas-3:QualifierKind_TemplateQualifier aas-3:QualifierKind_ValueQualifier ) ]
            ) ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:qualifierType ;
            sh:message "qualifierType: must be of datatype string; exactly one value required; length must be between 1 and 128; must match the required pattern."@en ;
            sh:datatype xsd:string ;
            sh:minCount 1 ;
            sh:maxCount 1 ;
            sh:minLength 1 ;
            sh:maxLength 128 ;
            sh:pattern "^([\\u0009\\u000a\\u000d\\u0020-\\ud7ff\\ue000-\\ufffd]|\\ud800[\\udc00-\\udfff]|[\\ud801-\\udbfe][\\udc00-\\udfff]|\\udbff[\\udc00-\\udfff])*$" ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:valueType ;
            sh:message "valueType: must be a valid XSD datatype; exactly one value required."@en ;
            sh:in ( xsd:anyURI xsd:base64Binary xsd:boolean xsd:byte xsd:date xsd:dateTime xsd:decimal xsd:double xsd:duration xsd:float xsd:gDay xsd:gMonth xsd:gMonthDay xsd:gYear xsd:gYearMonth xsd:hexBinary xsd:int xsd:integer xsd:long xsd:negativeInteger xsd:nonNegativeInteger xsd:nonPositiveInteger xsd:positiveInteger xsd:short xsd:string xsd:time xsd:unsignedByte xsd:unsignedInt xsd:unsignedLong xsd:unsignedShort ) ;
            sh:minCount 1 ;
            sh:maxCount 1 ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:value ;
            sh:message "value: must be of matching datatype to valueType; at most one value allowed; must match the required pattern."@en ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:valueId ;
            sh:message "valueId: must be of type Reference; at most one value allowed."@en ;
            sh:class aas-3:Reference ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
        ] ;
    .

    aas-3:RangeShape a sh:NodeShape ;
        sh:targetClass aas-3:Range ;
        sh:node aas-3:DataElementShape ;
        sh:sparql [
            a sh:SPARQLConstraint ;
            sh:message "The literal value of Range/min should be consistent with the data type defined in Range/valueType."@en ;
            sh:select """
                SELECT ?this ?minVal ?valueType
                WHERE {
                    ?this <https://admin-shell.io/aas/3/min> ?minVal .
                    ?this <https://admin-shell.io/aas/3/valueType> ?valueType .
                    FILTER (isLiteral(?minVal) && DATATYPE(?minVal) != ?valueType)
                }
            """ ;
        ] ;
        sh:sparql [
            a sh:SPARQLConstraint ;
            sh:message "The literal value of Range/max should be consistent with the data type defined in Range/valueType."@en ;
            sh:select """
                SELECT ?this ?maxVal ?valueType
                WHERE {
                    ?this <https://admin-shell.io/aas/3/max> ?maxVal .
                    ?this <https://admin-shell.io/aas/3/valueType> ?valueType .
                    FILTER (isLiteral(?maxVal) && DATATYPE(?maxVal) != ?valueType)
                }
            """ ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:valueType ;
            sh:message "valueType: must be a valid XSD datatype; exactly one value required."@en ;
            sh:in ( xsd:anyURI xsd:base64Binary xsd:boolean xsd:byte xsd:date xsd:dateTime xsd:decimal xsd:double xsd:duration xsd:float xsd:gDay xsd:gMonth xsd:gMonthDay xsd:gYear xsd:gYearMonth xsd:hexBinary xsd:int xsd:integer xsd:long xsd:negativeInteger xsd:nonNegativeInteger xsd:nonPositiveInteger xsd:positiveInteger xsd:short xsd:string xsd:time xsd:unsignedByte xsd:unsignedInt xsd:unsignedLong xsd:unsignedShort ) ;
            sh:minCount 1 ;
            sh:maxCount 1 ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:min ;
            sh:message "min: must be of matching datatype to valueType; at most one value allowed."@en ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:max ;
            sh:message "max: must be of matching datatype to valueType; at most one value allowed."@en ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
        ] ;
    .

    aas-3:ReferableShape a sh:NodeShape ;
        sh:targetClass aas-3:Referable ;
        sh:node aas-3:HasExtensionsShape ;
        sh:sparql [
            a sh:SPARQLConstraint ;
            sh:message "(ReferableShape): An aas-3:Referable is an abstract class. Please use one of the subclasses for the generation of instances."@en ;
            sh:select """
                SELECT ?this ?type
                WHERE {
                    ?this <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ?type .
                    FILTER (?type = <https://admin-shell.io/aas/3/Referable>)
                }
            """ ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:category ;
            sh:message "category: must be of datatype string; at most one value allowed; length must be between 1 and 128; must match the required pattern."@en ;
            sh:datatype xsd:string ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
            sh:minLength 1 ;
            sh:maxLength 128 ;
            sh:pattern "^([\\u0009\\u000a\\u000d\\u0020-\\ud7ff\\ue000-\\ufffd]|\\ud800[\\udc00-\\udfff]|[\\ud801-\\udbfe][\\udc00-\\udfff]|\\udbff[\\udc00-\\udfff])*$" ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:idShort ;
            sh:message "idShort: must be of datatype string; at most one value allowed; length must be between 1 and 128; must match the required pattern."@en ;
            sh:datatype xsd:string ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
            sh:minLength 1 ;
            sh:maxLength 128 ;
            sh:pattern "^[a-zA-Z][a-zA-Z0-9_-]*[a-zA-Z0-9_]+$" ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:displayName ;
            sh:message "displayName: must be of datatype rdf:langString; max length 128."@en ;
            sh:datatype rdf:langString ;
            sh:maxLength 128 ;
            sh:minCount 0 ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:description ;
            sh:message "description: must be of datatype rdf:langString; max length 1023."@en ;
            sh:datatype rdf:langString ;
            sh:maxLength 1023 ;
            sh:minCount 0 ;
        ] ;
    .

    aas-3:ReferenceShape a sh:NodeShape ;
        sh:description "AASd-121 to AASd-128: Constraints on key types depending on referenceType (ModelReference vs ExternalReference)." ;
        sh:targetClass aas-3:Reference ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:referenceType ;
            sh:message "referenceType: must be of type ReferenceType; exactly one value required."@en ;
            sh:or (
                [ sh:class aas-3:ReferenceType ]
                [ sh:in ( aas-3:ReferenceType_ExternalReference aas-3:ReferenceType_ModelReference ) ]
            ) ;
            sh:minCount 1 ;
            sh:maxCount 1 ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:referredSemanticId ;
            sh:message "referredSemanticId: must be of type Reference; at most one value allowed."@en ;
            sh:class aas-3:Reference ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:key ;
            sh:message "key: must be of type Key; at least 1 value(s) required."@en ;
            sh:class aas-3:Key ;
            sh:minCount 1 ;
        ] ;
    .

    aas-3:ReferenceElementShape a sh:NodeShape ;
        sh:targetClass aas-3:ReferenceElement ;
        sh:node aas-3:DataElementShape ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:value ;
            sh:message "value: must be of type Reference; at most one value allowed."@en ;
            sh:class aas-3:Reference ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
        ] ;
    .

    aas-3:RelationshipElementShape a sh:NodeShape ;
        sh:targetClass aas-3:RelationshipElement ;
        sh:node aas-3:SubmodelElementShape ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:first ;
            sh:message "first: must be of type Reference; at most one value allowed."@en ;
            sh:class aas-3:Reference ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:second ;
            sh:message "second: must be of type Reference; at most one value allowed."@en ;
            sh:class aas-3:Reference ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
        ] ;
    .

    aas-3:ResourceShape a sh:NodeShape ;
        sh:targetClass aas-3:Resource ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:path ;
            sh:message "path: must be of datatype string; exactly one value required; length must be between 1 and 2048; must match the required pattern."@en ;
            sh:datatype xsd:string ;
            sh:minCount 1 ;
            sh:maxCount 1 ;
            sh:minLength 1 ;
            sh:maxLength 2048 ;
            sh:pattern "^([a-zA-Z][a-zA-Z0-9+\\-.]*:((//((((([a-zA-Z0-9]|[-_.!~*'()])|%([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])|[;:&=+$,])*@)?((([a-zA-Z0-9]|[a-zA-Z0-9]([a-zA-Z0-9]|-)*[a-zA-Z0-9])\\.)*([a-zA-Z]|[a-zA-Z]([a-zA-Z0-9]|-)*[a-zA-Z0-9])(\\.)?|[0-9]+\\.[0-9]+\\.[0-9]+\\.[0-9]+)(:[0-9]*)?)?|(([a-zA-Z0-9]|[-_.!~*'()])|%([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])|[$,;:@&=+])+)(/((([a-zA-Z0-9]|[-_.!~*'()])|%([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])|[:@&=+$,]))*(;((([a-zA-Z0-9]|[-_.!~*'()])|%([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])|[:@&=+$,]))*)*(/((([a-zA-Z0-9]|[-_.!~*'()])|%([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])|[:@&=+$,]))*(;((([a-zA-Z0-9]|[-_.!~*'()])|%([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])|[:@&=+$,]))*)*)*)?|/((([a-zA-Z0-9]|[-_.!~*'()])|%([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])|[:@&=+$,]))*(;((([a-zA-Z0-9]|[-_.!~*'()])|%([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])|[:@&=+$,]))*)*(/((([a-zA-Z0-9]|[-_.!~*'()])|%([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])|[:@&=+$,]))*(;((([a-zA-Z0-9]|[-_.!~*'()])|%([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])|[:@&=+$,]))*)*)*)(\\?(([;/?:@&=+$,]|([a-zA-Z0-9]|[-_.!~*'()])|%([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])))*)?|(([a-zA-Z0-9]|[-_.!~*'()])|%([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])|[;?:@&=+$,])(([;/?:@&=+$,]|([a-zA-Z0-9]|[-_.!~*'()])|%([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])))*)|(//((((([a-zA-Z0-9]|[-_.!~*'()])|%([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])|[;:&=+$,])*@)?((([a-zA-Z0-9]|[a-zA-Z0-9]([a-zA-Z0-9]|-)*[a-zA-Z0-9])\\.)*([a-zA-Z]|[a-zA-Z]([a-zA-Z0-9]|-)*[a-zA-Z0-9])(\\.)?|[0-9]+\\.[0-9]+\\.[0-9]+\\.[0-9]+)(:[0-9]*)?)?|(([a-zA-Z0-9]|[-_.!~*'()])|%([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])|[$,;:@&=+])+)(/((([a-zA-Z0-9]|[-_.!~*'()])|%([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])|[:@&=+$,]))*(;((([a-zA-Z0-9]|[-_.!~*'()])|%([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])|[:@&=+$,]))*)*(/((([a-zA-Z0-9]|[-_.!~*'()])|%([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])|[:@&=+$,]))*(;((([a-zA-Z0-9]|[-_.!~*'()])|%([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])|[:@&=+$,]))*)*)*)?|/((([a-zA-Z0-9]|[-_.!~*'()])|%([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])|[:@&=+$,]))*(;((([a-zA-Z0-9]|[-_.!~*'()])|%([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])|[:@&=+$,]))*)*(/((([a-zA-Z0-9]|[-_.!~*'()])|%([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])|[:@&=+$,]))*(;((([a-zA-Z0-9]|[-_.!~*'()])|%([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])|[:@&=+$,]))*)*)*|(([a-zA-Z0-9]|[-_.!~*'()])|%([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])|[;@&=+$,])+(/((([a-zA-Z0-9]|[-_.!~*'()])|%([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])|[:@&=+$,]))*(;((([a-zA-Z0-9]|[-_.!~*'()])|%([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])|[:@&=+$,]))*)*(/((([a-zA-Z0-9]|[-_.!~*'()])|%([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])|[:@&=+$,]))*(;((([a-zA-Z0-9]|[-_.!~*'()])|%([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])|[:@&=+$,]))*)*)*)?)(\\?(([;/?:@&=+$,]|([a-zA-Z0-9]|[-_.!~*'()])|%([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])))*)?)?(#(([;/?:@&=+$,]|([a-zA-Z0-9]|[-_.!~*'()])|%([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])([0-9]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF]|[aA]|[bB]|[cC]|[dD]|[eE]|[fF])))*)?$" ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:contentType ;
            sh:message "contentType: must be of datatype string; at most one value allowed; length must be between 1 and 128; must match the required pattern."@en ;
            sh:datatype xsd:string ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
            sh:minLength 1 ;
            sh:maxLength 128 ;
            sh:pattern "^([!#$%&'*+\\-.^_`|~0-9a-zA-Z])+/([!#$%&'*+\\-.^_`|~0-9a-zA-Z])+([ \\t]*;[ \\t]*([!#$%&'*+\\-.^_`|~0-9a-zA-Z])+=(([!#$%&'*+\\-.^_`|~0-9a-zA-Z])+|\"(([\\t !#-\\[\\]-~]|[\\x80-\\xff])|\\\\([\\t !-~]|[\\x80-\\xff]))*\"))*$" ;
        ] ;
    .

    aas-3:SpecificAssetIdShape a sh:NodeShape ;
        sh:description "AASd-133: The externalSubjectId of a SpecificAssetId must be an ExternalReference." ;
        sh:targetClass aas-3:SpecificAssetId ;
        sh:node aas-3:HasSemanticsShape ;
        sh:sparql [
            a sh:SPARQLConstraint ;
            sh:message "AASd-133: The externalSubjectId of a SpecificAssetId must be an ExternalReference (referenceType = ExternalReference)."@en ;
            sh:select """
                SELECT ?this ?ref
                WHERE {
                    ?this <https://admin-shell.io/aas/3/externalSubjectId> ?ref .
                    ?ref <https://admin-shell.io/aas/3/referenceType> ?refType .
                    FILTER (?refType != <https://admin-shell.io/aas/3/ReferenceType_ExternalReference>)
                }
            """ ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:name ;
            sh:message "name: must be of datatype string; exactly one value required; length must be between 1 and 64; must match the required pattern."@en ;
            sh:datatype xsd:string ;
            sh:minCount 1 ;
            sh:maxCount 1 ;
            sh:minLength 1 ;
            sh:maxLength 64 ;
            sh:pattern "^([\\u0009\\u000a\\u000d\\u0020-\\ud7ff\\ue000-\\ufffd]|\\ud800[\\udc00-\\udfff]|[\\ud801-\\udbfe][\\udc00-\\udfff]|\\udbff[\\udc00-\\udfff])*$" ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:value ;
            sh:message "value: must be of datatype string; exactly one value required; length must be between 1 and 2048; must match the required pattern."@en ;
            sh:datatype xsd:string ;
            sh:minCount 1 ;
            sh:maxCount 1 ;
            sh:minLength 1 ;
            sh:maxLength 2048 ;
            sh:pattern "^([\\u0009\\u000a\\u000d\\u0020-\\ud7ff\\ue000-\\ufffd]|\\ud800[\\udc00-\\udfff]|[\\ud801-\\udbfe][\\udc00-\\udfff]|\\udbff[\\udc00-\\udfff])*$" ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:externalSubjectId ;
            sh:message "externalSubjectId: must be of type Reference; at most one value allowed."@en ;
            sh:class aas-3:Reference ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
        ] ;
    .

    aas-3:SubmodelShape a sh:NodeShape ;
        sh:targetClass aas-3:Submodel ;
        sh:node aas-3:IdentifiableShape ;
        sh:node aas-3:HasKindShape ;
        sh:node aas-3:HasSemanticsShape ;
        sh:node aas-3:QualifiableShape ;
        sh:node aas-3:HasDataSpecificationShape ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:submodelElement ;
            sh:message "submodelElement: must be of type SubmodelElement."@en ;
            sh:class aas-3:SubmodelElement ;
            sh:minCount 0 ;
        ] ;
    .

    aas-3:SubmodelElementShape a sh:NodeShape ;
        sh:targetClass aas-3:SubmodelElement ;
        sh:node aas-3:ReferableShape ;
        sh:node aas-3:HasSemanticsShape ;
        sh:node aas-3:QualifiableShape ;
        sh:node aas-3:HasDataSpecificationShape ;
        sh:sparql [
            a sh:SPARQLConstraint ;
            sh:message "(SubmodelElementShape): An aas-3:SubmodelElement is an abstract class. Please use one of the subclasses for the generation of instances."@en ;
            sh:select """
                SELECT ?this ?type
                WHERE {
                    ?this <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ?type .
                    FILTER (?type = <https://admin-shell.io/aas/3/SubmodelElement>)
                }
            """ ;
        ] ;
    .

    aas-3:SubmodelElementCollectionShape a sh:NodeShape ;
        sh:targetClass aas-3:SubmodelElementCollection ;
        sh:node aas-3:SubmodelElementShape ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:value ;
            sh:message "value: must be of type SubmodelElement."@en ;
            sh:or (
                [ sh:class aas-3:SubmodelElement ]
                [ sh:class aas-3:AnnotatedRelationshipElement ]
                [ sh:class aas-3:BasicEventElement ]
                [ sh:class aas-3:Blob ]
                [ sh:class aas-3:Capability ]
                [ sh:class aas-3:DataElement ]
                [ sh:class aas-3:Entity ]
                [ sh:class aas-3:EventElement ]
                [ sh:class aas-3:File ]
                [ sh:class aas-3:MultiLanguageProperty ]
                [ sh:class aas-3:Operation ]
                [ sh:class aas-3:Property ]
                [ sh:class aas-3:Range ]
                [ sh:class aas-3:ReferenceElement ]
                [ sh:class aas-3:RelationshipElement ]
                [ sh:class aas-3:SubmodelElementCollection ]
                [ sh:class aas-3:SubmodelElementList ]
            ) ;
            sh:minCount 0 ;
        ] ;
    .

    aas-3:SubmodelElementListShape a sh:NodeShape ;
        sh:description "AASd-107, AASd-114: semanticId must apply to all elements. AASd-108: type of elements must match typeValueListElement. AASd-109: valueType required when typeValueListElement is Property or Range. AASd-120: idShort of children shall not be set." ;
        sh:targetClass aas-3:SubmodelElementList ;
        sh:node aas-3:SubmodelElementShape ;
        sh:sparql [
            a sh:SPARQLConstraint ;
            sh:message "AASd-108: All first level child elements in a SubmodelElementList shall have the same submodel element type as specified in typeValueListElement."@en ;
            sh:select """
                SELECT ?this ?element ?typeValueListElement
                WHERE {
                    ?this <https://admin-shell.io/aas/3/value> ?element .
                    ?this <https://admin-shell.io/aas/3/typeValueListElement> ?typeValueListElement .
                    FILTER NOT EXISTS { ?element <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ?typeValueListElement }
                }
            """ ;
        ] ;
        sh:sparql [
            a sh:SPARQLConstraint ;
            sh:message "AASd-109: If typeValueListElement is Property or Range, valueTypeListElement shall be set."@en ;
            sh:select """
                SELECT ?this ?typeValueListElement
                WHERE {
                    ?this <https://admin-shell.io/aas/3/typeValueListElement> ?typeValueListElement .
                    FILTER (
                        ?typeValueListElement = <https://admin-shell.io/aas/3/Property>
                        || ?typeValueListElement = <https://admin-shell.io/aas/3/Range>
                    )
                    FILTER NOT EXISTS { ?this <https://admin-shell.io/aas/3/valueTypeListElement> ?vtl }
                }
            """ ;
        ] ;
        sh:sparql [
            a sh:SPARQLConstraint ;
            sh:message "AASd-109: All first level child elements shall have the valueType as specified in valueTypeListElement."@en ;
            sh:select """
                SELECT ?this ?element ?childValueType ?valueTypeListElement
                WHERE {
                    ?this <https://admin-shell.io/aas/3/typeValueListElement> ?typeValueListElement .
                    FILTER (
                        ?typeValueListElement = <https://admin-shell.io/aas/3/Property>
                        || ?typeValueListElement = <https://admin-shell.io/aas/3/Range>
                    )
                    ?this <https://admin-shell.io/aas/3/valueTypeListElement> ?valueTypeListElement .
                    ?this <https://admin-shell.io/aas/3/value> ?element .
                    ?element <https://admin-shell.io/aas/3/valueType> ?childValueType .
                    FILTER (?childValueType != ?valueTypeListElement)
                }
            """ ;
        ] ;
        sh:sparql [
            a sh:SPARQLConstraint ;
            sh:message "AASd-120: idShort of submodel elements being a direct child of a SubmodelElementList shall not be specified."@en ;
            sh:select """
                SELECT ?this ?element ?idShort
                WHERE {
                    ?this <https://admin-shell.io/aas/3/value> ?element .
                    ?element <https://admin-shell.io/aas/3/idShort> ?idShort .
                }
            """ ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:orderRelevant ;
            sh:message "orderRelevant: must be of datatype boolean; at most one value allowed."@en ;
            sh:datatype xsd:boolean ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:semanticIdListElement ;
            sh:message "semanticIdListElement: must be of type Reference; at most one value allowed."@en ;
            sh:class aas-3:Reference ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:typeValueListElement ;
            sh:message "typeValueListElement: must be of type AasSubmodelElements; exactly one value required."@en ;
            sh:in (
                aas-3:AnnotatedRelationshipElement
                aas-3:BasicEventElement
                aas-3:Blob
                aas-3:Capability
                aas-3:DataElement
                aas-3:Entity
                aas-3:EventElement
                aas-3:File
                aas-3:MultiLanguageProperty
                aas-3:Operation
                aas-3:Property
                aas-3:Range
                aas-3:ReferenceElement
                aas-3:RelationshipElement
                aas-3:SubmodelElement
                aas-3:SubmodelElementCollection
                aas-3:SubmodelElementList
            ) ;
            sh:minCount 1 ;
            sh:maxCount 1 ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:valueType ;
            sh:message "valueType: must be a valid XSD datatype; at most one value allowed."@en ;
            sh:in ( xsd:anyURI xsd:base64Binary xsd:boolean xsd:byte xsd:date xsd:dateTime xsd:decimal xsd:double xsd:duration xsd:float xsd:gDay xsd:gMonth xsd:gMonthDay xsd:gYear xsd:gYearMonth xsd:hexBinary xsd:int xsd:integer xsd:long xsd:negativeInteger xsd:nonNegativeInteger xsd:nonPositiveInteger xsd:positiveInteger xsd:short xsd:string xsd:time xsd:unsignedByte xsd:unsignedInt xsd:unsignedLong xsd:unsignedShort ) ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:value ;
            sh:message "value: must be of type SubmodelElement."@en ;
            sh:or (
                [ sh:class aas-3:SubmodelElement ]
                [ sh:class aas-3:AnnotatedRelationshipElement ]
                [ sh:class aas-3:BasicEventElement ]
                [ sh:class aas-3:Blob ]
                [ sh:class aas-3:Capability ]
                [ sh:class aas-3:DataElement ]
                [ sh:class aas-3:Entity ]
                [ sh:class aas-3:EventElement ]
                [ sh:class aas-3:File ]
                [ sh:class aas-3:MultiLanguageProperty ]
                [ sh:class aas-3:Operation ]
                [ sh:class aas-3:Property ]
                [ sh:class aas-3:Range ]
                [ sh:class aas-3:ReferenceElement ]
                [ sh:class aas-3:RelationshipElement ]
                [ sh:class aas-3:SubmodelElementCollection ]
                [ sh:class aas-3:SubmodelElementList ]
            ) ;
            sh:minCount 0 ;
        ] ;
    .

    aas-3:ValueListShape a sh:NodeShape ;
        sh:targetClass aas-iec61360-3:ValueList ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-iec61360-3:valueReferencePair ;
            sh:message "valueReferencePair: must be of type ValueReferencePair; at least 1 value(s) required."@en ;
            sh:class aas-iec61360-3:ValueReferencePair ;
            sh:minCount 1 ;
        ] ;
    .

    aas-3:ValueReferencePairShape a sh:NodeShape ;
        sh:targetClass aas-iec61360-3:ValueReferencePair ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:value ;
            sh:message "value: must be of datatype string; exactly one value required; length must be between 1 and 2048; must match the required pattern."@en ;
            sh:datatype xsd:string ;
            sh:minCount 1 ;
            sh:maxCount 1 ;
            sh:minLength 1 ;
            sh:maxLength 2048 ;
            sh:pattern "^([\\u0009\\u000a\\u000d\\u0020-\\ud7ff\\ue000-\\ufffd]|\\ud800[\\udc00-\\udfff]|[\\ud801-\\udbfe][\\udc00-\\udfff]|\\udbff[\\udc00-\\udfff])*$" ;
        ] ;
        sh:property [
            a sh:PropertyShape ;
            sh:path aas-3:valueId ;
            sh:message "valueId: must be of type Reference; at most one value allowed."@en ;
            sh:class aas-3:Reference ;
            sh:minCount 0 ;
            sh:maxCount 1 ;
        ] ;
    .
        '''
    AAS_SHACL_3_0 = """"""
    AAS_SHACL_3 = AAS_SHACL_3_1

    AAS_JSON_LD_CONTEXT_3 = """
{
  "@context": {
    "aas": "https://admin-shell.io/aas/3/",
    "iec61360": "https://admin-shell.io/DataSpecificationTemplates/DataSpecificationIec61360/3/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "@vocab": "https://admin-shell.io/aas/3/",
    "modelType": "@type",

    "semanticId": {
      "@id": "aas:semanticId",
      "@type": "@id"
    },
    "supplementalSemanticId": {
      "@id": "aas:supplementalSemanticId",
      "@container": "@set",
      "@type": "@id"
    },
    "extension": {
      "@id": "aas:extension",
      "@container": "@set",
      "@type": "@id"
    },
    "refersTo": {
      "@id": "aas:refersTo",
      "@container": "@set",
      "@type": "@id"
    },
    "category": {
      "@id": "aas:category"
    },
    "idShort": {
      "@id": "aas:idShort"
    },
    "displayName": {
      "@id": "aas:displayName",
      "@container": "@language"
    },
    "description": {
      "@id": "aas:description",
      "@container": "@language"
    },
    "administration": {
      "@id": "aas:administration",
      "@type": "@id"
    },
    "id": {
      "@id": "aas:id"
    },
    "embeddedDataSpecification": {
      "@id": "aas:embeddedDataSpecification",
      "@container": "@set",
      "@type": "@id"
    },
    "version": {
      "@id": "aas:version"
    },
    "revision": {
      "@id": "aas:revision"
    },
    "creator": {
      "@id": "aas:creator",
      "@type": "@id"
    },
    "templateId": {
      "@id": "aas:templateId"
    },
    "modelingKind": {
      "@id": "aas:modelingKind",
      "@type": "@vocab",
      "@context": {
        "Instance": { "@id": "aas:ModellingKind_Instance" },
        "Template": { "@id": "aas:ModellingKind_Template" }
      }
    },
    "qualifier": {
      "@id": "aas:qualifier",
      "@container": "@set",
      "@type": "@id"
    },
    "qualifierKind": {
      "@id": "aas:qualifierKind",
      "@type": "@vocab",
      "@context": {
        "ConceptQualifier": { "@id": "aas:QualifierKind_ConceptQualifier" },
        "TemplateQualifier": { "@id": "aas:QualifierKind_TemplateQualifier" },
        "ValueQualifier": { "@id": "aas:QualifierKind_ValueQualifier" }
      }
    },
    "qualifierType": {
      "@id": "aas:qualifierType"
    },
    "value": {
      "@id": "aas:value"
    },
    "valueId": {
      "@id": "aas:valueId",
      "@type": "@id"
    },
    "valueType": {
      "@id": "aas:valueType",
      "@type": "@id"
    },
    "referenceType": {
      "@id": "aas:referenceType",
      "@type": "@vocab",
      "@context": {
        "ExternalReference": { "@id": "aas:ReferenceType_ExternalReference" },
        "ModelReference": { "@id": "aas:ReferenceType_ModelReference" }
      }
    },
    "referredSemanticId": {
      "@id": "aas:referredSemanticId",
      "@type": "@id"
    },
    "key": {
      "@id": "aas:key",
      "@container": "@list"
    },
    "keyType": {
      "@id": "aas:keyType",
      "@type": "@vocab",
      "@context": {
        "AnnotatedRelationshipElement": { "@id": "aas:KeyType_AnnotatedRelationshipElement" },
        "AssetAdministrationShell": { "@id": "aas:KeyType_AssetAdministrationShell" },
        "BasicEventElement": { "@id": "aas:KeyType_BasicEventElement" },
        "Blob": { "@id": "aas:KeyType_Blob" },
        "Capability": { "@id": "aas:KeyType_Capability" },
        "ConceptDescription": { "@id": "aas:KeyType_ConceptDescription" },
        "DataElement": { "@id": "aas:KeyType_DataElement" },
        "Entity": { "@id": "aas:KeyType_Entity" },
        "EventElement": { "@id": "aas:KeyType_EventElement" },
        "File": { "@id": "aas:KeyType_File" },
        "FragmentReference": { "@id": "aas:KeyType_FragmentReference" },
        "GlobalReference": { "@id": "aas:KeyType_GlobalReference" },
        "Identifiable": { "@id": "aas:KeyType_Identifiable" },
        "MultiLanguageProperty": { "@id": "aas:KeyType_MultiLanguageProperty" },
        "Operation": { "@id": "aas:KeyType_Operation" },
        "Property": { "@id": "aas:KeyType_Property" },
        "Range": { "@id": "aas:KeyType_Range" },
        "Referable": { "@id": "aas:KeyType_Referable" },
        "ReferenceElement": { "@id": "aas:KeyType_ReferenceElement" },
        "RelationshipElement": { "@id": "aas:KeyType_RelationshipElement" },
        "Submodel": { "@id": "aas:KeyType_Submodel" },
        "SubmodelElement": { "@id": "aas:KeyType_SubmodelElement" },
        "SubmodelElementCollection": { "@id": "aas:KeyType_SubmodelElementCollection" },
        "SubmodelElementList": { "@id": "aas:KeyType_SubmodelElementList" }
      }
    },
    "assetInformation": {
      "@id": "aas:assetInformation",
      "@type": "@id"
    },
    "derivedFrom": {
      "@id": "aas:derivedFrom",
      "@type": "@id"
    },
    "submodelReference": {
      "@id": "aas:submodelReference",
      "@container": "@set",
      "@type": "@id"
    },
    "assetKind": {
      "@id": "aas:assetKind",
      "@type": "@vocab",
      "@context": {
        "Instance": { "@id": "aas:AssetKind_Instance" },
        "NotApplicable": { "@id": "aas:AssetKind_NotApplicable" },
        "Type": { "@id": "aas:AssetKind_Type" },
        "Role": { "@id": "aas:AssetKind_Role" }
      }
    },
    "assetType": {
      "@id": "aas:assetType"
    },
    "globalAssetId": {
      "@id": "aas:globalAssetId"
    },
    "specificAssetId": {
      "@id": "aas:specificAssetId",
      "@container": "@set",
      "@type": "@id"
    },
    "defaultThumbnail": {
      "@id": "aas:defaultThumbnail",
      "@type": "@id"
    },
    "name": {
      "@id": "aas:name"
    },
    "externalSubjectId": {
      "@id": "aas:externalSubjectId",
      "@type": "@id"
    },
    "contentType": {
      "@id": "aas:contentType"
    },
    "path": {
      "@id": "aas:path"
    },
    "submodelElement": {
      "@id": "aas:submodelElement",
      "@container": "@set",
      "@type": "@id"
    },
    "first": {
      "@id": "aas:first",
      "@type": "@id"
    },
    "second": {
      "@id": "aas:second",
      "@type": "@id"
    },
    "orderRelevant": {
      "@id": "aas:orderRelevant"
    },
    "semanticIdListElement": {
      "@id": "aas:semanticIdListElement",
      "@type": "@id"
    },
    "typeValueListElement": {
      "@id": "aas:typeValueListElement",
      "@type": "@vocab",
      "@context": {
        "AnnotatedRelationshipElement": { "@id": "aas:AnnotatedRelationshipElement" },
        "BasicEventElement": { "@id": "aas:BasicEventElement" },
        "Blob": { "@id": "aas:Blob" },
        "Capability": { "@id": "aas:Capability" },
        "DataElement": { "@id": "aas:DataElement" },
        "Entity": { "@id": "aas:Entity" },
        "EventElement": { "@id": "aas:EventElement" },
        "File": { "@id": "aas:File" },
        "MultiLanguageProperty": { "@id": "aas:MultiLanguageProperty" },
        "Operation": { "@id": "aas:Operation" },
        "Property": { "@id": "aas:Property" },
        "Range": { "@id": "aas:Range" },
        "ReferenceElement": { "@id": "aas:ReferenceElement" },
        "RelationshipElement": { "@id": "aas:RelationshipElement" },
        "SubmodelElement": { "@id": "aas:SubmodelElement" },
        "SubmodelElementCollection": { "@id": "aas:SubmodelElementCollection" },
        "SubmodelElementList": { "@id": "aas:SubmodelElementList" }
      }
    },
    "annotation": {
      "@id": "aas:annotation",
      "@container": "@set",
      "@type": "@id"
    },
    "statement": {
      "@id": "aas:statement",
      "@container": "@set",
      "@type": "@id"
    },
    "entityType": {
      "@id": "aas:entityType",
      "@type": "@vocab",
      "@context": {
        "CoManagedEntity": { "@id": "aas:EntityType_CoManagedEntity" },
        "SelfManagedEntity": { "@id": "aas:EntityType_SelfManagedEntity" }
      }
    },
    "source": {
      "@id": "aas:source",
      "@type": "@id"
    },
    "sourceSemanticId": {
      "@id": "aas:sourceSemanticId",
      "@type": "@id"
    },
    "observableReference": {
      "@id": "aas:observableReference",
      "@type": "@id"
    },
    "observableSemanticId": {
      "@id": "aas:observableSemanticId",
      "@type": "@id"
    },
    "topic": {
      "@id": "aas:topic"
    },
    "subjectId": {
      "@id": "aas:subjectId",
      "@type": "@id"
    },
    "timeStamp": {
      "@id": "aas:timeStamp"
    },
    "payload": {
      "@id": "aas:payload",
      "@type": "xsd:base64Binary"
    },
    "observed": {
      "@id": "aas:observed",
      "@type": "@id"
    },
    "direction": {
      "@id": "aas:direction",
      "@type": "@vocab",
      "@context": {
        "Input": { "@id": "aas:Direction_Input" },
        "Output": { "@id": "aas:Direction_Output" }
      }
    },
    "state": {
      "@id": "aas:state",
      "@type": "@vocab",
      "@context": {
        "On": { "@id": "aas:StateOfEvent_On" },
        "Off": { "@id": "aas:StateOfEvent_Off" }
      }
    },
    "messageTopic": {
      "@id": "aas:messageTopic"
    },
    "messageBroker": {
      "@id": "aas:messageBroker",
      "@type": "@id"
    },
    "lastUpdate": {
      "@id": "aas:lastUpdate"
    },
    "minInterval": {
      "@id": "aas:minInterval"
    },
    "maxInterval": {
      "@id": "aas:maxInterval"
    },
    "inputVariable": {
      "@id": "aas:inputVariable",
      "@container": "@set",
      "@type": "@id"
    },
    "outputVariable": {
      "@id": "aas:outputVariable",
      "@container": "@set",
      "@type": "@id"
    },
    "inoutputVariable": {
      "@id": "aas:inoutputVariable",
      "@container": "@set",
      "@type": "@id"
    },
    "isCaseOf": {
      "@id": "aas:isCaseOf",
      "@container": "@set",
      "@type": "@id"
    },
    "assetAdministrationShell": {
      "@id": "aas:assetAdministrationShell",
      "@container": "@set",
      "@type": "@id"
    },
    "conceptDescription": {
      "@id": "aas:conceptDescription",
      "@container": "@set",
      "@type": "@id"
    },
    "submodel": {
      "@id": "aas:submodel",
      "@container": "@set",
      "@type": "@id"
    },
    "dataSpecification": {
      "@id": "aas:dataSpecification",
      "@type": "@id"
    },
    "dataSpecificationContent": {
      "@id": "aas:dataSpecificationContent",
      "@type": "@id"
    },
    "min": {
      "@id": "aas:min"
    },
    "max": {
      "@id": "aas:max"
    },
    "dataType": {
      "@id": "iec61360:dataType",
      "@type": "@vocab",
      "@context": {
        "Blob": { "@id": "iec61360:DataTypeIec61360_Blob" },
        "Boolean": { "@id": "iec61360:DataTypeIec61360_Boolean" },
        "Date": { "@id": "iec61360:DataTypeIec61360_Date" },
        "File": { "@id": "iec61360:DataTypeIec61360_File" },
        "Html": { "@id": "iec61360:DataTypeIec61360_Html" },
        "IntegerCount": { "@id": "iec61360:DataTypeIec61360_IntegerCount" },
        "IntegerCurrency": { "@id": "iec61360:DataTypeIec61360_IntegerCurrency" },
        "IntegerMeasure": { "@id": "iec61360:DataTypeIec61360_IntegerMeasure" },
        "Irdi": { "@id": "iec61360:DataTypeIec61360_Irdi" },
        "Iri": { "@id": "iec61360:DataTypeIec61360_Iri" },
        "Rational": { "@id": "iec61360:DataTypeIec61360_Rational" },
        "RationalMeasure": { "@id": "iec61360:DataTypeIec61360_RationalMeasure" },
        "RealCount": { "@id": "iec61360:DataTypeIec61360_RealCount" },
        "RealCurrency": { "@id": "iec61360:DataTypeIec61360_RealCurrency" },
        "RealMeasure": { "@id": "iec61360:DataTypeIec61360_RealMeasure" },
        "String": { "@id": "iec61360:DataTypeIec61360_String" },
        "StringTranslatable": { "@id": "iec61360:DataTypeIec61360_StringTranslatable" },
        "Time": { "@id": "iec61360:DataTypeIec61360_Time" },
        "Timestamp": { "@id": "iec61360:DataTypeIec61360_Timestamp" }
      }
    },
    "preferredName": {
      "@id": "iec61360:preferredName",
      "@container": "@language"
    },
    "shortName": {
      "@id": "iec61360:shortName",
      "@container": "@language"
    },
    "unit": {
      "@id": "iec61360:unit"
    },
    "unitId": {
      "@id": "iec61360:unitId",
      "@type": "@id"
    },
    "sourceOfDefinition": {
      "@id": "iec61360:sourceOfDefinition"
    },
    "symbol": {
      "@id": "iec61360:symbol"
    },
    "definition": {
      "@id": "iec61360:definition",
      "@container": "@language"
    },
    "valueFormat": {
      "@id": "iec61360:valueFormat"
    },
    "valueList": {
      "@id": "iec61360:valueList",
      "@type": "@id"
    },
    "levelType": {
      "@id": "iec61360:levelType",
      "@type": "@id",
      "@context": {
        "min": { "@id": "iec61360:min" },
        "max": { "@id": "iec61360:max" },
        "nom": { "@id": "iec61360:nom" },
        "typ": { "@id": "iec61360:typ" }
      }
    },
    "valueReferencePair": {
      "@id": "iec61360:valueReferencePair",
      "@container": "@set",
      "@type": "@id",
      "@context": {
        "value": { "@id": "aas:value" },
        "valueId": { "@id": "aas:valueId", "@type": "@id" }
      }
    },
    "iec61360Value": {
      "@id": "iec61360:value"
    }
  }
}

    """

    AAS_4 = Namespace(
        "https://admin-shell.io/aas/4/")  # this is an example how future releases namespace would look like
    AAS_ONTOLOGY_4 = """"""
    AAS_SHACL_4 = """"""
