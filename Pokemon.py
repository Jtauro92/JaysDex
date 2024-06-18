import mysql.connector
class Pokemon:

    def __init__(self):
        self.attributes = ['number','name','type1','type2','ability',
                            'ability2','h_ability','stage','hp','atk',
                            'def','sp_atk','sp_def','speed']
        self.type_list = ['FIRE','WATER','GRASS','ELECTRIC','ICE','FIGHTING',
                          'POISON','GROUND','FLYING','PSYCHIC','BUG','ROCK',
                          'GHOST','DARK','DRAGON','STEEL','FAIRY','NORMAL']
        self.name_list = []
        self.num_list = []
        self.dex = []
        self.ability_list = []
        self.load_attributes()

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
        self.cursor.execute("select * FROM pokemon")
        self.dex = self.cursor.fetchall()


        self.cursor.execute("select P_Name FROM pokemon")
        for i in self.cursor.fetchall():
            self.name_list.append(i[0])

        self.cursor.execute("select Pokemon_Number FROM pokemon")
        for i in self.cursor.fetchall():
            self.num_list.append(i[0])

        with open('abilities.csv', 'r') as f:
            for line in f:
                for ability in line.split(','):
                    self.ability_list.append(ability.strip())       

        
             
if __name__ == '__main__': 
    print(Pokemon().num_list)
