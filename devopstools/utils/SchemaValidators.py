'''
Created on 12-Oct-2022

@author: srikari.rallabandi
'''

import os
from pathlib import Path

import jsonschema
from jsonschema import validate
import json


class SchemaValidator(object):

    def __init__(self, params):
        '''
        Constructor
        '''

    def getSchema(self, schemaName):
        '''
        Validate schema
        '''
        parent = Path(__file__).parent.parent
        schemaDir = (parent / 'schemas').resolve()
        print(schemaDir)

        for schema in schemaDir.glob("*.schema"):
            jsonfile = schema.name
            fn = jsonfile[:-7]
            if fn == schemaName:
                js = Path(schemaDir / jsonfile).read_text()
                return json.loads(js)

    def getExamples(self, exampleName):
        parent = Path(__file__).parent.parent
        schemaDir = (parent / 'schemas').resolve()
        print(schemaDir)

        for schema in schemaDir.glob("*.json"):
            jsonfile = schema.name
            fn = jsonfile[:-5]
            if fn == exampleName:
                js = Path(schemaDir / jsonfile).read_text()
                return json.loads(js)

    def validateSchema(self, instance, schemaName):
        schema = self.getSchema(schemaName)
        instance = self.getExamples(instance)
        try:
            print(validate(instance, schema))
        except jsonschema.exceptions.ValidationError as e:
            print("this is validation error:", e)
        except json.decorder.JSONDecodeError as e:
            print("not JSON", e)

    def validateJSON(self, instance, schemaName):
        schema = self.getSchema(schemaName)
        #instance = self.getExamples(instance)
        try:
            print(validate(instance, schema))
        except jsonschema.exceptions.ValidationError as e:
            print("this is validation error:", e)
        except json.decorder.JSONDecodeError as e:
            print("not JSON", e)

def main():
    sv = SchemaValidator({})
    print(sv.getSchema("EventAttributeSchema"))
    print(sv.validateSchema("EventAttributeSchema", "EventAttributeSchema"))


if __name__ == "__main__":
    main()
