'''
Created on May 16, 2014

@author: flaco
'''
import sys
import cPrinter

def usage():
    print("usage main.py source.json target.c\n")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        usage()
    if sys.argv[1] == None or sys.argv[2] == None:
        usage()
    interpreter = cPrinter.CPrinter(sys.argv[1],sys.argv[2])
    interpreter.process()