import msvcrt as m
from rich.console import Console as console
from database import ability_list, type_list, dex

cprint = console().print
clear_console = console().clear
def clear_line():
    print("\033[A\033[2K", end='', flush=True)
    
def minput():
        m.kbhit()
        return m.getch()

class Pokemon:
    def __init__(self,name='',number=0,type='',type2=None,ability='',ability2=None,h_ability=None,
                 stage=1,hp=0,atk=0,defn=0,sp_atk=0,sp_def=0,speed=0):

        self.name = name.capitalize() if name.strip() and (name == '0' or not name.isnumeric()) else None
        try:
            self.number = int(number) if 0 <= int(number)<= 1025 else None
        except ValueError:
            self.number = None
            
        self.type1 = type.upper() if type.upper() in type_list or type != ''.strip() else None
        self.type2 = type2
        self.ability = ability.title() if ability.strip() and (ability.title() in ability_list or ability.strip()) or ability =='0' else None
        self.ability2 = ability2
        self.h_ability =  h_ability
        self.stage = stage if 0 < stage < 4 else 1
        
        self.hp = hp
        self.atk = atk
        self.defn = defn
        self.sp_atk = sp_atk
        self.sp_def = sp_def
        self.speed = speed

    def in_pokedex(self):
        if isinstance(self.name,str):
            return any(pokemon['Name'] == self.name for pokemon in dex)
        elif isinstance(self.number,int):
            return any(pokemon['Number'] == self.number for pokemon in dex)
        
    def type2_equals_type1(self):
        return self.type1 == self.type2

    def has_same_ability(self):
        return (self.ability == self.ability2) or \
                (self.ability == self.h_ability) or\
                    (self.ability2 == self.h_ability)
           
    def __repr__(self):
        return f"{self.name}"     
        
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
    Testmon = Pokemon('Charizard',
                      number=9, 
                      type="Fire",
                      type2="Flying",
                      ability="blaze",
                      ability2="solar flare",
                      h_ability="Drought",)
    print (Testmon)
