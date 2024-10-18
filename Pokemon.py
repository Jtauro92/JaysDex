
from sqlite3 import connect
from unittest import result
import mysql.connector
import msvcrt as m
from rich.console import Console as console
import os

cprint = console().print
clear_console = console().clear
def clear_line():
    print("\033[A\033[2K", end='', flush=True)
    
def minput():
        m.kbhit()
        return m.getch()
    


class Pokemon:
    def __init__(self,name=None,number=None,type1=None,type2=None,ability=None,ability2=None,h_ability=None,
                 stage=None,hp=None,atk=None,defn=None,sp_atk=None,sp_def=None,speed=None):
        self.attributes = ['number','name','type1','type2','ability',
                            'ability2','h_ability','stage','hp','atk',
                            'def','sp_atk','sp_def','speed']
        self.type_list = ['FIRE','WATER','GRASS','ELECTRIC','ICE','FIGHTING',
                          'POISON','GROUND','FLYING','PSYCHIC','BUG','ROCK',
                          'GHOST','DARK','DRAGON','STEEL','FAIRY','NORMAL']
        self.name = name
        self.number = number
        self.type1 = type1
        self.type2 = type2
        self.ability = ability
        self.ability2 = ability2
        self.h_ability = h_ability
        self.stage = stage
        self.hp = hp
        self.atk = atk
        self.defn = defn
        self.sp_atk = sp_atk
        self.sp_def = sp_def
        self.speed = speed
        self.dex, self.ability_list = [],[]
        self.load_attributes()
        self.clear = lambda: os.system('cls')
    def in_pokedex(self):
        if self.name in self.dex:
            return True
        return False    
        
    def check_type(self):
        if Pokemon.type1 in self.type_list and Pokemon.type2 in self.type_list:
            return True
        return False
    
    def check_ability2(self):
        if self.ability2 in self.ability_list  and self.ability2 == self.ability:
            return True
        return False
    def __repr__(self):
        return f"{self.name}"     
        
    def __str__(self):
        return f"{self.name} is a {self.type1} type Pokemon with {self.hp} HP"

    def connect_to_db(self,database='pokedex'):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="devry123",
            database= database,
            autocommit=True
        )
        return mydb

        

    def load_attributes(self):
        connection = self.connect_to_db()
        with connection.cursor() as cursor:
            cursor.execute("select * FROM Pokemon")
            result = cursor.fetchall()
            columns = ['Number','Name','Type1','Type2','Ability','Ability2','Hidden_Ability','Stage']
            for row in result:
                row_dict = dict(zip(columns,row))
                self.dex.append(row_dict)

            with open('abilities.csv', 'r') as f:
                for line in f:
                    for ability in line.split(','):
                        self.ability_list.append(ability.strip()) 
                connection.close() 
                    
    def get_db_data(self,query):
        connection = self.connect_to_db()
        with connection.cursor() as cursor:
            cursor.execute(query)
            connection.close()
            return cursor.fetchall()
             

if __name__ == '__main__':
    P = Pokemon("Charmander")
    name = P.name
    print(P.in_pokedex())
