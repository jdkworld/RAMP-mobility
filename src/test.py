from parse_yaml import *
from input_class import Inputs


inputs = Inputs('IND', 'industry')

person = 'working'
username = person.capitalize() + " - " + " car"
print(username)

for attr in inputs.__dict__:
        print(f'{attr} -> {getattr(inputs, attr)}')

