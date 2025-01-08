from database import ability_list, type_list, dex

class Pokemon:
    def __init__(self,name: str, number: int, type: str, 
                 type2: str, ability: str, ability2: str, h_ability: str,
                 stage: int =0, hp: int=0, atk: int=0, defn: int=0,
                 sp_atk: int=0, sp_def: int=0, speed: int=0):
        
        self.name = name.title() if self.name_is_valid(name) else 'Default'
        self.number = int(number) if self.number_is_valid(number) else 0
        self.type1 = type.upper() if self.type_is_valid(type) else None
        self.type2 = type2.upper() if self.type2_is_valid(type2) else None
        self.ability = ability.title() if self.ability_is_valid else None
        self.ability2 = ability2.title() if self.ability_is_valid(ability2) else None
        self.h_ability =  h_ability.title() if self.ability_is_valid(h_ability) else None 
        if not (self.ability_is_unique(ability2)):
            self.ability2 = None
        self.h_ability =  h_ability.title() if self.ability_is_valid(h_ability) else None 
        if not (self.ability_is_unique(h_ability)):
            self.h_ability = None
        self.stage = int(stage) if 0 < int(stage) < 4 else 1
        
        self.hp = hp
        self.atk = atk
        self.defn = defn
        self.sp_atk = sp_atk
        self.sp_def = sp_def
        self.speed = speed
        
    def name_is_valid(self,name: str) -> bool:
        try:
            if name and (name.isalpha() is True):
                return True
        except AttributeError as e:
            print('Invalid name')
        return False
    
    def number_is_valid(self,number: int) -> bool:
        try:
            if number and (isinstance(number,int) is True):
                return True
        except AttributeError as e:
            print('Invalid number')
        return False
    
    def type_is_valid(self,type: str) -> bool:
        try:
            if type.upper() in type_list:
                return True
        except AttributeError as e:
            print('Invalid type')
        return False
    
    def type2_is_valid(self,type2: str) -> bool:

        if self.type_is_valid(type2) and type2.upper() != self.type1:
            return True
        return False
        
    def ability_is_valid(self, ability: str) -> bool:
        try:
            if ability.title() in ability_list:
                return True
        except AttributeError:
            print('Invalid ability')
        return False
    
    def ability_is_unique(self, ability: str) -> bool:
        return len({self.ability, ability, self.h_ability}) == 3 or \
                len({self.ability,self.ability2,ability}) == 3     

    def in_pokedex(self,name=None,number=None):
        if isinstance(name,str):
            return any(pokemon['Name'] == name for pokemon in dex)
        elif isinstance(number,int):
            return any(pokemon['Number'] == number for pokemon in dex)
            
        
    def __str__(self):
        return f"pokemon: {self.name}\n\
number: {self.number}\n\
type1: {self.type1}\n\
type2: {self.type2}\n\
ability: {self.ability}\n\
ability2: {self.ability2}\n\
hidden ability: {self.h_ability}\n\
stage: {self.stage}\n\
hp: {self.hp}\n\
atk: {self.atk}\n\
def: {self.defn}\n\
sp_atk: {self.sp_atk}\n\
sp_def: {self.sp_def}\n\
speed: {self.speed}\n"             

if __name__ == '__main__':
    Testmon = Pokemon(name = 'scovillan',
                      number=25,
                      type='fire',
                      type2='grass',
                      ability="drought",
                      ability2="solar power",
                      h_ability="drought",)
    print (Testmon)
