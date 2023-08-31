import pandas as pd
from Pokemon import Pokemon as P

class Pokedex(P):
    def __init__(self):
        P.__init__(self)
        df = pd.read_csv('dex.csv')
        self.pokedex = df[['name', 'number', 'type1', 'type2']]
        self.name = ''
        self.number = 0

    def set_pokemon(self, name):
        # set pokemon name
        try:
            name = int(name)
            for pokemon in self.dex:
                if pokemon['number'] == name:
                    self.name = pokemon['name']
                    break
                else:
                    self.name = None
            
        if (name in self.name_list) or (name == 'N'):
            self.name = name

        else:
            self.name = None


    