#!/usr/bin/env python

"""Tests for `py_aas_rdf` package."""
from py_aas_rdf.models import make_uri, is_irdi
from py_aas_rdf.models.data_specification_iec_61360 import ValueList, ValueReferencePair, DataSpecificationIec61360
from py_aas_rdf.models.environment import Environment
from py_aas_rdf.models.key import Key
from py_aas_rdf.models.multi_language_property import MultiLanguageProperty
from py_aas_rdf.models.property import Property
from py_aas_rdf.models.submodel import Submodel


def test_key_to_rdf():
    payload = Key(**{"type": "AssetAdministrationShell", "value": "example"})
    graph, created_node = payload.to_rdf()
    re_created = Key.from_rdf(graph, created_node)
    assert payload == re_created


def test_value_reference_to_rdf():
    payload = ValueReferencePair(**{
        "value": "something_63781b6f",
        "valueId": {
            "keys": [
                {
                    "type": "GlobalReference",
                    "value": "urn:yet-another-company15:6b346267"
                }
            ],
            "type": "ExternalReference"
        }
    })
    graph, created_node = payload.to_rdf()
    re_created = ValueReferencePair.from_rdf(graph, created_node)
    assert payload == re_created


def test_value_mlp_to_rdf():
    payload = MultiLanguageProperty(**{
        "idShort": "mlp",
        "modelType": "MultiLanguageProperty",
        "description": [
            {
                "language": "es-419",
                "text": "something_be9deae0"
            }
        ],
        "displayName": [
            {
                "language": "zh-CN-a-myext-x-private",
                "text": "something_535aeb51"
            }
        ],
        "value": [
            {
                "language": "en",
                "text": "something_cd7e6587"
            },
            {
                "language": "de",
                "text": "something_cd7e6587"
            }
        ],
    })
    graph, created_node = payload.to_rdf()
    print(graph.serialize(format='turtle'))
    re_created = MultiLanguageProperty.from_rdf(graph, created_node)
    assert payload == re_created


def test_value_list_to_rdf():
    payload = ValueList(**{
        "valueReferencePairs": [
            {
                "value": "something_63781b6f",
                "valueId": {
                    "keys": [
                        {
                            "type": "GlobalReference",
                            "value": "urn:yet-another-company15:6b346267"
                        }
                    ],
                    "type": "ExternalReference"
                }
            }
        ]
    })
    graph, created_node = payload.to_rdf()
    re_created = ValueList.from_rdf(graph, created_node)
    assert payload == re_created


def test_dataspec_to_rdf():
    payload = DataSpecificationIec61360(**{
        "dataType": "DATE",
        "definition": [
            {
                "language": "de-Qaaa",
                "text": "something_2ae95f9f"
            }
        ],
        "levelType": {
            "max": True,
            "min": True,
            "nom": True,
            "typ": True
        },
        "modelType": "DataSpecificationIec61360",
        "preferredName": [
            {
                "language": "i-enochian",
                "text": "something_84b0b440"
            },
            {
                "language": "en-GB",
                "text": "Something random in English 5b15c20d"
            }
        ],
        "shortName": [
            {
                "language": "x-whatever",
                "text": "something_65af8271"
            }
        ],
        "sourceOfDefinition": "something_1bd907c8",
        "symbol": "something_c13116d7",
        "unit": "something_a6bd9450",
        "unitId": {
            "keys": [
                {
                    "type": "Submodel",
                    "value": "urn:an-example01:69d96aad"
                }
            ],
            "type": "ModelReference"
        },
        "value": "something_13759f45",
        "valueFormat": "something_f019e5a8"
    })
    graph, created_node = payload.to_rdf()
    print(graph.serialize(format='turtle'))

    re_created = DataSpecificationIec61360.from_rdf(graph, created_node)
    assert payload == re_created


def test_property_to_rdf():
    payloads = [
        {
            "idShort": "PropertyWithConceptDescription",
            "modelType": "Property",
            "value": "12.0",
            "valueType": "xs:double",
            "semanticId": {
                "keys": [
                    {
                        "type": "ConceptDescription",
                        "value": "something_8ccad77f"
                    }
                ],
                "type": "ModelReference"
            }
        },
        {
            "idShort": "PropertyWithECLASSSemantic",
            "modelType": "Property",
            "value": "Test",
            "valueType": "xs:string",
            "semanticId": {
                "keys": [
                    {
                        "type": "GlobalReference",
                        "value": "0173-1#02-AAO677#004"
                    }
                ],
                "type": "ExternalReference"
            }
        },
        {
            "idShort": "PropertyWithIECCDDSemantic",
            "modelType": "Property",
            "value": "Test",
            "valueType": "xs:string",
            "semanticId": {
                "keys": [
                    {
                        "type": "GlobalReference",
                        "value": "0112/2///61360_4#AAD001#002"
                    }
                ],
                "type": "ExternalReference"
            }
        },
        {
            "idShort": "something3fdd3eb4",
            "modelType": "Property",
            "value": "12.013",
            "valueType": "xs:double"
        }
    ]
    for payload in payloads:
        payload = Property(**payload)
        graph, created_node = payload.to_rdf()
        print(graph.serialize(format='turtle'))
        re_created = Property.from_rdf(graph, created_node)
        assert payload == re_created


