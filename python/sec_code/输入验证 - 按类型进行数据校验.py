# pip install cerberus
from cerberus import Validator

v = Validator({"name":{"type":"string"}})
v.validate({"name":"python string"})