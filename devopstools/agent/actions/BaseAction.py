'''
Created on 24-Jun-2022

@author: srikari.rallabandi
'''
import json
from devops.core.utils import SchemaValidators

class BaseAction(object):
    '''
    classdocs
    This class represents the action that is performed
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
