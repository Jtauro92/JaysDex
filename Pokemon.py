from math import e
import msvcrt as m
import re
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
    def __init__(self,name='',number=None,type='',type2='',ability='',ability2=None,h_ability=None,
                 stage=1,hp=0,atk=0,defn=0,sp_atk=0,sp_def=0,speed=0):
        
        self.name = name.title() if self.validate_pokemon(name) else None
        self.number = int(number) if self.validate_pokemon(number=number) else None
        self.type1 = type.upper() if self.validate_pokemon(type=type) else None
        self.type2 = type2.upper() if self.validate_pokemon(type2=type2) else None
        self.ability = ability.title() if self.validate_pokemon(ability=ability) else None
        self.ability2 = ability2.titlte() if self.validate_pokemon(ability2=ability2) else None
        self.h_ability =  h_ability.title() if self.validate_pokemon(h_ability=h_ability) else None
        self.stage = stage if 0 < stage < 4 else 1
        
        self.hp = hp
        self.atk = atk
        self.defn = defn
        self.sp_atk = sp_atk
        self.sp_def = sp_def
        self.speed = speed
        self.in_pokedex = False
        
    def validate_pokemon(self, name=None, number=None, type=None, type2=None, ability=None,
                         ability2=None, h_ability=None):
        if name and any(pokemon['Name'] == name.title() for pokemon in dex):
            return True
        
        elif number and any(pokemon['Number'] == number for pokemon in dex):
            return True
        
        if type and type.upper() in type_list:
            return True

        elif type2 and self.validate_pokemon(type=type2) and type2.upper() != self.type1:
            return True
        
        if ability and ability.title() in ability_list:
            return True
        
        elif ability2 and self.validate_pokemon(ability=ability2) and ability2.title() != self.ability:
            return True
        
        elif h_ability and self.validate_pokemon(ability=h_ability) and h_ability.title() not in [self.ability,self.ability2]:
            return True
        
        return False

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
    Testmon = Pokemon(number=25,
                      type="flying",
                      type2="fire",
                      ability="drought",
                      ability2="drought",
                      h_ability="",)
    print (Testmon)
