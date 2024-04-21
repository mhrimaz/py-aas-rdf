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
