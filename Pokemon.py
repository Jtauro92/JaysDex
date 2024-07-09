import mysql.connector
import msvcrt as m
from rich.console import Console as console
import os

cprint = console().print
clear_console = console().clear

def minput():
        m.kbhit()
        return m.getch()
    
def get_db_data(query):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="devry123",
    database="pokedex",
    autocommit=True
    )
    cursor = mydb.cursor()
    cursor.execute(query)
    fetch = cursor.fetchall()
    mydb.close()
    return fetch

class Pokemon:
    def __init__(self):
        self.attributes = ['number','name','type1','type2','ability',
                            'ability2','h_ability','stage','hp','atk',
                            'def','sp_atk','sp_def','speed']
        self.type_list = ['FIRE','WATER','GRASS','ELECTRIC','ICE','FIGHTING',
                          'POISON','GROUND','FLYING','PSYCHIC','BUG','ROCK',
                          'GHOST','DARK','DRAGON','STEEL','FAIRY','NORMAL']
        self.name = None
        self.number = None
        self.type1 = None
        self.type2 = None
        self.ability = None
        self.ability2 = None
        self.hidden_ability = None
        self.dex = []
        self.ability_list = []
        self.load_attributes()
        self.clear = lambda: os.system('cls')
        

    def connect_to_db(self,database='pokedex'):
        self.mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="devry123",
        database= database,
        autocommit=True
        )
        self.cursor = self.mydb.cursor()
    

    def load_attributes(self):
        self.connect_to_db()
        result = self.get_db_data("select * FROM Pokemon")
        columns = ['Number','Name','Type1','Type2','Ability','Ability2','Hidden_Ability','Stage']
        for row in result:
            row_dict = dict(zip(columns,row))
            self.dex.append(row_dict)

        with open('abilities.csv', 'r') as f:
            for line in f:
                for ability in line.split(','):
                    self.ability_list.append(ability.strip())  
                    
    def get_db_data(self,query):
        self.cursor.execute(query)
        return self.cursor.fetchall()
             

if __name__ == '__main__': 
    print(Pokemon().dex)
