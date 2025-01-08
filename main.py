#from add_pokemon import Add_Pokemon 
#from add_stats import add_stats as AS
#from view_pokemon import View_Pokemon as VP
from menu import Menu as m

joblist: dict = {
                'Add Pokemon':'ap',
                'Add Stats': 'as',
                'View Pokekmon': 'vp'
                }
    
def run() -> None:
    main_menu = m('Main Menu', joblist)
    main_menu.run()
  
if __name__ == '__main__':
    run()