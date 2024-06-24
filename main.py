from multiprocessing import process
from add_pokemon import Add_Pokemon as AP
from add_stats import add_stats as AS
from view_pokemon import View_Pokemon as VP
from menu import Menu as M
import msvcrt as MS
from rich.console import Console 
from rich import print as rprint
console = Console()

class dex_menu:
    def __init__(self):
        self.ap = AP().main
        self.as_ = AS().main
        self.vp = VP().main
        self.joblist = [(b'1',self.ap),
                        (b'2',self.as_),
                        (b'3',self.vp)]
        
    def set_option(self,number= None,version=None):
        while (number not in [b'0',b'1',b'2',b'3']) or (int(number) == version):
            rprint('\n[bold red]Invalid Entry. Try Again![/bold red]')
            MS.kbhit()
            print("\033[A\033[2K\033[A", end='')
            number = MS.getch()
        return number
        
    def processes(self,hit):
        for job in self.joblist:
            if (hit == job[0]):
                job[1]()
                break
        return int(job[0])

    def main(self):
        M().main_menu()
        MS.kbhit()
        selection = MS.getch()
        selection = self.set_option(selection)
        while selection != b'0':
            version = self.processes(selection)
            M().main_menu(int(selection))
            MS.kbhit()
            selection = MS.getch()
            selection = self.set_option(selection,version)
        rprint('[bold green]\nGoodbye![/bold green]')


  
if __name__ == '__main__':

    dex_menu().main()