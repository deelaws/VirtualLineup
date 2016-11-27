from enum import Enum

'''
There can be many different types of line in a store.
'''
class VirtualLineType(Enum):
    Cashier = 1
    ChangeRoom = 2
    CustomerService = 3

def vlinetype_enum_to_string(line_type):
    return line_type.name