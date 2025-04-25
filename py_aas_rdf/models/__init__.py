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
from base64 import urlsafe_b64decode, urlsafe_b64encode
from urllib.parse import quote, unquote
import re
import rdflib
from rdflib import URIRef

IRDI_PATTERN = re.compile(
    r"^\d{4}[a-zA-Z0-9_./-]*#[a-zA-Z0-9_./-]+(?:#[a-zA-Z0-9_./-]+)?$"

)


def is_valid_uri(uri: str) -> bool:
    return uri.startswith(('http://', 'https://', 'urn:'))


def is_irdi(identifier: str) -> bool:
    return bool(IRDI_PATTERN.fullmatch(identifier))


def make_uri(identifier: str, base: str = "") -> str:
    if is_valid_uri(identifier):
        return URIRef(identifier)
    elif is_irdi(identifier):
        return URIRef(f"urn:irdi:{identifier.replace('-', '_').replace('#', '__')}")
    else:
        return URIRef(f"{base}{url_encode(identifier)}")


def base_64_url_encode(data: str) -> str:
    try:
        result = urlsafe_b64encode(data.encode("utf-8")).rstrip(b"=").decode("utf-8")
    except Exception:
        import py_aas_rdf.models.response

        raise py_aas_rdf.models.response.InvalidBase64URLIdentifier()
    return result


def url_encode(data: str) -> str:
    return quote(data, safe="")


def base_64_url_decode(base_64_url: str) -> str:
    try:
        result = urlsafe_b64decode(base_64_url + "=" * (4 - len(base_64_url) % 4)).decode("utf-8")
    except Exception:
        import py_aas_rdf.models.response

        raise py_aas_rdf.models.response.InvalidBase64URLIdentifier()
    return result


def url_decode(url_encoded_data: str) -> str:
    return unquote(url_encoded_data)


rdflib.plugin.register("turtle_custom", rdflib.plugin.Serializer, "py_aas_rdf.models.serializer",
                       "TurtleSerializerCustom")
