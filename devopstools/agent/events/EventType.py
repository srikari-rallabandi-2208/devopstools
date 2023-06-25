'''
Created on 12-Aug-2022

@author: narayana.rallabandi
'''

import enum


@enum.unique
class EventType(enum.Enum):
    '''
    classdocs
    This class represents the event types that occur in the
    DevOps Ecosystem
    '''

    ACTION = 1
    MESSAGING = 2
    SERVER = 3
    AGENT = 4
    ACCOUNT = 5
    USER = 6

    def __init__(self, params):
        '''
        Constructor
        '''
