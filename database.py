import mysql.connector

attributes = ['Number','Name','Type1','Type2','Ability','Ability2',
              'Hidden_Ability','Stage']
type_list = ['FIRE','WATER','GRASS','ELECTRIC','ICE','FIGHTING',
                    'POISON','GROUND','FLYING','PSYCHIC','BUG','ROCK',
                    'GHOST','DARK','DRAGON','STEEL','FAIRY','NORMAL']    

class Pokedex():
    def __init__(self):
        pass

    def connect_to_db(self,database='pokedex'):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="devry123",
            database= database,
            autocommit=True
        )
        return mydb
    
    def get_db_data(self,query):
        connection = self.connect_to_db()
        with connection.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()
        connection.close()
        
    def load_dex(self):
        dex=[]
        result = self.get_db_data("select * FROM Pokemon")
        columns = attributes
        for row in result:
            dex.append(dict(zip(columns,row)))
        return dex
    
    def load_ability_list(self):
        ability_list=[]
        with open('abilities.csv', 'r') as f:
            for line in f:
                for ability in line.split(','):
                    ability_list.append(ability.strip()) 
        return ability_list

dex = Pokedex().load_dex()
ability_list = Pokedex().load_ability_list()
  
if __name__ == '__main__':
    pokedex = Pokedex()
    print(dex)