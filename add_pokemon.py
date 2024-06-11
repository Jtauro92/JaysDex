from audioop import mul
from numpy import number
from Pokemon import Pokemon as P
from view_pokemon import color as C
from view_pokemon import View_Pokemon as VP
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

    def validate_Name(self,name):
        while name.isnumeric() == True:
            print(C().color_string('error','\nNumbers are invalid!\n'))
            name = input('Enter Pokemon Name: ')
        else:
            name = name.title()
            if name == '':
                print(C().color_string('error','\nName cannot be empty!\n'))
                name = self.validate_Name(input('Enter Pokemon Name: '))
            if name == 'N':
                print(C().color_string('error','\nYou have chosen to cancel!\n'))
                return 
            if name in self.name_list:
                print(C().color_string('error',' \nThis Pokemon already exist!\n'))
                name = self.validate_Name(input('Enter Pokemon Name: '))

        return name

    def validate_Number(self,number):
        while number.isnumeric() == False:
            if number.upper() == 'N':
                print(C().color_string('error','\nYou have chosen to cancel!\n'))
                return
            else: 
                print(C().color_string('error','\nOnly numbers are valid!\n'))
                number = input('Enter Pokedex Number: ')
        else:
            number = int(number)
            if not (0<number<=1025):
                print(C().color_string('error','\nInvalid Pokedex Number!\n'))
                number = self.validate_Number(input('Enter Pokedex Number: '))
            if number in self.num_list:
                print(C().color_string('error',' \nThis Pokemon already exist!\n'))
                number = self.validate_Number(input('Enter Pokedex Number: '))
            
        return number
    
    def set_Type(self,type):
        while type.isnumeric() == True:
            print(C().color_string('error','\nNumbers are invalid!\n'))
            type = input('Enter Primary Type: ')
        else:
            type = type.upper()
            if type == 'N':
                print(C().color_string('error','\nYou chose to quit!\n'))
                return
            if (type not in self.type_list):
                print(C().color_string('error','\nThis type doesn\'t exist!\n'))
                type = self.set_Type(input('Enter Primary Type: '))

        return type

    def set_Type2(self,type1,type2):
        while type2.isnumeric() == True:
            print(C().color_string('error','\nNumbers are invalid!\n'))
            type2 = input('Enter Secondary Type: ')
        else:
            type2 = type2.upper()
            if type2 == 'N':
                print(C().color_string('error','\nYou chose to quit!\n'))
                return None
            elif (type2 == type1) or (type2 == ''):
                type2 = ''
            elif (type2 not in self.type_list):
                print(C().color_string('error','\nThis type doesn\'t exist!\n'))
                self.set_Type2(type1,input('Enter Secondary Type: '))

        return type2

    def set_Ability(self,ability):
        while ability.isnumeric() == True:
            print(C().color_string('error','\nNumbers are invalid!\n'))
            ability = input('Enter Ability: ')
        else:
            ability = ability.title()
            if ability == 'N':
                print(C().color_string('error','\nYou chose to quit!\n'))
                return
            if (ability not in self.ability_list):
                print(C().color_string('error','\nThis ability doesn\'t exist!\n'))
                ability = self.set_Ability(input('Enter Ability: '))

        return ability

    def set_Abitlity2(self,ability1,ability2):
        while ability2.isnumeric() == True:
            print(C().color_string('error','\nNumbers are invalid!\n'))
            ability2 = input('Enter Ability #2: ')
        else:
            ability2 = ability2.title()
            if ability2 == 'N':
                print(C().color_string('error','\nYou chose to quit!\n'))
                return None
            elif (ability2 == ability1) or (ability2 == ''):
                type2 = ''
            elif (ability2 not in self.ability_list):
                print(C().color_string('error','\nThis ability doesn\'t exist!\n'))
                self.set_Abitlity2(ability1,input('Enter Ability #2: '))

        return ability2

    def set_Hidden_Ability(self,ability1,ability2,ability3):
        while ability3.isnumeric() == True:
            print(C().color_string('error','\nNumbers are invalid!\n'))
            ability3 = input('Enter Hidden Ability: ')
        else:
            ability3 = ability3.title()
            if ability3 == 'N':
                print(C().color_string('error','\nYou chose to quit!\n'))
                return None
            elif (ability3 == ability1) or (ability3 == ability2) or (ability3 == ''):
                ability3 = ''
            elif (ability3 not in self.ability_list):
                print(C().color_string('error','\nThis ability doesn\'t exist!\n'))
                self.set_Hidden_Ability(ability1,ability2,input('Enter Hidden Ability: '))

        return ability3
        
    def add_Dex_Entry(self,number,name,ability,type1,type2 = None, ability2 = None, hidden_ability = None,stage=1):
        self.cursor.execute("INSERT INTO pokemon VALUES (%s, %s, %s, %s, %s, %s, %s,%s)", 
                    (number, name, type1, type2, ability, ability2, hidden_ability,stage))
        self.cursor.execute("INSERT INTO stats (pokemon_number,p_name) VALUES (%s,%s)",
                    (number,name))
        print(C().color_string('success','\nPokemon added to Pokedex!\n'))

    def main(self):
        while True:
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
            if (self.type2 is None):
                return
            if self.type2 == '':
                self.type2 = None
            

            self.ability = self.set_Ability(input('Enter Ability: '))
            if self.ability is None:
                return

            self.ability2 = self.set_Abitlity2(self.ability, input('Enter Ability #2: '))
            if (self.ability2 is None):
                return
            if self.ability2 == '':
                self.ability2 = None

            self.hidden_ability = self.set_Hidden_Ability(self.ability,self.ability2, input('Enter Hidden Ability: '))
            if (self.hidden_ability is None):
                return
            if self.hidden_ability == '':
                self.hidden_ability= None

            self.add_Dex_Entry(self.number, self.name, self.ability, self.type1, self.type2, self.ability2, self.hidden_ability)
            VP().view_one_pokemon(self.name)

            proceed = input(f'\nWould you like to enter {self.name}\'s stats?{C().color_string('error','\n(Press ENTER to continue)\n')}')
            if proceed.upper() == 'N':
                return
        
            AS().update_stat(self.name)

            proceed = input(f'\nAdd another Pokémon?{C().color_string('error','\n(Press ENTER to continue)\n')}')
            if proceed.upper() == 'N':
                return

    def show_Pokemon(self):
        self.cursor.execute("SELECT Pokemon_number, P_Name, P_Type1, p_type2 FROM pokemon order by Pokemon_Number;")
        result = self.cursor.fetchall()
        count = self.cursor.rowcount
        dex = PT()
        dex.field_names = self.attributes[0:4]
        dex.add_rows(result)
        print(f'{dex} \n {C().color_string('success',f'\nThere are {count} pokemon in the pokedex!\n'):}')

