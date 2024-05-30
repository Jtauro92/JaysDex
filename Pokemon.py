import mysql.connector
import itertools
import prettytable

class Pokemon:
  def __init__(self):
    self.mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="devry123",
    database="pokedex"
    )
    self.attributes = ['number','name','type1','type2','ability',
                        'ability2','h_ability','hp','atk','def','sp.atk','sp.def','speed']
    self.type_list = []
    self.name_list = []
    self.num_list = []
    self.dex = []
    self.ability_list = []

    self.cursor = self.mydb.cursor()

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

if __name__ == '__main__': 
    column_names = Pokemon().attributes[0:7]
    table = prettytable.PrettyTable(column_names)
    for pokemon in Pokemon().dex:
        table.add_row(pokemon)
    print(table)

