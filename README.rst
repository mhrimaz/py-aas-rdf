==========
py-aas-rdf
==========


.. image:: https://img.shields.io/pypi/v/py_aas_rdf.svg
        :target: https://pypi.python.org/pypi/py_aas_rdf

.. image:: https://img.shields.io/travis/mhrimaz/py_aas_rdf.svg
        :target: https://travis-ci.com/mhrimaz/py_aas_rdf

.. image:: https://readthedocs.org/projects/py-aas-rdf/badge/?version=latest
        :target: https://py-aas-rdf.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status




Utility library to de-/serialize AAS in RDF and JSON.

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

