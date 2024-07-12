from Pokemon import cprint, clear_console, minput, clear_line
from add_pokemon import Add_Pokemon as AP, color
from add_stats import add_stats as AS
from view_pokemon import View_Pokemon as VP
from menu import Menu as M

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
            cprint(color('Invalid Entry. Try Again!','error'))
            number = minput()
            clear_line()
        return number
        
    def processes(self,hit):
        for job in self.joblist:
            if hit == job:
                self.joblist[hit]()
                return int(hit)
            
    def main(self):
        main_menu = M().main_menu
        clear_console()
        cprint(main_menu(),justify='center')
        selection = self.set_option(minput())
        while selection != b'0':
            process_num = self.processes(selection)
            clear_console()
            cprint(main_menu(int(selection)),justify='center')
            selection = self.set_option(minput(),process_num)
        clear_console()
        cprint(color('Goodbye!', 'success'))
  
if __name__ == '__main__':
    dex_menu().main()