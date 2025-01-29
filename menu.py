from rich.panel import Panel
from rich.layout import Layout
from rich.box import DOUBLE, MINIMAL, SQUARE, ASCII, ASCII_DOUBLE_HEAD,\
    HEAVY, HEAVY_HEAD, ROUNDED,SQUARE_DOUBLE_HEAD
from rich.text import Text
from tools import minput,cprint, color_str as c, clear_console as clear
import time
import rich.columns as columns

def exit():
    clear()
    cprint("Goodbye!")
    time.sleep(1)
    clear()
    raise SystemExit

class Menu():
    def __init__(self, title, options: dict={}, escape = {'Exit': exit},):
        self.title = title
        self.subtitle = "Select an option"
        self.options = options
        self.current_row = 0
        self.escape = escape
        
    def menu_panel(self) -> Panel:
        title_text = Text(str(self.title), style="bold yellow")

        menu_screen = Panel(
        self.menu_options(),
        title=title_text,
        subtitle=c(self.subtitle, 'error', 'r'),
        style="white on black",
        box=ROUNDED,
        padding=(2, 1, 0, 1)
    )
        return menu_screen

    def menu_options(self) -> Text:
        self.add_option(self.escape)
        menu_text = Text(justify='center')
        for idx, option in enumerate(self.options.keys()):
            style = 'success' if idx == self.current_row else None
            menu_text.append(c(f"<<< {option} >>>\n\n", style, 'r') if style else f"{option}\n\n")
        return menu_text
    
    def display_menu(self) -> None:
        clear()
        cprint(self.menu_panel())
        
    def add_option(self, option: dict) -> None:
        self.options.update(option)
    
    def run(self) -> None:
        def select_option() -> str:
            selected_option: str = ''
            key = minput()
            if key == 'UP' and self.current_row > 0:
                self.current_row -= 1
            elif key == 'DOWN' and self.current_row < len(self.options) - 1:
                self.current_row += 1
            elif key == 'ENTER':
                selected_option = list(self.options.keys())[self.current_row]
            return selected_option
        
        def process(selected_option):
            try:
                if any(selected_option == option for option in self.options):
                    self.options[selected_option]()
            except TypeError:
                cprint(f"You selected '{selected_option}'")
                time.sleep(1)
   
        while True:
            self.display_menu()
            selected_option = select_option()
            if selected_option == 'Cancel':
                break
            process(selected_option)
            
class SubMenu(Menu):
    def __init__(self, title, options: dict ={}, escape = {'Cancel': ''}):
        super().__init__(title, options = options, escape=escape)
        
class Seletion_Menu(Menu):
    def __init__(self, title, options: dict ={}, escape = {'Cancel': ''}):
        super().__init__(title, options = options, escape=escape)
        

if __name__ == '__main__':
    options = []
    row, col = divmod(50, 2)
    for i in range(1, 11):
        options.append(f"Option {i}")
    columns = columns.Columns(options, equal=True)
    cprint(columns)
    