def test_env_to_rdf():
    payload = Environment(**{
        "assetAdministrationShells": [
            {
                "assetInformation": {
                    "assetKind": "NotApplicable",
                    "globalAssetId": "something_eea66fa1"
                },
                "submodels": [
                    {
                        "keys": [
                            {
                                "type": "Submodel",
                                "value": "something_48c66017"
                            }
                        ],
                        "type": "ModelReference"
                    }
                ],
                "id": "something_142922d6",
                "modelType": "AssetAdministrationShell"
            }
        ],
        "submodels": [
            {
                "submodelElements": [
                    {
                        "idShort": "PropertyWithConceptDescription",
                        "modelType": "Property",
                        "value": "12.0",
                        "valueType": "xs:double",
                        "semanticId": {
                            "keys": [
                                {
                                    "type": "ConceptDescription",
                                    "value": "something_8ccad77f"
                                }
                            ],
                            "type": "ModelReference"
                        }
                    },
                    {
                        "idShort": "PropertyWithECLASSSemantic",
                        "modelType": "Property",
                        "value": "Test",
                        "valueType": "xs:string",
                        "semanticId": {
                            "keys": [
                                {
                                    "type": "GlobalReference",
                                    "value": "0173-1#02-AAO677#004"
                                }
                            ],
                            "type": "ExternalReference"
                        }
                    },
                    {
                        "idShort": "PropertyWithIECCDDSemantic",
                        "modelType": "Property",
                        "value": "Test",
                        "valueType": "xs:string",
                        "semanticId": {
                            "keys": [
                                {
                                    "type": "GlobalReference",
                                    "value": "0112/2///61360_4#AAD001#002"
                                }
                            ],
                            "type": "ExternalReference"
                        }
                    }
                ],
                "id": "something_48c66017",
                "modelType": "Submodel"
            }
        ],
        "conceptDescriptions": [
            {
                "id": "something_8ccad77f",
                "modelType": "ConceptDescription"
            }
        ]
    })

    graph, created_node = payload.to_rdf()
    print(graph.serialize(format='turtle'))
    re_created = Environment.from_rdf(graph, created_node)
    assert payload == re_created


def test_irdi():
    assert is_irdi("0173-1#02-AAA123#001") == True
    assert is_irdi("0112-1-a-18582#KAA802#s") == True
    assert is_irdi("0112/2///61360_4#AAD001") == True


def test_iri():
    assert str(make_uri("http://example.com/aas1")) == "http://example.com/aas1"
    assert str(make_uri("0173-1#02-AAA123#001")) == "urn:irdi:0173_1__02_AAA123__001"


def test_complex_env_to_rdf():
    payload = Environment(**{
        "assetAdministrationShells": [
            {
                "assetInformation": {
                    "assetKind": "NotApplicable",
                    "globalAssetId": "something_eea66fa1"
                },
                "submodels": [
                    {
                        "keys": [
                            {
                                "type": "Submodel",
                                "value": "something_48c66017"
                            }
                        ],
                        "type": "ModelReference"
                    },
                    {
                        "keys": [
                            {
                                "type": "Submodel",
                                "value": "https://aas.metaphacts.cloud/submodels/source"
                            }
                        ],
                        "type": "ModelReference"
                    },
                    {
                        "keys": [
                            {
                                "type": "Submodel",
                                "value": "https://aas.metaphacts.cloud/submodels/target"
                            }
                        ],
                        "type": "ModelReference"
                    }
                ],
                "id": "something_142922d6",
                "modelType": "AssetAdministrationShell"
            }
        ],
        "submodels": [
            {
                "submodelElements": [
                    {
                        "idShort": "PropertyWithConceptDescription",
                        "modelType": "Property",
                        "value": "12.0",
                        "valueType": "xs:double",
                        "semanticId": {
                            "keys": [
                                {
                                    "type": "ConceptDescription",
                                    "value": "something_8ccad77f"
                                }
                            ],
                            "type": "ModelReference"
                        }
                    },
                    {
                        "idShort": "PropertyWithECLASSSemantic",
                        "modelType": "Property",
                        "value": "Test",
                        "valueType": "xs:string",
                        "semanticId": {
                            "keys": [
                                {
                                    "type": "GlobalReference",
                                    "value": "0173-1#02-AAO677#004"
                                }
                            ],
                            "type": "ExternalReference"
                        }
                    },
                    {
                        "idShort": "PropertyWithIECCDDSemantic",
                        "modelType": "Property",
                        "value": "Test",
                        "valueType": "xs:string",
                        "semanticId": {
                            "keys": [
                                {
                                    "type": "GlobalReference",
                                    "value": "0112/2///61360_4#AAD001#002"
                                }
                            ],
                            "type": "ExternalReference"
                        }
                    }
                ],
                "id": "something_48c66017",
                "modelType": "Submodel"
            },
            {
                "idShort": "Inventory",
                "id": "https://aas.metaphacts.cloud/submodels/source",
                "kind": "Instance",
                "submodelElements": [
                    {
                        "idShort": "ReferenceToManufacturerProperty",
                        "value": {
                            "type": "ModelReference",
                            "keys": [
                                {
                                    "type": "Submodel",
                                    "value": " https://aas.metaphacts.com/submodels/target"
                                },
                                {
                                    "type": "Property",
                                    "value": "Manufacturer"
                                }
                            ]
                        },
                        "modelType": "ReferenceElement"
                    }
                ],
                "modelType": "Submodel"
            },
            {
                "idShort": "ProductInformation",
                "id": "https://aas.metaphacts.cloud/submodels/target",
                "kind": "Instance",
                "submodelElements": [
                    {
                        "idShort": "Manufacturer",
                        "valueType": "xs:string",
                        "value": "metaphacts",
                        "modelType": "Property"
                    }
                ],
                "modelType": "Submodel"
            }
        ],
        "conceptDescriptions": [
            {
                "id": "something_8ccad77f",
                "modelType": "ConceptDescription"
            }
        ]
    })

    graph, created_node = payload.to_rdf()
    print(graph.serialize(format='turtle'))
    re_created = Environment.from_rdf(graph, created_node)
    assert payload == re_created