class Add_MegaEvolution(Add_Pokemon):
    def __init__(self):
        Add_Pokemon.__init__(self)

    def add_Mega_dex_entry(self, number,name,type1,type2,ability,ability2,hidden_ability):
        self.cursor.execute('''INSERT INTO megas (pokemon_number,p_name,m_type1,m_type2,m_ability1,m_ability2,m_h_ability)
                    VALUES (%s,%s,%s,%s,%s,%s,%s);''',
                    (number,name,type1,type2,ability,ability2,hidden_ability))
        self.cursor.execute('select m_number from megas where p_name = %s',(name,))
        result = self.cursor.fetchall()
        for i in result:
            meganumber = i[0]
        self.cursor.execute('INSERT INTO stats (pokemon_number,p_name, m_number) VALUES (%s,%s,%s)',(number,name,meganumber))
        print(C().color_string('success','\nMega Evolution added to Pokedex!\n'))

    def show_Mega_Evo(self):
        pass

    def main(self):
        self.name = VP().set_name('Enter Pokemon Name: ')
        if self.name is None:
            return
        
        self.number = self.cursor.execute('SELECT Pokemon_number FROM pokemon WHERE P_Name = %s',(self.name,))

if __name__ == '__main__':
   M = Add_MegaEvolution()
   M.add_Mega_dex_entry(9,'C','Fire','Dragon','Tough Claws',None,'Drought')

    
        
    
        