from os import name
from database import ability_list, type_list, dex
from Pokemon_Decorator import *

def type_check(func):
    def wrapper(self, type1:str = 'N/A'):
        try:
            # Check if the type is in the type list
            if type1 in type_list:
                func(self, type1)
        except TypeError as te:
            print(te)
            print(f"{type1} is not a valid type")
    return wrapper

def ability_check(func):
    def wrapper(self, ability:str):
        # Check if the ability is in the ability list
        try:
            if ability in ability_list:
                func(self, ability)
        except ValueError as te:
            print(te)
            return ability
    return wrapper

class Pokemon():    
    def __init__(self, name:str='N/A', number : int = 0, type1:str='D', type2:str='N/A',
                 ability:str='N/A', ability2:str='N/A', h_ability:str='N/A'):
        self._name = name.capitalize()
        self._number = int(number)
        self._ability = ability.capitalize()
        self._type1 = self.setType1(type1.upper())
        self._type2 = type2.upper()
        self._ability2 = ability2
        self._h_ability = h_ability
        
    def __str__(self) -> str:
        statement = ("name: " + self.getName() + "\n" + 
                     "number: " + str(self.getNumber()) + "\n" + 
                     "type1: " + self._type1 + "\n" +  
                     "type2: " + self._type2 + "\n" + 
                     "ability: " + self._ability + "\n" + 
                     "ability2: " + self._ability2 + "\n" + 
                     "h_ability: " + self._h_ability)

        return statement
        
    def setName(self, name:str):
        try:
            self._name = name.capitalize()
        except AttributeError as ae:
            print(ae)
        
    
    def getName(self) -> str:
        return self._name
        
    def setNumber(self, number:int):
        if number in dex:
            self._number = number
    
    def getNumber(self) -> int:
        return self._number
    
    @type_check
    def setType1(self, type1:str ='N/A'):
        return type1
    
    def getType1(self) -> str:
        return self._type1  

    @type_check
    def setType2(self, type2:str) -> str:
        if type2 == self._type1:
            raise ValueError(f"{type2} is the same as type 1")
        return type2
    
    def getType2(self) -> str:
        return self._type2
    
    @ability_check
    def setAbility(self, ability:str):
        return ability
    
    def getAbility(self) -> str:
        return self._ability



    
    
        
            
if __name__ == '__main__':
    p = Pokemon('Jason',25, 'D', 'D', 'D', 'Blaze', 'Surge Surfer')
    print(p)
        
        
