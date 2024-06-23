import mysql.connector
import os


class Pokemon:
    def __init__(self):
        self.attributes = ['number','name','type1','type2','ability',
                            'ability2','h_ability','stage','hp','atk',
                            'def','sp_atk','sp_def','speed']
        self.type_list = ['FIRE','WATER','GRASS','ELECTRIC','ICE','FIGHTING',
                          'POISON','GROUND','FLYING','PSYCHIC','BUG','ROCK',
                          'GHOST','DARK','DRAGON','STEEL','FAIRY','NORMAL']
        self.name = ''
        self.number = 0
        self.type1 = ''
        self.type2 = ''
        self.ability = ''
        self.ability2 = ''
        self.hidden_ability = ''
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
        self.cursor.execute("select * FROM national_pokedex")
        self.dex = self.cursor.fetchall()

        with open('abilities.csv', 'r') as f:
            for line in f:
                for ability in line.split(','):
                    self.ability_list.append(ability.strip())       

if __name__ == '__main__': 
    print(Pokemon().ability_list)
