'''
Created on 12-Aug-2022

@author: narayana.rallabandi
'''
import enum


@enum.unique
class ActionType(enum.Enum):
    '''
    classdocs
    '''
    MESSAGING = 1
    SERVER = 2
    AGENT = 3
    ACCOUNT = 4
    USER = 5

    def __init__(self, params):
        '''
        Constructor
        '''
