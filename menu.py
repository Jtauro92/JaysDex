from rich.panel import Panel
from rich.box import DOUBLE, MINIMAL, SQUARE, ASCII, ASCII_DOUBLE_HEAD,\
    HEAVY, HEAVY_HEAD, ROUNDED,SQUARE_DOUBLE_HEAD
from rich.text import Text
from tools import minput,cprint, color_str as c, clear_console as clear
import time

class Menu():
    def __init__(self, title, subtitle, options: dict):
        self.title = title
        self.subtitle = subtitle
        self.options = options
        self.current_row = 0
        
    def menu_panel(self) -> Panel:
        menu_screen = Panel(Text(self.menu_options(), 
                                 justify='center'),
                            title=self.title,
                            subtitle=self.subtitle,
                            box=ROUNDED,
                            padding=(1,1,0,1))
        return menu_screen
        
    def menu_options(self) -> str:
        menu_text = ""
        for idx, option in enumerate(self.options.keys()):
            if idx == self.current_row:
                menu_text += f"<<< {option} >>>\n"
            else:
                menu_text += f"{option}\n"
        return menu_text
    
    def display_menu(self) -> None:
        clear()
        cprint(self.menu_panel())
        
    def add_option(self, option: str) -> None:
        self.options.append(option)
    
    def run(self) -> None:
        def process(selected_option):
            try:
                if any(selected_option == option for option in self.options):
                    self.options[selected_option]()
            except TypeError:
                cprint(f"You selected '{selected_option}'")
                time.sleep(1)
                clear()
                
        while True:
            self.display_menu()
            process(self.select_option())
            
    def select_option(self) -> str:
        selected_option: str = ''
        key = minput()
        if key == 'UP' and self.current_row > 0:
            self.current_row -= 1
        elif key == 'DOWN' and self.current_row < len(self.options) - 1:
            self.current_row += 1
        elif key == 'ENTER':
            selected_option = list(self.options.keys())[self.current_row]
        return selected_option

if __name__ == '__main__':
    menu = Menu("Main Menu", 
                "Select an Option", 
                {'Option 1':'',
                 'Option 2':'',
                 'Option 3':'',
                 'Exit': exit})
    menu.run()

        
        