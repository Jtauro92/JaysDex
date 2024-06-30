
from Pokemon import * 
from menu import View_Pokemon_Display as VPD, Menu as M
from rich.table import Table
from rich.text import Text
from rich.columns import Columns as C
from rich.prompt import Prompt
cinput = console().input
ask = Prompt.ask


class View_Pokemon(Pokemon):
    def __init__(self):
        Pokemon.__init__(self)
        self.main_frame = VPD().main_frame
        self.name = None
        self.color = color().color_rich
        self.color_map = color().color_map
        self.job_map = {
                        b'1':self.view_stats,
                        }
        
    def set_name(self,name):
        while True:
            if name.isnumeric() == False:
                name = name.title()
                if name == 'N':
                    return name
                else:
                    for pokemon in self.dex:
                        if name == pokemon[1]:
                            return name
                    else:
                        clear_console()
                        cprint(prompt('This pokemon doesn\'t exist! Try again!','error'),justify='center')
                        name = input()
            else:
                name = int(name)
                for pokemon in self.dex:
                    if name == pokemon[0]:
                        return pokemon[1]
                else:
                    clear_console()
                    cprint(prompt('This pokemon doesn\'t exist! Try again!','error'),justify='center')
                    name = input()
        
    def set_option(self,number= None,version=None):
            while (number not in self.job_map) and (number not in [b'9',b'0']) or(int(number) == version) :
                cprint('\n[bold red]Invalid Entry. Try Again![/bold red]')
                number = minput()
                print("\033[A\033[2K\033[A", end='', flush=True)
            return number    
        
    def view_all_pokemon(self):
        column_names = self.attributes[0:4]
        table = PrettyTable(column_names,align='c')
        for pokemon in self.dex:
            table.add_row(pokemon[0:4])
        print(table)

   # def view_one_pokemon(self, name=None):
        self.cursor.execute("select * FROM pokemon")
        dex = self.cursor.fetchall()
        column_names = self.attributes[0:7]
        table = PrettyTable(column_names)
        for pokemon in dex:
            if (name == pokemon[1]):
                table.add_row(pokemon[:7])
                print(color().color_string(pokemon[2],table))
                table.clear_rows()
   
    def pokemon_data(self, entry=None):
        dex = get_db_data("select * FROM pokemon")
        for pokemon in dex:
            if (entry == pokemon[1]):
                name,number = pokemon[1],pokemon[0]
                rich_color = self.color_map.get(pokemon[2].lower(), 'white')
                row = [str(attr) for attr in pokemon[2:7]]
            
        table = Table(title=f'#{number:04} {name}\n',
                      title_style=rich_color, 
                      padding=(0,1,0,1),
                      collapse_padding=False,
                      expand=True,
                      show_edge=False
                    )
        
        for column_name in self.attributes[2:7]:
            table.add_column(column_name)
        table.add_row(*row)
        return table
        
    def view_mega_pokemon(self, name=None):
        column_names = self.attributes[1:5]
        table = Table(headers=column_names)
        result  = self.get_db_data(f'''select p_name, m_type1, m_type2,m_ability1 from megas
                            where p_name like '{name}%';''')

        for i in result:
            result = list(i)
            name = f'(mega) {result[0]}' 
            result[0] = name
            table.add_row(result)
        print(f'\n{color().color_string(result[1],table)}')
        table.clear_rows()

    def  view_evolution_line(self,name):
        self.cursor.execute("select * FROM pokemon")
        dex = self.cursor.fetchall()
        table2 = Table(header = False)
        table3 = Table(header = False)
  
        for pokemon in dex:
            if name == pokemon[1]:
                if pokemon[7] == 1:
                    if name == "Eevee":
                        for pokemon in dex:
                            if pokemon[1] in ['Vaporeon','Jolteon','Flareon','Espeon','Umbreon','Leafeon','Glaceon','Sylveon']:
                                table2.add_row(pokemon[0:7])
                                print(f'\n{name} evolves from: \n{color().color_string(pokemon[2],table2)}')
                                table2.clear_rows()
                    else:
                        try:
                            pokemon2 = dex[(pokemon[0])]
                            if pokemon2[7] == 2:
                                table2.add_row(pokemon2[0:7])
                                print(f'\n{pokemon[1]} evolves into: \n{color().color_string(pokemon[2],table2)}')
                                table2.clear_rows()
                                pokemon3 = dex[(pokemon[0]+1)]
                                if pokemon3[7] == 3:
                                    table3.add_row(pokemon3[0:7])
                                    print(f'\n{pokemon2[1]} evolves into: \n{color().color_string(pokemon[2],table3)}')
                                    table3.clear_rows()
                        except IndexError:                       
                            pass
                        
                if pokemon[7] == 2:
                    if name in ['Vaporeon','Jolteon','Flareon','Espeon','Umbreon','Leafeon','Glaceon','Sylveon']:
                        for pokemon in dex:
                            if pokemon[1] == "Eevee":
                                table2.add_row(pokemon[0:7])
                                print(f'\n{name} evolves into: \n{color().color_string(pokemon[2],table2)}')
                                table2.clear_rows()
                    else:
                        pokemon2 = dex[(pokemon[0]-2)]
                        table2.add_row(pokemon2[0:7])
                        print(f'\n{pokemon[1]} evolves from: \n{color().color_string(pokemon[2],table2)}')
                        pokemon3 = dex[(pokemon[0])]
                        if pokemon3[7] == 3:
                            table3.add_row(pokemon3[0:7])
                            print(f'\n{pokemon[1]} evolves into: \n{color().color_string(pokemon[2],table3)}')
                            table2.clear_rows()
                            table3.clear_rows()

                if pokemon[7] == 3:
                    pokemon2 = dex[pokemon[0]-2]
                    if pokemon2 is not None:
                        table2.add_row(pokemon2[0:7])
                        print(f'\n{pokemon[1]} evolves from: \n{color().color_string(pokemon[2],table2)}')
                        pokemon3 = dex[(pokemon[0]-3)]
                        table3.add_row(pokemon3[0:7])
                        print(f'\n{pokemon2[1]} evolves from: \n{color().color_string(pokemon[2],table3)}')
                        table2.clear_rows()

    def pokemon_can_evolve(self,name):
        dex = self.get_db_data('select * FROM pokemon')
        for pokemon in dex:
            if name == pokemon[1]:
                if pokemon[7] == 1:
                    if name == "Eevee":
                         return True
                    else:
                        try:
                            pokemon2 = dex[(pokemon[0])]
                            if pokemon2[7] == 2:
                                return True
                        except IndexError:
                            return False
                elif pokemon[7] == 2:
                    return True
                elif pokemon[7] == 3:
                    return True
                else:
                    return False
            
    def search_by_type(self,type):
        column_names = self.attributes[0:7]
        table = PrettyTable(column_names)
        type = self.set_Type(type).upper()
        for pokemon in self.dex:
            if (type == pokemon[2]) or (type == pokemon[3]):
                table.add_row(pokemon[:7])
        print(table)              

    def stat_table(self,name):
        stats = self.get_db_data(f"select hp,atk,def,sp_atk,sp_def,speed FROM stats where P_Name = '{name}';")
        stats = [str(stat) for stat in stats[0]]
        table = Table()
        for column_names in self.attributes[8:]:
            table.add_column(column_names)
        table.add_row(*stats)
        return table

    def view_stats(self,selection,options):
        columns = C([self.stat_table(self.name),
                     M().view_one_pokemon_menu(self.name,selection=selection,options=options)],
                    title='Stats',
                    expand=True,
                    align='center',
                    padding=(2,0))
        finished_columns = (C([self.pokemon_data(self.name),columns],
                        expand=True,
                        align='center',
                        padding=(2,0)))
        cprint(self.main_frame(finished_columns),justify='center')

    def main(self):
        while True:
            while self.name == None:
                self.name = self.set_name(input("\nWhich Pokemon? (N to quit)\n").capitalize())
                if self.name != 'N':
                    self.view_one_pokemon(self.name)
                else:
                    self.clear()
                    print(color().color_string('error','\nYou have chosen to quit!\n'))
                    self.name = None
            
            proceed = input(f'\nView stats?').upper()
            if proceed.upper() == 'N':
                print(color().color_string('error','\nYou have chosen to quit!\n'))
                return
            else:
                self.view_stats(self.name)
            if self.pokemon_can_evolve(self.name) == True:
                proceed == input(f'\nView Evolution Line?')
                if proceed.upper() == 'N':
                    print(color().color_string('error','\nYou have chosen to quit!\n'))
                    self.name = None
                self.view_evolution_line(self.name)
            else:
                pass
            
            self.cursor.execute(f"select * FROM megas where p_name like '{self.name}%';")
            result = self.cursor.fetchall()
            if len(result) > 0:
                print(f'\nView Mega Pokemon?{color().color_string("error","\n(Press ENTER to continue or N to quit!)")}')
                m.kbhit()
                proceed = m.getch()
                if proceed.upper() == b'N':
                    self.clear()
                    print(color().color_string('error','\nYou have chosen to quit!\n'))
                    return
                self.view_mega_pokemon(self.name)
                
            print(f'\nView Another Pokemon?{color().color_string("error","\n(Press ENTER to continue or N to quit!)")}')
            m.kbhit()
            proceed = m.getch()
            if proceed.upper() == b'N':
                self.clear()
                print(color().color_string('error','\nYou have chosen to quit!\n'))
                return

            self.name = None
            clear_console
            
    def new_main(self):
        while True:
            options = ['VIEW STATS']
            key = ''
            tick = 1
            clear_console()
            cprint(prompt('Which Pokemon?'),justify='center')
            self.name = self.set_name(cinput())
            if self.name.upper() == 'N':
                clear_console()
                cprint(color().color_rich('You have chosen to quit!', 'error'))
                self.name = None
                return
            else:
                clear_console()
                if self.pokemon_can_evolve(self.name) == True:
                    key_to_update = tick+1
                    options.append('VIEW EVOLUTION LINE')
                    key = str(key_to_update).encode()
                    self.job_map[key] = self.new_main
                        
                view_pokemon_layout = (C([
                                        self.pokemon_data(self.name),
                                        M().view_one_pokemon_menu(self.name,options=options)
                                    ],
                                    expand=True,
                                    align='center',
                                    padding=(2,0)))
                cprint(VPD().main_frame(view_pokemon_layout),justify='center')
                selection = self.set_option(minput())
                while True:
                    if selection == b'9':
                            break
                    if selection == b'0':
                            clear_console()
                            cprint(color().color_rich('Goodbye!', 'success'))
                            self.name = None
                            return
                    else:
                        for key in self.job_map:
                            if selection == key:
                                clear_console()
                                self.job_map[selection](int(selection),options)
                                break
                    selection = self.set_option(minput(),int(selection))



                    
            
        


            
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
            ('\033[38;5;196m', 'error'),
            ('\033[38;5;46m', 'success')
        ]
        self.reset = '\033[0m'

        self.color_map = {
            'fire': 'red',
            'water': 'blue',
            'grass': 'green',
            'poison': 'purple',
            'flying': 'yellow',
            'bug': 'dark_green',
            'normal': 'white',
            'electric': 'yellow',
            'ground': 'brown',
            'rock': 'gray',
            'fighting': 'dark_red',
            'psychic': 'magenta',
            'ghost': 'light_gray',
            'ice': 'cyan',
            'dragon': 'dark_blue',
            'dark': 'black',
            'steel': 'light_gray',
            'fairy': 'light_magenta',
            'error': 'bold red',
            'success': 'bold green',
        }
        
    def color_string(self,type,string):
        type = type.lower()
        for color in self.colors:
            if type == color[1]:
                return f'{color[0]}{string}{self.reset}'
        return string
    
    def color_rich(self,string,type):
        type = type.lower()
        rich_color = self.color_map.get(type, 'white')
        return Text(string,style=rich_color)

if __name__ == '__main__':
    View_Pokemon().new_main()