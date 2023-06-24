'''
Created on 12-Aug-2022

@author: narayana.rallabandi
'''
import enum


@enum.unique
class Staus(enum.Enum):
    '''
    classdocs
    '''
    SCHEDULED = 1
    RUNNING = 2
    FINISHED_SUCCESS = 3
    FINISHED_ABORTED = 4
    FINISHED_TERMINATED = 5

    def __init__(self, params):
        '''
        Constructor
        '''
