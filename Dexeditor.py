from add_pokemon import Add_Pokemon as AP
from add_stats import add_stats as AS
from view_pokemon import View_Pokemon as VP
print("Jason's Dexeditor ")


class dex_menu:
    def __init__(self):
        self.option = None

    def set_option(self,number= None):
        try:
            if 0 <= int(number) <= 4:
                self.option = int(number)
            else:
                print("Invalid Entry")
                self.option = None
        except ValueError:
            print('\nInvalid Entry')
            self.option = None

    def menu_display(self):
        print('''\b
            +=================+
            + 1. Add Pokemon  +
            + 2. Edit Stats   +
            + 3. View Pokemon +
            + 0. EXIT         +
            +=================+
            ''')
        
    def __main__(self):

        while self.option == None:
            self.menu_display()
            self.set_option(input('Enter option: '))
        
            if self.option == 1:
                AP().add_Pokemon()
                self.option = None

            elif self.option == 2:
                AS().add_stat()
                self.option = None

            elif self.option == 3:
                VP().view_pokemon()
                self.option = None

            elif self.option == 0:
                print('\nThank you\n')


if __name__ == '__main__':
    dex_menu().__main__()