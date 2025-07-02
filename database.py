from multiprocessing import connection
import mysql.connector
import time


attributes = ['Number','Name','Type1','Type2','Ability','Ability2',
              'Hidden_Ability','Stage']
type_list = ['FIRE','WATER','GRASS','ELECTRIC','ICE','FIGHTING',
                    'POISON','GROUND','FLYING','PSYCHIC','BUG','ROCK',
                    'GHOST','DARK','DRAGON','STEEL','FAIRY','NORMAL'] 
  


class Pokedex():
    DATABASE_INFO = {
    'host': 'localhost',
    'user': 'root',
    'password': 'devry123',
    'database': 'pokedex',
    'autocommit': True
}
    def __init__(self, database: dict = DATABASE_INFO):
        self.database = database

    @classmethod
    def connectDB(cls,database = DATABASE_INFO):
        try:
            mydb = mysql.connector.connect(**database)
            return mydb
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            print("Unable to connect to the database.")
    
    def create_db(self):
        connection = Pokedex.connectDB()
        if connection:
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS Pokemon " 
                        + "Number INT PRIMARY KEY , "
                        + "Name VARCHAR(20) , "                       
                        + "Type1 VARCHAR(255), "
                        + "Type2 VARCHAR(255), "
                        + "Ability VARCHAR(255), "
                        + "Ability2 VARCHAR(255), "
                        + "Hidden_Ability VARCHAR(255), "
                        + "Stage INT)")
            connection.close()
        
    def getPokemon(self, name: str):
        connection = self.connectDB()
        if connection:
            with connection.cursor() as cursor:
                query = """SELECT P_Name, Pokemon_Number, p_type1, p_type2, 
                            p_ability1, p_ability2,
                            h_ability FROM Pokemon WHERE P_Name = %s"""
                cursor.execute(query, (name,))
                result = cursor.fetchone()
            connection.close()
            return result
        
    def addPokemon(self, pokemon):
        if pokemon:
            connection = self.connectDB()
            if connection:
                with connection.cursor() as cursor:
                    query = """INSERT INTO Pokemon 
                            (P_Name, Pokemon_Number,p_type1, 
                            p_type2, p_ability1, p_ability2, h_ability) 
                            VALUES (%s, %s, %s, %s, %s, %s, %s)"""
                    cursor.execute(query, (pokemon.name, pokemon.number,
                                        pokemon.type1, pokemon.type2,
                                        pokemon.ability, pokemon.ability2,
                                        pokemon.h_ability))
                connection.close()
                
    def deletePokemon(self, name: str):
        connection = self.connectDB()
        if connection:
            with connection.cursor() as cursor:
                query = "DELETE FROM Pokemon WHERE P_Name = %s"
                cursor.execute(query, (name,))
            connection.close()
    
    def updateStats(self, name: str, column: str, value):
        connection = self.connectDB()
        if connection:
            with connection.cursor() as cursor:
                query = f"UPDATE Pokemon SET {column} = %s WHERE P_Name = %s"
                cursor.execute(query, (value, name))
            connection.close()

    
    def get_db_data(self,query):
        connection = self.connectDB()
        if connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                connection.close()
                return result

    def getAllPokemon(self) -> list[dict]:
        connection = self.connectDB()
        if connection:
            with connection.cursor() as cursor:
                query = "SELECT * FROM Pokemon"
                cursor.execute(query)
                result = cursor.fetchall()
                dex = [dict(zip(attributes,row)) for row in result]
                connection.close()
                return dex
        else:
            return []
                
    def pokemonDispenser(self):
        connection = self.connectDB()
        if connection:
            with connection.cursor() as cursor:
                query = "SELECT * FROM Pokemon"
                cursor.execute(query)
                while True:
                    row = cursor.fetchone()  # Fetch one row at a time
                    if row is None:  # No more rows
                        connection.close()
                        break
                    yield row
                connection.close()

    @staticmethod
    def load_ability_list():
        ability_list=[]
        with open('abilities.csv', 'r') as f:
            for line in f:
                for ability in line.split(','):
                    ability_list.append(ability.strip()) 
        return ability_list

dex = Pokedex().getAllPokemon()
ability_list = Pokedex().load_ability_list()
  
if __name__ == '__main__':
    pokedex = Pokedex()
    print(dex)