''' JavaScript Object Notation '''
''' to load a json file into python, we use json.load method
    to load a json string into python object, we use json.loads method'''

import json

with open('states.json') as f:
    data=json.load(f)

print(type(data))
# to print the states