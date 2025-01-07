from rich.panel import Panel
from rich.box import DOUBLE, MINIMAL, SQUARE, ASCII, ASCII_DOUBLE_HEAD,\
    HEAVY, HEAVY_HEAD, ROUNDED,SQUARE_DOUBLE_HEAD
from rich.text import Text
from tools import minput,cprint, color_str as c, clear_console as clear
import time

class Menu():
    def __init__(self, title, subtitle, options):
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
                            padding=(1,1))
        return menu_screen
        
    def menu_options(self) -> str:
        menu_text = ""
        for idx, option in enumerate(self.options):
            if idx == self.current_row:
                menu_text += f"<<< {option} >>>\n"
            else:
                menu_text += f"{option}\n"
        return menu_text
    
    def display_menu(self) -> None:
        clear()
        cprint(self.menu_panel())
    
    def run(self) -> int:
        while True:
            self.display_menu()
            key = minput()
            if key == 'UP' and self.current_row > 0:
                self.current_row -= 1
            elif key == 'DOWN' and self.current_row < len(self.options) - 1:
                self.current_row += 1
            elif key == 'ENTER':
                cprint(f"You selected '{self.options[self.current_row]}'")
                time.sleep(1)
                if self.options[self.current_row] == 'Exit':
                    break
        return self.current_row       

if __name__ == '__main__':
    menu = Menu("Main Menu", "Select an option", ["Option 1", "Option 2", "Option 3", "Exit"])
    number = menu.run()
    cprint(c(f"Number selected: {number}", 'success','r'))
        