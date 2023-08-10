import csv

class Pokemon:
    def __init__(self):
        self.attributes = ['number','name','type1','type2','ability',
                           'hp','atk','def','sp.atk','sp.def','speed']
        self.type_list = ['Normal','Grass','Fire','Water','Electric',
                          'Ground','Rock','Steel','Ice','Fighting',
                          'Flying','Psychic','Ghost','Dark','Dragon',
                          'Bug','Poison','Fairy']
        self.name_list = []
        self.num_list = []
        self.dex = []
        self.ability_list = []

        with open('abilities.csv','r') as abilities:
            self.ability_list = abilities.read().split(',')



        with open ('dex.csv','r') as dex:
            pokedex = csv.DictReader(dex)
            for pokemon in pokedex:
                self.dex.append(pokemon)
                self.name_list.append(pokemon['name'])
                self.num_list.append(int(pokemon['number']))

    def show_stats(self,entry):
        print(f"\n#{entry['number']:>04} {entry['name']}")
        print(f"{entry['type1']}",end='')
        if entry['type2'] != '':
            print(f"/{entry['type2']}",end='')
        else:
            print('',end='')
        print(f"\nAbility: \n\
HP: {entry['hp']}\n\
ATK: {entry['atk']}\n\
DEF: {entry['def']}\n\
SP.ATK: {entry['sp.atk']}\n\
SP.DEF: {entry['sp.def']}\n\
SPEED: {entry['speed']}")
        
print(Pokemon().ability_list)
