#!/usr/bin/env python

"""Tests for `py_aas_rdf` package."""

from py_aas_rdf.models.key import Key


def test_key_to_rdf():
    payload = Key(**{"type": "AssetAdministrationShell", "value": "example"})
    graph, created_node = payload.to_rdf()
    re_created = Key.from_rdf(graph, created_node)
    assert payload == re_created
