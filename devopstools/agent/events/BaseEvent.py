'''
Created on 12-Aug-2022

@author: narayana.rallabandi
'''
import json
from devops.core.utils import SchemaValidators

class BaseEvent(object):
    '''
    classdocs
    This class represents the base event
    It contains the attributes and a payload object
    The attributes section will talk about the payload type or
    its the metadata about the payload
    '''

    def __init__(self, attributes, payload):
        '''
        Constructor
        '''
        if type(attributes) is not dict:
            raise SyntaxError("Attribute Section must be a Dictionary")
        self.attributes = attributes
        self.payload = payload

    def validateAttribute(self):
        attributes = json.loads(self.attributes)
        sv = SchemaValidators.validateSchema(attributes,"EventAttributeSchema")

def main():
    baseEvent = BaseEvent([], {})
    print(baseEvent)


if __name__ == "__main__":
    main()