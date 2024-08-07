from rich.console import Console
from rich.panel import Panel
from rich.box import DOUBLE, MINIMAL, SQUARE, ASCII, ASCII_DOUBLE_HEAD,\
    HEAVY, HEAVY_HEAD, ROUNDED,SQUARE_DOUBLE_HEAD
from rich.text import Text
import io

    
console = Console()
virtual_file = io.StringIO()
vconsole = Console(file=virtual_file,record=True)

class Menu:
    def __init__(self):
        self.console = Console()
        
    def display_menu(self,index=None,
                     color: str ='white',
                     header: str ='Main Menu',
                     options=[],
                     exit_statement='0. EXIT',
                     footer='[bold red](ENTER an Option)',
                     padding=(2,4,2,4),
                    width=None,
                    line_style = HEAVY):
        
        def option_generator(options, selected_index):
            for i, option in enumerate(options, start=1):
                if i - 1 != selected_index:
                    yield f"{i}. {option}"
                    
    
        if (len(options) == 1) and (index is not None):
            option_list = f'{exit_statement} '
        elif (len(options) > 1) and (index is not None):
            option_list = '\n\n'.join(option_generator(options, index-1)) + f'\n\n{exit_statement}'
        else:
            option_list = '\n\n'.join([f"{i}. {option}" for i, option in enumerate(options, start=1)]) + f'\n\n{exit_statement}'

        
        panel = Panel(
            Text(option_list, justify='left'),
            title=header,
            subtitle=footer,
            border_style=color,
            padding=padding,
            box=line_style,
            expand=False,
            width=width
        )
        return panel

    def main_menu(self,selection = None):
        return self.display_menu(index= selection,
                          options=['ADD POKEMON',
                                   'EDIT STATS ',
                                   'VIEW POKEMON  '],
                            header='Main Menu')
                                    
        
    def add_menu(self):
        self.display_menu(options=['ADD NEW POKEMON',
                                   'EDIT STATS '],
                            header='Add Menu')
                                    
        
    def add_pokemon_menu(self,options = [
                                        'ADD NEW POKEMON',
                                        'ADD MEGA EVOLUTION',
                                        'ADD GIGANTAMAX FORM',
                                        'ADD REGIONAL VARIANT',
                                        'ADD FORM'
                                        ]
                         ):
        return self.display_menu(options=options,
                            header='Add Pokemon Menu')
                                
    def view_pokemon_menu(self):
        self.display_menu(options=['VIEW ALL POKEMON',
                                   'SEARCH POKEMON BY NAME',
                                   'VIEW POKEMON BY TYPE',
                                   'VIEW POKEMON BY REGION'],
                            header='View Pokemon Menu')
        
    def view_one_pokemon_menu(self,
                              name='[blue]Charizard',
                              selection = None,
                              options = ['VIEW STATS',
                                   'VIEW EVOLUTION LINE',
                                   'VIEW MEGA EVOLUTION',
                                   'VIEW GIGANTAMAX FORM',
                                   'VIEW REGIONAL VARIANT',
                                   'VIEW FORM']):
        return self.display_menu(index = selection,
                                 options = options,
                                 header = name,

                                 exit_statement='9. SWITCH POKEMON\n\n0. EXIT',)

    

class View_Pokemon_Display:
    def __init__(self):
        pass

    def main_frame(self,
                   render= Menu().view_one_pokemon_menu(),
                   title='View Pokemon',
                   line = HEAVY,
                   panel_color = 'green',
                   padding = (2,5,1,5)):
        
        header =f'[u bold white]{title}[/u bold white]'
        
        return Panel(
            render,
            title=header,
            box=line,
            border_style=panel_color,
            padding = padding,
            expand=False,
            width=console.width  # Add this line to set the width to the terminal width
        )

    def prompt(self, string='',color_name='white'):
        color_map = {'error': 'bold red'}
        rich_color = color_map.get(color_name, 'white')
        return self.main_frame(
                        render=Text(string,
                                  justify = 'center',
                                  style = rich_color),
                        line = HEAVY_HEAD,padding=(1,11))
        
class Add_Pokemon_Display:
    def __init__(self):
        pass

    def main_frame(self,
                   options = ['Name:',
                            'Number:',
                            'Type:',
                            'Type 2:',
                            'Ability:',
                            'Ability 2:',
                            'Hidden Ability:'],
                    exit_statement = '8. CLEAR\n\n9. SUBMIT\n\n0. EXIT',
                    index = None,
                   title='Add Pokemon',
                   line = HEAVY,
                   panel_color = 'blue',
                   padding = (2,5,1,5),
                   footer = '[bold red](ENTER an Option)'):
        
        header =f'[u bold white]{title}[/u bold white]'
        console.clear()
        
        return Menu().display_menu(color= panel_color,
                                   options=options,
                                   exit_statement=exit_statement,
                                   footer=footer,
                                   index=index,
                                   header=header,
                                   padding=padding,
                                   width=None,
                                   line_style=line) # Add this line to set the width to the terminal width
        
    def prompt(self, string='',color_name='white'):
        color_map = {'error': 'bold red'}
        rich_color = color_map.get(color_name, 'white')
        return Panel(
            Text(string,
                 justify = 'center',
                 style = rich_color),
            title='[u bold white]Add MegaEvolution',  # Add this line to set the title to 'Add Pokemon
            box=HEAVY_HEAD,
            border_style='orange_red1',
            padding=(1,11),
            expand=False)        
    
if __name__ == "__main__":
    console.print(Add_Pokemon_Display().prompt('This is a test','error',),justify='center')