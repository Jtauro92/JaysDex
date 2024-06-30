from add_pokemon import Add_Pokemon as AP
from add_stats import add_stats as AS
from view_pokemon import View_Pokemon as VP
from menu import Menu as M
import msvcrt as MS
from rich.console import Console 
from rich import print as rprint


clear_console = Console().clear
cprint = Console().print


def minput():
    MS.kbhit()
    return MS.getch()

class dex_menu:
    def __init__(self):

        self.joblist = {
                        b'1': AP().main,
                        b'2': AS().main,
                        b'3': VP().main,
                        b'0': 'exit'
                        }
    
    def set_option(self,number= None,version=None):
        while (number not in self.joblist) or (int(number) == version):
            rprint('\n[bold red]Invalid Entry. Try Again![/bold red]')
            number = minput()
            print("\033[A\033[2K\033[A", end='', flush=True)
        return number
        
    def processes(self,hit):
        for job in self.joblist:
            if hit == job:
                self.joblist[hit]()
                return int(hit)


    def main(self):
        main_menu = M().main_menu
        clear_console()
        cprint(main_menu())
        selection = self.set_option(minput())
        while selection != b'0':
            process_num = self.processes(selection)
            clear_console()
            cprint(main_menu(int(selection)))
            selection = self.set_option(minput(),process_num)
        clear_console()
        rprint('[bold green]Goodbye![/bold green]')
  
if __name__ == '__main__':
    dex_menu().main()