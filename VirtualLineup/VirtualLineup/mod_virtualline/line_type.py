from enum import Enum

'''
There can be many different types of line in a store.
'''
class LineType(Enum):
    Cashier = 1
    ChangeRoom = 2
    CustomerService = 3