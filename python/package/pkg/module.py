# __all__ affects the from <module> import * behavior only
__all__ = ['add']

def add(a, b):
    return a + b

def sub(a, b):
    return a - b