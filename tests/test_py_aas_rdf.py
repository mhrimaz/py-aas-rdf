#!/usr/bin/env python

"""Tests for `py_aas_rdf` package."""
from py_aas_rdf.models.data_specification_iec_61360 import ValueList, ValueReferencePair
from py_aas_rdf.models.key import Key


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
