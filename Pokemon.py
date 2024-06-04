import mysql.connector
import itertools
import prettytable

class Pokemon:
    def __init__(self):
        self.attributes = ['number','name','type1','type2','ability',
                            'ability2','h_ability','stage','hp','atk',
                            'def','sp_atk','sp_def','speed']
        self.type_list = []
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

        self.cursor.execute("select DISTINCT P_Type1, P_Type2 FROM pokemon")
        self.type_list = list(set(itertools.chain(*self.cursor.fetchall())))

        self.cursor.execute("select P_Name FROM pokemon")
        self.name_list = list(set(itertools.chain(*self.cursor.fetchall())))

        self.cursor.execute("select Pokemon_Number FROM pokemon")
        self.num_list = list(set(itertools.chain(*self.cursor.fetchall())))

        with open('abilities.csv', 'r') as f:
            for line in f:
                for ability in line.split(','):
                    self.ability_list.append(ability.strip())       

    def set_Type(self, type):
        if type.isnumeric() == False:
            type = type.upper()
            if type in self.type_list:
                return type
            else:
                print('\nThis type doesn\'t exist')
                return None
        else:
            print('\nInvalid')
            return None

if __name__ == '__main__': 
    column_names = Pokemon().attributes[0:8]
    table = prettytable.PrettyTable(column_names)
    for pokemon in Pokemon().dex:
        table.add_row(pokemon)
    print(table)

