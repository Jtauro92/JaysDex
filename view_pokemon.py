from Pokemon import Pokemon as P
from prettytable import PrettyTable

class View_Pokemon(P):
    def __init__(self):
        P.__init__(self)
        self.name = None

    def validate_Name(self, name):
        if name.isnumeric() == False:
            name = name.title()
            if (name in self.name_list) or (name == "N"):
                self.name = name
            else:
                print('\nThis pokemon doesn\'t exist')
        else:
            name = int(name)
            if name in self.num_list:
                self.name = name
            else:
                print('\nThis pokemon doesn\'t exist')

    def view_all_pokemon(self):
        column_names = self.attributes[0:4]
        table = PrettyTable(column_names)
        for pokemon in self.dex:
            table.add_row(pokemon[0:4])
        print(table)

    def view_one_pokemon(self):
        column_names = self.attributes[0:7]
        table = PrettyTable(column_names)
        while self.name == None:
            self.validate_Name(input("\nWhich Pokemon? (N to quit)\n").capitalize())
            if self.name != 'N':
                for pokemon in self.dex:
                    if (self.name == pokemon[1]) or (self.name == pokemon[0]):
                        table.add_row(pokemon[:7])
                        print(table)
                        table.clear_rows()
                        self.name = None

    def  view_evolution_line(self,name):
        table2 = PrettyTable()
        table2.header = False
        table3 = PrettyTable()
        table3.header = False
        for pokemon in self.dex:
            if name == pokemon[1]:
                if pokemon[7] == 1:
                    pokemon2 = self.dex[pokemon[0]]
                    if pokemon2[7] == 2:
                        table2.add_row(pokemon2[0:7])
                        print(f'{pokemon[1]} evolves into: \n{table2}')
                        table2.clear_rows()
                        pokemon3 = self.dex[pokemon[0]+1]
                        if pokemon3[7] == 3:
                            table3.add_row(pokemon3[0:7])
                            print(f'{pokemon2[1]} evolves into: \n{table3}')
                            table3.clear_rows()
                            break
                
                if pokemon[7] == 2:
                    pokemon2 = self.dex[pokemon[0]-2]
                    table2.add_row(pokemon2[0:7])
                    print(f'{pokemon[1]} evolves from: \n{table2}')
                    pokemon3 = self.dex[pokemon[0]]
                    if pokemon3[7] == 3:
                        table3.add_row(pokemon3[0:7])
                        print(f'{pokemon[1]} evolves into: \n{table3}')
                        table2.clear_rows()
                        table3.clear_rows()
                        break

                if pokemon[7] == 3:
                    pokemon2 = self.dex[pokemon[0]-2]
                    table2.add_row(pokemon2[0:7])
                    print(f'{pokemon[1]} evolves from: \n{table2}')
                    pokemon3 = self.dex[pokemon[0]-3]
                    table3.add_row(pokemon3[0:7])
                    print(f'{pokemon2[1]} evolves from: \n{table3}')
                    table2.clear_rows()
                    table3.clear_rows()
                    break
            
    def search_by_type(self,type):
        column_names = self.attributes[0:7]
        table = PrettyTable(column_names)
        type = self.set_Type(type).upper()
        for pokemon in self.dex:
            if (type == pokemon[2]) or (type == pokemon[3]):
                table.add_row(pokemon[:7])
        print(table)              

    def view_stats(self,name):
        column_names = self.attributes[8:]
        table = PrettyTable(column_names)
        self.cursor.execute(f"SELECT hp,atk,def,sp_atk,sp_def,speed FROM stats WHERE P_Name = '{name}'")
        pokemon = (self.cursor.fetchall())
        table.add_rows(pokemon)
        print(table)
        table.clear_rows()

if __name__ == '__main__':
    VP = View_Pokemon()
    VP.view_stats('Bulbasaur')