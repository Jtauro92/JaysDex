from tools import minput, cprint, color_str as c, clear_console as clear
from pokemon import Pokemon, name_check, number_check, dex

class AddNew(Pokemon):
    def __init__(self):
        super().__init__()
        
        
    @property
    def name(self) -> str:
        return self._name
        
    @name.setter
    @name_check
    def name(self, name: str):
        if (any(pokemon["Name"] != name for pokemon in dex)):
            self._name = name

    @property
    def number(self) -> int:
        return self._number

    @number.setter
    @number_check
    def number(self, number: int):
        if not any(pokemon["Number"] == number for pokemon in dex):
            self._number = number


        
        
if __name__ == "__main__":
    clear()
    cprint("Welcome to the Pokemon Add New Menu")
    new_pokemon = AddNew()
    new_pokemon.number = 734
    cprint(new_pokemon)
    
    
    