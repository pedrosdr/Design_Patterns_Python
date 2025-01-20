from __future__ import annotations
from typing import List
from copy import deepcopy


class StringReprMixin:
    def __str__(self):
        params = [f"{k}={v}" for k, v in self.__dict__.items()]
        return f"{self.__class__.__name__}({', '.join(params)})"

    def __repr__(self):
        return self.__str__()
    

class Cloneable:
    def clone(self):
        return deepcopy(self)


class Person(StringReprMixin, Cloneable):
    def __init__(
            self, 
            firstname:str=None, 
            lastname:str=None
    ) -> None:
        self.firstname:str = firstname
        self.lastname:str = lastname
        self.addresses: List[Address] = []

    def add_address(self, address:Address) -> None:
        self.addresses.append(address)
    

class Address(StringReprMixin, Cloneable):
    def __init__(
            self, 
            street:str=None, 
            number:str=None
    ) -> None:
        self.street:str = street
        self.number:str = number
    

if __name__ == "__main__":
    luiz = Person('Luiz', 'Miranda')
    address_luiz = Address('Av. Brasil', '250A')
    luiz.add_address(address_luiz)

    esposa_luiz = luiz.clone()
    esposa_luiz.firstname = 'Letícia'

    print(luiz)
    print(esposa_luiz)

