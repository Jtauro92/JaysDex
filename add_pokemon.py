from Pokemon import Pokemon as P
from view_pokemon import color as C
from add_stats import add_stats as AS
from prettytable import PrettyTable as PT

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

    def validate_Name(self, name):
        while name.isnumeric() == True:
            print(C().color_string('error','\nNumbers are invalid!\n'))
            name = input('Enter Pokemon Name: ')
        else:
            name = name.title()
            if name == 'N':
                print(C().color_string('error','\nYou have chosen to cancel\n'))
                return 
            while name in self.name_list:
                print(C().color_string('error',' \nThis Pokemon already exist!\n'))
                name = input('Enter Pokemon Name: ').title()
            else:
                return name

    def validate_Number(self, number):
        while number.isnumeric() == False:
            number = number.upper()
            if number == 'N':
                print(C().color_string('error','\nYou have chosen to cancel!\n'))
                return
            else:
                print(C().color_string('error','\nInvalid! Only numbers are allowed!\n'))
                number = input('Enter Pokemon Number: ')

        number = int(number)
        if (number in self.num_list):
            print(C().color_string('error','\nThis Pokemon already exist!\n'))
            number = self.validate_Number(input('Enter Pokemon Number: '))
        else:
            if (number < 1) or (number > 1025):
                print(C().color_string('error','\nInvalid! Number must be between 1 and 1025!\n'))
                number = self.validate_Number(input('Enter Pokemon Number: '))

        return number
    
    def set_Type(self, type):
        while type.isnumeric() == True:
            print(C().color_string('error','\nNumbers are invalid!\n'))
            type = input('Enter type: ')
        
        type = type.upper()

        while type not in self.type_list:
            type = type.upper()
            if type == 'N':
                print(C().color_string('error','\nYou have chosen to cancel\n'))
                return
            else:
                print(C().color_string('error','\nInvalid! This type doesn\'t exist!\n'))
                self.set_Type(input('Enter Primary type: '))
        else:
            return type
    
    def set_Type2(self, type1,type2):
        if type2 is (None):
            return None
        else:
            while type2.isnumeric() == True:
                print(C().color_string('error','\nNumbers are invalid!\n'))
                type2 = input('Enter type: ')
            
            type2 = type2.upper()

            if type2 not in self.type_list:
                type2 = type2.upper()
                if (type2 == 'N') or (type2 == ''):
                    return type2
                else:
                    print(C().color_string('error','\nInvalid! This type doesn\'t exist!\n'))
                    self.set_Type2(type1,input('Enter type: '))
            elif type2 == type1:
                return None
            else:
                return type2


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

    def add_Dex_Entry(self,number,name,ability,type1,type2 = None, ability2 = None, hidden_ability = None,stage=1):
        self.cursor.execute("INSERT INTO pokemon VALUES (%s, %s, %s, %s, %s, %s, %s,%s)", 
                    (number, name, type1, type2, ability, ability2, hidden_ability,stage))
        self.cursor.execute("INSERT INTO stats (pokemon_number,p_name) VALUES (%s,%s)",
                    (number,name))
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

        self.type2 = self.set_Type2(self.type1,input('Enter Secondary Type: '))
        if (self.type2 is None) or (self.type2 == 'N'):
            print(C().color_string('error','\nYou have chosen to cancel\n'))
            return
        if self.type2 == '':
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

        AS().update_stat(self.name)

    def show_Pokemon(self):
        self.cursor.execute("SELECT Pokemon_number, P_Name, P_Type1, p_type2 FROM pokemon order by Pokemon_Number;")
        result = self.cursor.fetchall()
        count = self.cursor.rowcount
        dex = PT()
        dex.field_names = self.attributes[0:4]
        dex.add_rows(result)
        print(f'{dex} \n There are {count} pokemon in the pokedex.')

if __name__ == '__main__':
    add = Add_Pokemon()
    add.add_Pokemon()

    
        
    
        