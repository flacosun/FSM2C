'''
Created on May 16, 2014

@author: flaco
'''
import json


class jsonParser(object):
    '''
    classdocs
    '''
    

    def __init__(self, jsonFilePath, cPath):
        '''
        Todo exception handling
        '''
        try:
            jsonInput = open(jsonFilePath, "r")
        except IOError:
            print("Failed to open json file.\n")
        data = json.load(jsonInput)
        self.period = data["attributes"]["period"]
        self.initialState = data["attributes"]["start"]
        self.variables = data["attributes"]["variables"]
        self.states = data["states"]
        self.cPath = cPath
    
    def printToC(self):
        try:
            outFile = open(self.cPath, "w")
        except IOError:
            print("Failed to create C file\n")
        print("Start generating C file\n")
        outFile.write(
                      '''
#include "RIMS.h"
volatile unsigned char TimerFlag = 0;
void TimerISR() {
    TimerFlag = 1;
}
                      '''
        )
        outFile.close()
        
        
        
        