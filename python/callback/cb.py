'''
Callback
    - is a function
    - as a argument
'''

def get_value(param, data):
    param(data)

def call_back(value):
    print("Value is:", value)

get_value(call_back, 123)