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
    
    def set_Type(self, type=None):
        type = type.upper()
        while type not in self.type_list:
            type = type.upper()
            if type.isnumeric() == True:
                print(C().color_string('error','\nNumbers are invalid!\n'))
                type = input('Enter Primary type: ').upper()
            else:
                if type == 'N':
                    print(C().color_string('error','\nYou chose to quit!\n'))
                    return
                else:
                    print(C().color_string('error','\nThis type doesn\'t exist!\n'))
                    type = input('Enter Primary type: ').upper()
        else:
            return type
    
    def set_Type2(self,type1,type2):
        type2 = type2.upper()
        while type2 not in self.type_list:
            type2 = type2.upper()
            if type2.isnumeric() == True:
                print(C().color_string('error','\nNumbers are invalid!\n'))
                type2 = input('Enter Secondary type: ').upper()
            else:
                if type2 == 'N':
                    print(C().color_string('error','\nYou chose to quit!\n'))
                    return 'N'
                else:
                    print(C().color_string('error','\nThis type doesn\'t exist!\n'))
                    type2 = input('Enter Secondary type: ').upper()
        else:
            if type2 == type1:
                return ''
            return type2

    def set_Ability(self, ability):
        ability = ability.title()
        while ability not in self.ability_list:
            ability = ability.title()
            if ability.isnumeric() == True:
                print(C().color_string('error','\nNumbers are invalid!\n'))
                ability = input('Enter ability: ').title()
            else:
                if ability == 'N':
                    print(C().color_string('error','\nYou chose to quit!\n'))
                    return
                else:
                    print(C().color_string('error','\nThis ability doesn\'t exist!\n'))
                    ability = input('Enter ability: ').title()
        else:
            return ability

    def set_Abitlity2(self,ability1,ability2):
        ability2 = ability2.title()
        while ability2 not in self.ability_list:
            ability2 = ability2.title()
            if ability2.isnumeric() == True:
                print(C().color_string('error','\nNumbers are invalid!\n'))
                ability2 = input('Enter ability #2: ').title()
            else:
                if ability2 == 'N':
                    print(C().color_string('error','\nYou chose to quit!\n'))
                    return 'N'
                else:
                    print(C().color_string('error','\nThis ability doesn\'t exist!\n'))
                    ability2 = input('Enter ability #2: ').title()
        else:
            if ability2 == ability1:
                return ''
            return ability2

    def set_Hidden_Ability(self,ability1,ability2,hidden_ability):
        hidden_ability = hidden_ability.title()
        while hidden_ability not in self.ability_list:
            hidden_ability = hidden_ability.title()
            if hidden_ability.isnumeric() == True:
                print(C().color_string('error','\nNumbers are invalid!\n'))
                hidden_ability = input('Enter Hidden ability: ').title()
            else:
                if hidden_ability == 'N':
                    print(C().color_string('error','\nYou chose to quit!\n'))
                    return 'N'
                else:
                    print(C().color_string('error','\nThis ability doesn\'t exist!\n'))
                    hidden_ability = input('Enter Hidden ability: ').title()
        else:
            if (hidden_ability == ability1) or (hidden_ability == ability2):
                return ''
            return hidden_ability
        
    def add_Dex_Entry(self,number,name,ability,type1,type2 = None, ability2 = None, hidden_ability = None,stage=1):
        self.cursor.execute("INSERT INTO pokemon VALUES (%s, %s, %s, %s, %s, %s, %s,%s)", 
                    (number, name, type1, type2, ability, ability2, hidden_ability,stage))
        self.cursor.execute("INSERT INTO stats (pokemon_number,p_name) VALUES (%s,%s)",
                    (number,name))
        print(C().color_string('success','\nPokemon added to Pokedex!'))

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
            return
        if self.type2 == '':
            self.type2 = None
        

        self.ability = self.set_Ability(input('Enter Ability: '))
        if self.ability is None:
            return

        self.ability2 = self.set_Abitlity2(self.ability, input('Enter Ability #2: '))
        if (self.ability2 is None) or (self.ability2 == 'N'):
            return
        if self.ability2 == '':
            self.ability2 = None

        self.hidden_ability = self.set_Hidden_Ability(self.ability,self.ability2, input('Enter Hidden Ability: '))
        if (self.hidden_ability is None) or (self.hidden_ability == 'N'):
            return
        if self.hidden_ability == '':
            self.hidden_ability= None

        self.add_Dex_Entry(self.number, self.name, self.ability, self.type1, self.type2, self.ability2, self.hidden_ability)

        check = True
        check = input(f'Would you like to enter {self.name}\'s stat\'s?{C().color_string('error','\n(Press ENTER to continue)}\n')}')
        if check.isalpha() == True:
            if check.upper() == 'N':
                return
            else:
                AS().add_stats(self.number,self.name)
        else:
            AS().add_stats(self.number,self.name)
 

    def show_Pokemon(self):
        self.cursor.execute("SELECT Pokemon_number, P_Name, P_Type1, p_type2 FROM pokemon order by Pokemon_Number;")
        result = self.cursor.fetchall()
        count = self.cursor.rowcount
        dex = PT()
        dex.field_names = self.attributes[0:4]
        dex.add_rows(result)
        print(C().color_string('success',f'{dex} \n There are {count} pokemon in the pokedex.'))

if __name__ == '__main__':
    A = Add_Pokemon()
    A.add_Pokemon()
    A.show_Pokemon()
    
        
    
        