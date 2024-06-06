from Pokemon import Pokemon as P
from prettytable import PrettyTable

class View_Pokemon(P):
    def __init__(self):
        P.__init__(self)
        self.name = None

    def set_name(self,name):
        if name.isnumeric() == False:
            name = name.title()
            if name in self.name_list:
                return name
        else:
            name = int(name)
            if name in self.num_list:
                for pokemon in self.dex:
                    if name == pokemon[0]:
                        return pokemon[1]
            else:
                print('\nInvalid')

    def view_all_pokemon(self):
        column_names = self.attributes[0:4]
        table = PrettyTable(column_names,align='c')
        print(table.header)
        for pokemon in self.dex:
            table.add_row(pokemon[0:4])
        print(table)


    def view_one_pokemon(self):
        column_names = self.attributes[0:7]
        table = PrettyTable(column_names)
        while self.name == None:
            self.name = self.set_name(input("\nWhich Pokemon? (N to quit)\n").capitalize())
            if self.name != 'N':
                for pokemon in self.dex:
                    if (self.name == pokemon[1]):
                        table.add_row(pokemon[:7])
                        print(color().color_string(pokemon[2],table))
                        table.clear_rows()

    def  view_evolution_line(self,name):
        table2 = PrettyTable()
        table2.header = False
        table3 = PrettyTable()
        table3.header = False
        for pokemon in self.dex:
            if name == pokemon[1]:
                if pokemon[7] == 1:
                    try:
                        pokemon2 = self.dex[pokemon[0]]
                        if pokemon2[7] == 2:
                            table2.add_row(pokemon2[0:7])
                            print(f'\n{pokemon[1]} evolves into: \n{table2}')
                            table2.clear_rows()
                            pokemon3 = self.dex[pokemon[0]+1]
                            if pokemon3[7] == 3:
                                table3.add_row(pokemon3[0:7])
                                print(f'\n{pokemon2[1]} evolves into: \n{table3}')
                                table3.clear_rows()
                                break
                        else:
                            print(f'\n{pokemon[1]} doesn\'t evolve.')   
                    except IndexError:
                        print(f'\n{pokemon[1]} doesn\'t evolve.')
                        break
                
                if pokemon[7] == 2:
                    pokemon2 = self.dex[pokemon[0]-2]
                    table2.add_row(pokemon2[0:7])
                    print(f'{pokemon[1]} evolves from: \n{table2}')
                    pokemon3 = self.dex[pokemon[0]]
                    if pokemon3[7] == 3:
                        table3.add_row(pokemon3[0:7])
                        print(f'\n{pokemon[1]} evolves into: \n{table3}')
                        table2.clear_rows()
                        table3.clear_rows()
                        break

                if pokemon[7] == 3:
                    pokemon2 = self.dex[pokemon[0]-2]
                    table2.add_row(pokemon2[0:7])
                    print(f'\n{pokemon[1]} evolves from: \n{table2}')
                    pokemon3 = self.dex[pokemon[0]-3]
                    table3.add_row(pokemon3[0:7])
                    print(f'\n{pokemon2[1]} evolves from: \n{table3}')
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

    def main(self):
        check = ''
        self.view_one_pokemon()
        check = input('\nView Stats? (Y/N) \n').upper()
        if check.isalpha() and check == 'Y':
            self.view_stats(self.name)
            check = input('\nView Evolution Line? (Y/N)\n').upper()
            if check.isalpha() and check == 'Y':
                self.view_evolution_line(self.name)
            else:
                return
        else:
            return


class color:
    def __init__(self):
        self.colors = [
            ('\033[48;5;1m ', 'fire'),
            ('\033[48;5;27m ', 'water'),
            ('\033[48;5;28m \033[38;5;15m', 'grass'),
            ('\033[48;5;129m ', 'poison'),
            ('\033[48;5;81m \033[38;5;0m', 'flying'),
            ('\033[48;5;142m \033[38;5;232m', 'bug'),
            ('\033[48;5;251m \033[38;5;0m', 'normal'),
            ('\033[48;5;226m \033[38;5;0m', 'electric'),
            ('\033[48;5;94m \033[38;5;0m', 'ground'),
            ('\033[48;5;95m \033[38;5;0m', 'rock'),
            ('\033[48;5;208m \033[38;5;0m', 'fighting'),
            ('\033[48;5;163m ', 'psychic'),
            ('\033[48;5;55m \033[38;5;15m', 'ghost'),
            ('\033[48;5;45m \033[38;5;0m', 'ice'),
            ('\033[48;5;52m \033[38;5;15m', 'dragon'),
            ('\033[48;5;16m \033[38;5;15m', 'dark'),
            ('\033[48;5;102m \033[38;5;232m', 'steel'),
            ('\033[48;5;212m \033[38;5;232m', 'fairy'),
            ('\033[38;5;0m', 'color'),
            ('\033[48;5;0m', 'background_color'),
            ('\033[0m', 'reset'),
            ('\033[38;5;196m', 'error')
            ('\033[38;5;46m', 'success')
        ]
        self.reset = '\033[0m'

    def color_string(self,type,string):
        type = type.lower()
        for color in self.colors:
            if type == color[1]:
                return f'{color[0]}{string}{self.reset}'
        return string

if __name__ == '__main__':
    VP = View_Pokemon()
    VP.view_one_pokemon()