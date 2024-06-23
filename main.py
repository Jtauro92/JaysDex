from add_pokemon import Add_Pokemon as AP
from add_stats import add_stats as AS
from view_pokemon import View_Pokemon as VP
from menu import Menu as M
import msvcrt as MS
print("Jason's Dexeditor ")


class dex_menu:
    def __init__(self):
        self.option = True

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
        proceed = 0
        while True:
            M().main_menu(proceed)
            MS.kbhit()
            proceed = MS.getch()
        
            if proceed == b'1':
                AP().main()
                proceed = int(proceed)

            elif proceed == b'2':
                AS().add_stats()
                self.option = True

            elif proceed == b'3':
                VP().main()
                proceed = int(proceed)

            if proceed == b'0':
                print('\nThank you\n')
                break


if __name__ == '__main__':
    dex_menu().main()