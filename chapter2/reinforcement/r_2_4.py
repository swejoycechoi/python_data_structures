'''Write a Python class, Flower, that has three instance variables of type str,
int, and float, that respectively represent the name of the flower, its number
of petals, and its price. Your class must include a constructor method
that initializes each variable to an appropriate value, and your class should
include methods for setting the value of each type, and retrieving the value
of each type'''

# Hint: Consider using get and set methods for accessing and modifying the values

class Flower:

    def __init__(self, name: str, petals: int, price: float):
        '''constructor to initialize the instance variables'''
        self._name = name
        self._petals = petals
        self._price = price
    
    # getter and setter methods for name
    def get_name(self) -> str:
        return self._name
    
    def set_name(self, name: str):
        self._name = name

    # getter and setter methods for petals
    def get_petals(self) -> int:
        return self._petals
    
    def set_petals(self, petals: int):
        self._petals = petals

    # getter and setter methods for price
    def get_price(self) -> float:
        return self._price
    
    def set_price(self, price: float):
        self._price = price
