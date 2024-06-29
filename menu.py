from re import L
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
        
    def display_menu(self,index=None,color='',header='Main Menu',options=[],
                     footer='[bold red](ENTER an Option)'):
        def option_generator(options, selected_index):
            for i, option in enumerate(options, start=1):
                if i - 1 != selected_index:
                    yield f"{i}. {option}"
                    
        if index is not None:
            option_list = '\n\n'.join(option_generator(options, index-1)) + '\n\n0. EXIT'
        else:
            option_list = '\n\n'.join([f"{i}. {option}" for i, option in enumerate(options, start=1)]) + '\n\n0. EXIT'
                    
        base_height = 5  # Adjust based on your design
        # Dynamic height based on options (2 lines per option in this setup)
        dynamic_height = (len(options)+1) * 2
        # Total height
        total_height = base_height + dynamic_height
        
        base_width = 15  # Adjust based on your design
        # Dynamic width based on options (2 lines per option in this setup)
        longest_string = max(options)
        dynamic_width = len(longest_string)+ 20
        # Total width
        total_width = base_width + dynamic_width
        
        panel = Panel(
            option_list,
            title=header,
            subtitle=footer,
            style=color,
            padding=(2,3,2,3),
            box=ROUNDED,
            width=total_width,
            height=total_height,
            expand=False
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
                                   'VIEW FORM'],
                              footer = '(N to Quit)'):
        return self.display_menu(index = selection,
                                 options = options,
                                 header = name,
                                 footer = footer)

    

class View_Pokemon_Display:
    def __init__(self):
        pass

    def main_frame(self,
                   render= Menu().view_one_pokemon_menu(),
                   title='View Pokemon',
                   line = HEAVY,
                   panel_color = 'green',
                   padding = (2,5,1,5),
                   subtitle = '[bold red](N to Quit)[/bold red]'):
        
        header =f'[u bold white]{title}[/u bold white]'
        
        return Panel(
            render,
            title=header,
            subtitle=subtitle,
            box=line,
            border_style=panel_color,
            padding = padding,
            expand=False,
            width=console.width  # Add this line to set the width to the terminal width
        )

    def prompt(self, string='',color_name=None):
        color_map = {'error': 'bold red'}
        rich_color = color_map.get(color_name, 'white')
        return self.main_frame(
                        render=Text(string,
                                  justify = 'center',
                                  style = rich_color),
                        line = HEAVY_HEAD,padding=(1,11))
        
if __name__ == "__main__":
    View_Pokemon_Display().prompt('Invalid Entry. Try Again!','error')