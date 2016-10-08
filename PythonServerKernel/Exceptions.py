#!/usr/bin/env python3

class Error(Exception):
    pass

class KernerlCriticalFailur(Error):
    def __init__(self, expresion, message):
        self.expression=expresion
        self.message=message


#TODO in alle datein einbauhen
class RunnedFromFalseFile(Error):
    def __init__(self, file):
        self.file = file