'''
Created on May 16, 2014

@author: flaco
'''
import sys
import FSM2C

if __name__ == '__main__':
    interpreter = FSM2C.jsonParser(sys.argv[1],sys.argv[2])
    interpreter.printToC()