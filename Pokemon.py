from database import ability_list, type_list, dex
from Pokemon_Decorator import *

class Pokemon(ValidType):
    name = ValidName()
    number = ValidNumber()
    type1 = ValidType()
    type2 = ValidType2()
    ability = ValidAbility()
    ability2 = ValidAbility2()
    h_ability = ValidHiddenAbility()
    
    def __init__(self, name:str='', number : int = 0, ability:str='', type1:str='', type2:str='',
                 ability2:str='', h_ability:str=''):
        self._name = name
        self._number = number
        self.ability = ability
        self.type1 = type1
        self._type2 = type2
        self.ability2 = ability2
        self.h_ability = h_ability
        
    def __str__(self):
        return f"{self.name} {self.number} {self.type1} {self.type2} {self.ability} {self.ability2} {self.h_ability}"
        
            
if __name__ == '__main__':
    p = Pokemon()
    p.name = 'charmander'
    p.number = 56
    p.type1 = 'fire'
    p.type2 = 'fire'
    p.ability = 'blaze'
    p.ability2 = 'blaze'
    p.h_ability = 'drought'
    print(p)
        
        
