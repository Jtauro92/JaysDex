from database import dex
from pokemon_decorator import name_check, type_check, ability_check

class Pokemon():
    DEFAULT_VALUE = 'N/A'
    def __init__(self, name:str= DEFAULT_VALUE, number : int = 0, 
                 type1:str= DEFAULT_VALUE, type2:str= DEFAULT_VALUE, 
                 ability:str= DEFAULT_VALUE, ability2:str= DEFAULT_VALUE, 
                 h_ability:str= DEFAULT_VALUE):
        self._name = name
        self._number = number
        self._type1 = type1
        self._type2 = type2
        self._ability = ability
        self._ability2 = ability2
        self._h_ability = h_ability
        
    def __str__(self) -> str:
        statement = ("name: " + self.name + "\n" 
                     + "number: " + str(self.number) + "\n"  
                     + "type1: " + (self.type1) + "\n"   
                     + "type2: " + (self._type2) + "\n" 
                     + "ability: " + (self._ability) + "\n" 
                     + "ability2: " + (self._ability2) + "\n"
                     + "h_ability: " + (self._h_ability) + "\n")

        return statement
    
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    @name_check
    def name(self, name:str):
        if (any(pokemon["Name"] == name for pokemon in dex)):
            self._name = name
    
    @property
    def number(self) -> int:
        return self._number
    
    @number.setter
    def number(self, number:int):
        if (any(pokemon["Number"] == number for pokemon in dex)):
            self._number = number

    @property
    def type1(self) -> str:
        return self._type1
    
    @type1.setter
    @type_check
    def type1(self, type1:str):
        self._type1 = type1
    
    @property
    def type2(self) -> str:
        return self._type2
    
    @type2.setter
    @type_check
    def type2(self, type2:str):
        if (type2 != self._type1):
            self._type2 = type2
            
    @property
    def ability(self) -> str:
        return self._ability
    
    @ability.setter
    @ability_check
    def ability(self, ability:str):
        self._ability = ability
    
    @property
    def ability2(self) -> str:
        return self._ability2
    
    @ability2.setter
    @ability_check
    def ability2(self, ability2:str):
        if ability2 not in {self._ability, self._h_ability}:
            self._ability2 = ability2

    @property
    def h_ability(self) -> str:
        return self._h_ability
    
    @h_ability.setter
    @ability_check
    def h_ability(self, h_ability:str):
        if h_ability not in {self._ability, self._ability2}:
            self._h_ability = h_ability

            
if __name__ == '__main__':
    p = Pokemon()
    p.type1 = "fire"
    p.type2 = "fire"
    p.ability = 'overgrow'
    p.ability2 = 'overgrow'
    p.h_ability = 'overgrow'
    p.number = 6000
    p.name = 'Jason'
    
    print((p))
        
        
