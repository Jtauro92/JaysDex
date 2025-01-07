import msvcrt as m
from rich.console import Console as console
from rich.text import Text

def minput() -> str:
    while True:
        key = m.getch()
        if key == b'\xe0':  # Special keys (arrows, f keys, ins, del, etc.)
            key = m.getch()  # Get the second byte
            if key == b'H':  # Up arrow
                return 'UP'
            elif key == b'P':  # Down arrow
                return 'DOWN'
            elif key == b'K':  # Left arrow
                return 'LEFT'
            elif key == b'M':  # Right arrow
                return 'RIGHT'
        elif key in [b'\r', b'\n']:  # Enter key
            return 'ENTER'
        else:
            return key.decode('utf-8')  # Return other keys as normal characters

def color_str(string:str, color:str, type = None):
    color_map = {
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
        'success': 'bold green'
                }
    
    ascii_color_map = {
        'fire': '\033[48;5;1m ',
        'water': '\033[48;5;27m ',
        'grass': '\033[48;5;28m \033[38;5;15m',
        'poison': '\033[48;5;129m ',
        'flying': '\033[48;5;81m \033[38;5;0m',
        'bug': '\033[48;5;142m \033[38;5;232m',
        'normal': '\033[48;5;251m \033[38;5;0m',
        'electric': '\033[48;5;226m \033[38;5;0m',
        'ground': '\033[48;5;94m \033[38;5;0m',
        'rock': '\033[48;5;95m \033[38;5;0m',
        'fighting': '\033[48;5;208m \033[38;5;0m',
        'psychic': '\033[48;5;163m ',
        'ghost': '\033[48;5;55m \033[38;5;15m',
        'ice': '\033[48;5;45m \033[38;5;0m',
        'dragon': '\033[48;5;52m \033[38;5;15m',
        'dark': '\033[48;5;16m \033[38;5;15m',
        'steel': '\033[48;5;102m \033[38;5;232m',
        'fairy': '\033[48;5;212m \033[38;5;232m',
        'color': '\033[38;5;0m',
        'background_color': '\033[48;5;0m',
        'reset': '\033[0m',
        'error': '\033[38;5;196m',
        'success': '\033[38;5;46m'
                    }
        
    def rich(string:str = string ,type:str = color) -> Text:
            type = type.lower()
            rich_color = color_map.get(type, 'white')
            return Text(string,style=rich_color)
        
    def ascii(string:str = string, type:str = color) -> str:
        type = type.lower()
        color = ascii_color_map.get(type, 'white')
        return f"{color}{string} {ascii_color_map['reset']}"
        
    if type and type == 'r':
        new_str = rich()
    else:
        new_str = ascii()
        
    return new_str

def clear_console():
    console().clear()
    
def clear_line():
    print("\033[A\033[2K", end='', flush=True)
    
clear_two_lines = lambda : (clear_line(), clear_line())
    
def cprint(*args, **kwargs):
    console().print(*args, **kwargs)

if __name__ == '__main__':
    clear_console()
    cprint(color_str("Hello World", 'fire', 'r'))