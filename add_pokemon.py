import csv
from Pokemon import Pokemon as P
from add_stats import add_stats as AS

class Add_Pokemon(P): #Eventual menu option to add Pokemon to Pokedex
    
    def __init__(self):
        P.__init__(self)
        self.name = ''
        self.number = 0
        self.type1 = ''
        self.type2 = ''
        self.ability = ''

    def set_Type(self, type):
        if type in self.type_list:
            self.type1 = type
        elif type == 'N':
            print("\nYou chose to quit\n")
            self.type1 = 'N'
        else:
            print('\nThis type doesn\'t exist\n')
            self.type1 = 'N'


    
    def set_Type2(self, type):
        if (type == self.type1) or (type == ''):
            self.type2 = ''
        elif (type in self.type_list) and (type != self.type1):
            self.type2 = type
        else:
            print('\nInvalid\n')
            self.type2 = None


    def validate_Name(self, name):
        if name in self.name_list:
            print('\nThis pokemon already exist')
            self.name = None
        elif name not in self.name_list:
            self.name = name
        else:
            print('\nInvalid')
            self.name = None


    def validate_Number(self, number):
        try:
            self.number = int(number)
        except ValueError:
            self.number = None
        
 
        if self.number in self.num_list:
            print('\nThis pokemon already exist')
            self.number = None
        elif self.number == None:
            print('Invalid')
        else: 
            if 0 < self.number <= 1008:
                self.number = number
            else:
                print('\nNumber can\'t be entered')
                self.number = None

    def validate_Ability(self, ability):
        if ability in self.ability_list:
            self.ability = ability
        else:
            print('\nInvalid')
            self.ability = None

    def add_Dex_Entry(self):
        with open('dex.csv', 'a',newline='') as pokedex:
            entry = dict(name = self.name, number = self.number, type1 = self.type1.upper())
            if self.type2 != None:
                entry['type2'] = self.type2.upper()
            writer = csv.DictWriter(pokedex, fieldnames= self.attributes)
            writer.writerow(entry)
            print('\nPokemon added to Pokedex!')

    def add_Pokemon(self):
        checker = ''
        while checker.upper() != 'N':
            p = Add_Pokemon()
            p.set_Type(input('\nEnter Primary type:\n').capitalize())

            if p.type1 != 'N':
                p.set_Type2(input('\nEnter Secondary type:\n').capitalize())
     
                if p.type2 != None:
                    p.validate_Name(input("\nEnter name:\n").capitalize())

                    if p.name != None:
                        try:
                            p.validate_Number(input("\nEnter number:\n"))
                        except ValueError:
                            print('\nInvalid entry\n')
                            p.number = None

                        if p.number != None:
                            p.add_Dex_Entry()
                            checker = input('\nEdit stats? (N to quit)\n')
                            if checker != 'N':
                                AS().adjust_stat(p.name)
                                checker = input('\nAdd another Pokemon? (N to quit)\n')
                            elif checker == 'N':
                                checker = input('\nAdd another Pokemon? (N to quit)\n')
                                
                        else:
                            checker = input('\nTry again? (N to quit)\n')
                    else:
                        checker = input('\nTry again? (N to quit)\n')
                else:
                    checker = input('\nTry again? (N to quit)\n')
            elif p.type1 == 'N':
                checker = input('\nTry again? (N to quit)\n')

if __name__ == '__main__':
    Add_Pokemon().add_Pokemon()
    with open ('dex.csv','r',newline='') as dex:
        pokedex = csv.DictReader(dex)
        for i, pokemon in enumerate(pokedex):
            print(f"#{pokemon['number']:>04} {pokemon['name']}")
            print(f"{pokemon['type1']}",end='')
            if pokemon['type2'] != '':
                print(f"/{pokemon['type2']}\n")
            else:
                print('\n')
           
        print(f"There are {i+1} pokemon in the pokedex\n")
        