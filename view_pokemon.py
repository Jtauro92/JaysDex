from Pokemon import * 
from menu import Menu as M , View_Pokemon_Display as VPD
from rich.table import Table
from rich.text import Text
from rich.columns import Columns as C

prompt = VPD().prompt
#View_Pokemon class inherits from Pokemon class
#View_Pokemon class is responsible for displaying the pokemon data
class View_Pokemon(Pokemon):
    def __init__(self):
        super().__init__()
        self.main_frame = VPD().main_frame
        self.main_menu = M().view_one_pokemon_menu
        self.color = color().color_rich
        self.color_map = color().color_map
        self.table_color = color().table_color
        self.job_map = {
                        b'1':self.view_stats
                        }

    def set_name(self,name):
        while True:
            if name == '0':
                return name
            if name.isnumeric() == False:
                name = name.title()
                if any(name == pokemon['Name'] for pokemon in self.dex):
                    return name
                else:
                    clear_console()
                    cprint(prompt('This pokemon doesn\'t exist! Try again!','error'),justify='center')
            else:
                name = int(name)
                for pokemon in self.dex:
                    if name == pokemon['Number']:
                        return pokemon['Name']
                    else:
                        clear_console()
                        cprint(prompt('This pokemon doesn\'t exist! Try again!','error'),justify='center')
            name = input()
        
    def set_option(self,number= None,version=None):
            while (number not in self.job_map) and (number not in [b'9',b'0']) or(int(number) == version) :
                cprint(self.color('Invalid Entry. Try Again!','error'))
                number = minput()
                clear_line()
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
        for pokemon in self.dex:
            if (entry == pokemon['Name']):
                title_color = self.color_map.get(pokemon['Type1'].lower(), 'white')
                table_color = self.table_color.get(pokemon['Type1'].lower(), 'white')
                row = [str(pokemon[key]) for key in ['Type1', 'Type2', 'Ability', 'Ability2','Hidden_Ability']]
            
                table = Table(
                            title=f'#{pokemon['Number']:04} {pokemon['Name']}',
                            title_style=title_color, 
                            padding=(0,1),
                            expand=True,
                            show_edge=True,
                            border_style=table_color,
                            header_style=table_color
                            )
                
                for column_name in self.attributes[2:7]:
                    table.add_column(column_name,justify='center',style=table_color)
                table.add_row(*row)
                return table
        
    def view_mega_pokemon(self, selection=None,option=None):
        result  = self.get_db_data(f'''select pokemon_number, p_name, m_type1, m_type2,m_ability1 from megas
                            where p_name like '{self.name}%';''')
        dex =[]
        column_names = ['Number','Name','Type1','Type2','Ability']
        for i in result:
            row_dict = dict(zip(column_names,i))
            dex.append(row_dict)
            
        tables = []
            
        for pokemon in dex:
            table = Table(
                        title=f'(mega) {pokemon['Name']}\n',
                        padding=(0,1),
                        expand=True,
                        show_edge=False,
                        )

            for i in column_names[2:]:
                table.add_column(i,justify='center')
            
            row = ([str(attr) for attr in list(pokemon.values())[2:]])
            table.add_row(*row)
            tables.append(table)

        grid = C(tables,align='center',padding=(2,4))
        columns = C([grid,M().view_one_pokemon_menu(self.name,
                                                      selection=selection,
                                                      options=option)],
                    title='[u]Mega Evolution\n',
                    expand=True,
                    align='center',
                    padding=(4,0))
        finished_columns = C([self.pokemon_data(self.name),columns],
                             expand=True,
                             align='center',
                             padding=(4,0))
        cprint(self.main_frame(finished_columns),justify='center',style= 'red')

    def  view_evolution_line(self,selection=None,options=None):
        for pokemon in self.dex:
            if self.name == pokemon['Name']:
                if pokemon['Stage'] == 1:
                    if self.name == "Eevee":
                        column = [f'{pokemon["Name"]} evolves into:']
                        for pokemon2 in self.dex:
                            if pokemon2['Name'] in ['Vaporeon','Jolteon','Flareon','Espeon','Umbreon','Leafeon','Glaceon','Sylveon']:
                                column.append(self.pokemon_data(pokemon2['Name']))
                        tables = C(column,expand=True,align='center',padding=(1,0,3,0))
                    else:
                        for pokemon2 in self.dex:
                            if pokemon2['Number'] == (pokemon['Number']+1):
                                if pokemon2['Stage'] == 2:
                                    column = [f'{pokemon["Name"]} evolves into:']
                                    column.append(self.pokemon_data(pokemon2['Name']))
                                    for pokemon3 in self.dex:
                                        if pokemon3['Number'] == (pokemon2['Number']+1):
                                            if pokemon3['Stage'] == 3:
                                                column.append(f'{pokemon2["Name"]} evolves into:')
                                                column.append(self.pokemon_data(pokemon3['Name']))
                    tables = C(column,expand=True,align='center',padding=(1,0))      
                        
                if pokemon['Stage'] == 2:
                    if self.name in ['Vaporeon','Jolteon','Flareon','Espeon','Umbreon','Leafeon','Glaceon','Sylveon']:
                        column = [f'{self.name} evolves from:']
                        column.append(self.pokemon_data('Eevee'))
                        tables = C(column,expand=True,align='center',padding=(1,0))
                    else:
                        for pokemon2 in self.dex:
                            if pokemon2['Number'] == (pokemon['Number']-1):
                                column = [f'{pokemon["Name"]} evolves from:']
                                column.append(self.pokemon_data(pokemon2['Name']))
                                for pokemon3 in self.dex:
                                    if pokemon3['Number'] == (pokemon['Number']+1):
                                        if pokemon3['Stage'] == 3:
                                            column.append(f'{pokemon["Name"]} evolves into:')
                                            column.append(self.pokemon_data(pokemon3['Name']))
                    tables = C(column,expand=True,align='center',padding=(1,0))

                if pokemon['Stage'] == 3:
                    for pokemon2 in self.dex:
                        if pokemon2['Number'] == pokemon['Number']-1:
                            column = [f'{pokemon["Name"]} evolves from:']
                            column.append(self.pokemon_data(pokemon2['Name']))
                            for pokemon3 in self.dex:
                                if pokemon3['Number'] == pokemon2['Number']-1:
                                    column.append(f'{pokemon2["Name"]} evolves from:')
                                    column.append(self.pokemon_data(pokemon3['Name']))
                    tables = C(column,expand=True,align='center',padding=(1,0))
        columns = C([tables,M().view_one_pokemon_menu(self.name,
                                                      selection=selection,
                                                      options=options)],
                    title='[u]Evolution Line\n',
                    expand=True,
                    align='center',
                    padding=(2,0))
        finished_columns = C([self.pokemon_data(self.name),columns],
                             expand=True,
                             align='center',
                             padding=(2,0))
        cprint(self.main_frame(finished_columns),justify='center')

    def pokemon_can_mega_evolve(self,name):
        megasymbol = self.get_db_data(f"select mega FROM megas where p_name like '{self.name}%';")
        if len(megasymbol) > 0:
            return True
        else:
            return False
        
    def pokemon_can_evolve(self,name):
        for pokemon in self.dex:
            for pokemon2 in self.dex:
                if name == pokemon['Name']:
                    if pokemon['Stage'] == 1:
                        if name == "Eevee":
                            return True
                        else:
                            if pokemon2['Number'] == pokemon['Number']+1:
                                if pokemon2['Stage'] == 2:
                                    return True
                                else:
                                    return False
                    elif pokemon['Stage'] == 2:
                        return True
                    elif pokemon['Stage'] == 3:
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

    def old_main(self):
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
            
    def main(self):
        while True:
            options = ['VIEW STATS']
            key = ''
            key_to_update = 1
            clear_console()
            cprint(prompt('Which Pokemon?'),justify='center')
            self.name = self.set_name(input())
            if self.name == '0':
                clear_console()
                cprint(self.color('You have chosen to quit!', 'error'))
                self.name = None
                return
            else:
                clear_console()
                if self.pokemon_can_evolve(self.name) == True:
                    key_to_update +=1
                    options.append('VIEW EVOLUTION LINE')
                    key = str(key_to_update).encode()
                    self.job_map[key] = self.view_evolution_line
                if self.pokemon_can_mega_evolve(self.name) == True:
                    key_to_update +=1
                    options.append('VIEW MEGA EVOLUTION')
                    print(key_to_update)
                    key = str(key_to_update).encode()
                    self.job_map[key] = self.view_mega_pokemon
                        
                view_pokemon_layout = (C([
                                            self.pokemon_data(self.name),
                                            M().view_one_pokemon_menu(self.name,options=options)
                                          ],
                                    expand=True,
                                    align='center',
                                    padding=(2,0)))
                cprint(self.main_frame(view_pokemon_layout),justify='center')
                selection = self.set_option(minput())
                while True:
                    if selection == b'9':
                            break
                    elif selection == b'0':
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
        
        self.table_color = {
                            'fire': 'white on red',
                            'water': 'white on blue',
                            'grass': 'bold black on green',
                            'poison': 'white on purple',
                            'flying': 'white on sky_blue1',
                            'bug': 'bold black on chartreuse4',
                            'normal': 'bold black on white',
                            'electric': 'black on yellow',
                            'ground': 'white on orange4',
                            'rock': 'black on tan',
                            'fighting': 'white on orange_red1',
                            'psychic': 'white on magenta',
                            'ghost': 'white on navy_blue',
                            'ice': 'bold black on cyan',
                            'dragon': 'white on deep_pink4',
                            'dark': 'bold white on grey30',
                            'steel': 'bold black on grey82',
                            'fairy': 'bold black on plum1',
                            }

        self.color_map = {
                            'fire': 'bold red',
                            'water': 'bold blue',
                            'grass': 'bold green',
                            'poison': 'bold purple',
                            'flying': 'bold sky_blue1',
                            'bug': 'bold chartreuse4',
                            'normal': 'white',
                            'electric': 'yellow',
                            'ground': 'bold orange4',
                            'rock': 'bold tan',
                            'fighting': 'bold orange_red1',
                            'psychic': 'bold magenta',
                            'ghost': 'bold navy_blue',
                            'ice': 'bold cyan',
                            'dragon': 'bold deep_pink4',
                            'dark': 'bold grey30',
                            'steel': 'bold grey82',
                            'fairy': 'bold plum1',
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
    View_Pokemon().main()