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
        self.ability2 = ''
        self.hidden_ability = ''

    def set_Type(self, type):
        if type.isnumeric() == False:
            type = type.upper()
            if type in self.type_list:
                return type
            else:
                print('\nThis type doesn\'t exist')
                return None
        else:
            print('\nInvalid')
            return None

    def validate_Name(self, name):
        if name.isnumeric() == False:
            name = name.title()
            if name in self.name_list:
                print('\nThis pokemon already exist')
                return None
            else:
                return name
        else:
            print('\nInvalid')
            return None

    def validate_Number(self, number):
        if number.isnumeric():
            number = int(number)
            if number in self.num_list:
                print('\nThis pokemon already exist')
                return None
            elif 0 < number <= 1008:
                return number
            else:
                print('\nNumber can\'t be entered')
                return None
        else:
            print('\nInvalid')
            return None 

    def validate_Ability(self, ability):
        if ability.isnumeric() == False:
            ability = ability.title()
            if ability in self.ability_list:
                return ability
            else:
                return None
        else:
            print('\nInvalid')
            return None

    def add_Dex_Entry(self,number,name,ability,type1,type2 = None, ability2 = None, hidden_ability = None):
        self.cursor.execute("INSERT INTO pokemon (Pokemon_Number, P_Name, P_Type1, P_Type2, P_Ability1, P_Ability2, H_Ability) VALUES (%s, %s, %s, %s, %s, %s, %s)", 
                    (number, name, type1, type2, ability, ability2, hidden_ability))
        self.mydb.commit()
        print('\nPokemon added to Pokedex!')

    def add_Pokemon(self):
        self.name = self.validate_Name(input('Enter Pokemon Name: '))
        if self.name is None:
            return

        self.number = self.validate_Number(input('Enter Pokemon Number: '))
        if self.number is None:
            return

        self.type1 = self.set_Type(input('Enter Primary Type: '))
        if self.type1 is None:
            return

        self.type2 = self.set_Type(input('Enter Secondary Type: '))
        if (self.type2 is None) or (self.type2 == self.type1):
            self.type2 = None

        self.ability = self.validate_Ability(input('Enter Ability: '))
        if self.ability is None:
            return

        self.ability2 = self.validate_Ability(input('Enter Ability #2: '))
        if self.ability2 == self.ability:
            self.ability2 = None

        self.hidden_ability = self.validate_Ability(input('Enter Hidden Ability: '))
        if (self.hidden_ability == (self.ability or self.ability2)):
            self.hidden_ability = None

        self.add_Dex_Entry(self.number, self.name, self.ability, self.type1, self.type2, self.ability2, self.hidden_ability)

if __name__ == '__main__':
    Add_Pokemon().add_Pokemon()
    for i, pokemon in enumerate(Add_Pokemon().dex):
        print(f"#{pokemon[0]:>04} {pokemon[1]}")
        print(f"{pokemon[2]}",end='')
        if pokemon[3] != None:
            print(f"/{pokemon[3]}\n")
        else:
            print('\n')
        
    print(f"There are {i+1} pokemon in the pokedex\n")
        