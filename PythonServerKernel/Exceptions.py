#!/usr/bin/env python3

class Error(Exception):
    pass

class KernerlCriticalFailur(Error):
    def __init__(self, expresion, message):         #define undifen error
        self.expression=expresion
        self.message=message


#TODO in alle datein einbauhen
class RunnedFromFalseFile(Error):                   #define New Error to raise if someone calling the false file
    def __init__(self, file):
        self.file = file



if __name__ == '__main__':
    raise RunnedFromFalseFile('PythonServerKernel_Exception_py')