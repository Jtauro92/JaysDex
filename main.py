from add_pokemon import Add_Pokemon as AP
from add_stats import add_stats as AS
from view_pokemon import View_Pokemon as VP
from menu import Menu as M
import msvcrt as MS
from rich.console import Console
print("Jason's Dexeditor ")

class dex_menu:
    def __init__(self):
        self.console = Console()
    def set_option(self,number= None):
        try:
            if 0 <= int(number) <= 4:
                return int(number)
            else:
                print("Invalid Entry")
                return  None
        except ValueError:
            print('\nInvalid Entry')
            return None
    
    def main(self):
        while True:
            proceed = 0
            M().main_menu()
            MS.kbhit()
            proceed = MS.getch()
            while True:
                if proceed == b'1':
                    AP().main()
                    proceed = int(proceed)
                    M().main_menu(proceed)
                    MS.kbhit()
                    while (MS.getch() == b'1') or (int(MS.getch()) > 3):
                        print('\nInvalid Entry. Try Again!')
                        MS.kbhit()
                        print("\033[A\033[2K\033[A", end='')                 
                    proceed = MS.getch()

                if proceed == b'2':
                    AS().add_stats()
                    proceed = int(proceed)
                    M().main_menu(proceed)
                    MS.kbhit()
                    while MS.getch() == b'2' or (int(MS.getch()) > 3):
                        print('\nInvalid Entry. Try Again!')
                        MS.kbhit()
                        print("\033[A\033[2K\033[A", end='')
                    proceed = MS.getch()

                if proceed == b'3':
                    VP().main()
                    proceed = int(proceed)
                    M().main_menu(proceed)
                    MS.kbhit()
                    while MS.getch() == b'3':
                        print('\nInvalid Entry. Try Again!')
                        MS.kbhit()
                        print("\033[A\033[2K\033[A", end='')
                    proceed = MS.getch()

                if proceed == b'0':
                    self.console.clear()
                    print('\nThank you\n')
                    return


if __name__ == '__main__':
    dex_menu().main()