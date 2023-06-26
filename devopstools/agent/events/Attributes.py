'''
Created on 25-Jun-2022

@author: srikari.rallabandi
'''

import json
from datetime import datetime;

class Action(object):
    '''
    classdocs
    This class represents the action that is performed
    '''

    def __init__(self,eventType,eventSource,createdBy,timestamp,payloadType,user):
        self.eventType = eventType,
        self.eventSource = eventSource,
        self.createdBy = createdBy,
        self.timestamp = datetime.now(),
        self.payloadType = payloadType,
        self.user = user




