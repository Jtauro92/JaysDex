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
    def __init__(self,name,number=0,type='',type2=None,ability=None,ability2=None,h_ability=None,
                 stage=1,hp=0,atk=0,defn=0,sp_atk=0,sp_def=0,speed=0):
        
        self.name = name if self.validate_pokemon(name) else None
        self.number = number if self.validate_pokemon(number) else None
        self.type1 = type.upper() if type.upper() in type_list or type != ''.strip() else None
        self.type2 = type2
        self.ability = ability if self.validate_ability(ability) else None
        self.ability2 = ability2
        self.h_ability =  ability2
        self.stage = stage if 0 < stage < 4 else 1
        
        self.hp = hp
        self.atk = atk
        self.defn = defn
        self.sp_atk = sp_atk
        self.sp_def = sp_def
        self.speed = speed
        self.in_pokedex = False
        
    def validate_pokemon(self,name=None,number=0):
        if any (pokemon['Name'] == name for pokemon in dex):
            yield True
        if any (pokemon['Number'] == number for pokemon in dex):
            return True
        
        return False

     
        
    def validate_ability(self,ability=None):
        if ability in ability_list:
            return True
        else:
            return False
   


    def in_pokedex(self,name=None,number=None):
        if isinstance(name,str):
            return any(pokemon['Name'] == name for pokemon in dex)
        elif isinstance(number,int):
            return any(pokemon['Number'] == number for pokemon in dex)
            
    def type2_equals_type1(self):
        return self.type1 == self.type2

    def has_same_ability(self):
        if (self.ability2 is not None) and (self.ability2 == self.ability):
            return True 
        return False   
        
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
    Testmon = Pokemon(name="Charizard",
                      number=8000, 
                      type="Fire",
                      type2="Flying",
                      ability="drought",
                      ability2="drought",
                      h_ability="",)
    print (Testmon)
