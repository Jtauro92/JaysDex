
from cgitb import text
from numpy import isin
from rich.console import Console
from rich.panel import Panel
from rich.box import DOUBLE, MINIMAL, SQUARE, ASCII, ASCII_DOUBLE_HEAD, DOUBLE,\
    HEAVY, HEAVY_HEAD, ROUNDED, SQUARE,SQUARE_DOUBLE_HEAD
from rich.text import Text
import os

class Menu:
    def __init__(self):
        self.console = Console()
        
    def display_menu(self,color='',header='Main Menu',options=[],
                     footer='[bold red](ENTER an Option)'):
        option_list = []
        if isinstance(options, list):
            option_list = '\n\n'.join([f"{i}. {option}" for i, option in enumerate(options, start=1)]) + '\n\n0. EXIT'
            
        base_height = 5  # Adjust based on your design
        # Dynamic height based on options (2 lines per option in this setup)
        dynamic_height = (len(options)+1) * 2
        # Total height
        total_height = base_height + dynamic_height
        
        base_width = 20  # Adjust based on your design
        # Dynamic width based on options (2 lines per option in this setup)
        longest_string = max(options)
        dynamic_width = len(longest_string)
        # Total width
        total_width = base_width + dynamic_width
        text = Text(option_list, justify='center')
        header =f'[u bold]{header}[/u bold]'
        
        panel = Panel(
            text,
            title=header,
            subtitle=footer,
            style=color,
            padding=(2),
            box=ROUNDED,
            width=total_width,
            height=total_height,
            expand=True,
        )
        self.console.print(panel)
        
    def main_menu(self):
        self.display_menu(options=['ADD POKEMON',
                                   'EDIT STATS ',
                                   'VIEW POKEMON'],
                            header='Main Menu')
                                    
        
    def add_menu(self):
        self.display_menu(options=['ADD NEW POKEMON',
                                   'EDIT STATS '],
                            header='Add Menu')
                                    
        
    def add_pokemon_menu(self):
        self.display_menu(options=['ADD NEW POKEMON',
                                   'ADD MEGA EVOLUTION',
                                   'ADD GIGANTAMAX FORM',
                                   'ADD REGIONAL VARIANT',
                                   'ADD FORM'],
                            header='Add Pokemon Menu')
                                
    def view_pokemon_menu(self):
        self.display_menu(options=['VIEW ALL POKEMON',
                                   'SEARCH POKEMON BY NAME',
                                   'VIEW POKEMON BY TYPE',
                                   'VIEW POKEMON BY REGION'],
                            header='View Pokemon Menu')
        
    def view_one_pokemon_menu(self,name='[blue]Charizard'):
        self.display_menu(options=['VIEW STATS',
                                   'VIEW EVOLUTION LINE',
                                   'VIEW MEGA EVOLUTION',
                                   'VIEW GIGANTAMAX FORM',
                                   'VIEW REGIONAL VARIANT',
                                   'VIEW FORM'],
                            header=name)
if __name__ == "__main__":
    menu = Menu()
    menu.view_one_pokemon_menu()