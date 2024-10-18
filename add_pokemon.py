from Pokemon import *
from view_pokemon import color as C, View_Pokemon as VP
from add_stats import add_stats as AS
from menu import Add_Pokemon_Display as APD

color = C().color_rich

clear_two_lines = lambda: (clear_line(), clear_line())

class Add_Pokemon(Pokemon): #Eventual menu option to add Pokemon to Pokedex
    def __init__(self):
        super().__init__()
        self.options = ['Name*:', 
                        'Pokedex Number*:', 
                        'Primary Type*:', 
                        'Secondary Type:', 
                        'Ability*:', 
                        'Ability #2:', 
                        'Hidden Ability:']
        self.index = None
        self.job_map ={b'1':self.validate_Name,
                        b'2':self.validate_Number,
                        b'3':self.set_Type,
                        b'4':self.set_Type2,
                        b'5':self.set_Ability,
                        b'6':self.set_Abitlity2,
                        b'7':self.set_Hidden_Ability,
                        b'8':self.clear_data,
                        b'9':self.add_Dex_Entry}
        self.data_table = VP().pokemon_data

    def validate_Name(self):
        name = input('Enter Pokemon Name: ')
        clear_line()
        while True:
            if name == '0':
                return
            if name.isnumeric():
                cprint(color('Numbers are invalid!','error'))
                
            elif name == '':
                cprint(color('Name cannot be empty!','error'))
            else:
                name = name.title()
                if any(name == pokemon['Name'] for pokemon in self.dex):
                    cprint(color('This Pokemon already exist!','error'))
                else:
                    self.name = name
                    self.options[0] = f'Name:               {self.name}'
                    return
            name = input('Enter Pokemon Name: ')
            clear_line()
            clear_line()
                
    def validate_Number(self):
        number = input('Enter Pokedex Number: ')
        clear_line()
        while True:
            if number == '0':
                return
            if (number.isnumeric() == False):
                cprint(color('Only numbers are valid!','error'))
            else:
                number = int(number)
                if not (0<number<=1025):
                    cprint(color('Invalid Pokedex Number!','error'))
                else:
                    if any(number == pokemon['Number'] for pokemon in self.dex):
                        cprint(color('This Pokemon already exist!','error'))
                    else:
                        self.options[1] = f'Pokedex Number:     {number}'
                        self.number = number
                        return
            number = input('Enter Pokedex Number: ')
            clear_two_lines()
    
    def set_Type(self):
        type = input('Enter Primary Type: ')
        clear_line()
        while True:
            if type == '0':
                return
            if type.isnumeric():
                cprint(color('Numbers are invalid!','error'))
            else:
                type = type.upper()
                if (type not in self.type_list):
                    cprint(color('This type doesn\'t exist!','error'))
                else:
                    self.options[2] = f'Primary Type:       {type}'
                    self.type1 = type
                    return
            type = input('Enter Primary Type: ')
            clear_two_lines()

    def set_Type2(self):
        if self.type1 == None:
            return 
        else:
            type2 = input('Enter Secondary Type: ')
            clear_line()
            while True:
                if type2 == '0':
                    return
                if type2.isnumeric():
                    cprint(color('Numbers are invalid!','error'))
                else:
                    type2 = type2.upper()
                    if (type2 not in self.type_list):
                        cprint(color('This type doesn\'t exist!','error'))
                    else:
                        if type2 == self.type1:
                            cprint(color('Cannot be the same as Primary type!','error'))
                        else:
                            self.options[3] = f'Secondary Type:     {type2}'
                            self.type2 = type2
                            return
                type2 = input('Enter Secondary Type: ')
                clear_two_lines()

    def set_Ability(self):
        ability = input('Enter Ability: ')
        clear_line()
        while True:
            if ability == '0':
                return
            if ability.isnumeric():
                cprint(color('Numbers are invalid!','error'))
            else:
                ability = ability.title()
                if (ability not in self.ability_list):
                    cprint(color('This ability doesn\'t exist!','error'))
                else:
                    self.options[4] = f'Ability:            {ability}'
                    self.ability = ability
                    return
            ability = input('Enter Ability: ')
            clear_two_lines()

    def set_Abitlity2(self):
        if self.ability == None:
            return 
        else:
            ability2 = input('Enter Ability #2: ')
            clear_line()
            while True:
                if ability2 == '0':
                    return
                if ability2.isnumeric():
                    cprint(color('Numbers are invalid!','error'))
                else:
                    ability2 = ability2.title()
                    if (ability2 not in self.ability_list):
                        cprint(color('This ability doesn\'t exist!','error'))
                    else:
                        if ability2 in [self.ability,self.hidden_ability]:
                            cprint(color('This ability has been entered!','error'))
                        else:
                            self.options[5] = f'Ability #2:         {ability2}'
                            self.ability2 = ability2
                            return
                ability2 = input('Enter Ability #2: ')
                clear_two_lines()

    def set_Hidden_Ability(self):
        if self.ability == None:
            return 
        else:
            ability3 = input('Enter Hidden Ability: ')
            clear_line()
            while True:
                if ability3 == '0':
                    return
                if ability3.isnumeric():
                    cprint(color('Numbers are invalid!','error'))
                else:
                    ability3 = ability3.title()
                    if (ability3 not in self.ability_list):
                        cprint(color('This ability doesn\'t exist!','error'))
                    else:
                        if ability3 in [self.ability,self.ability2]:
                            cprint(color('This ability has been entered!','error'))
                        else:
                            self.options[6] = f'Hidden Ability:     {ability3}'
                            self.hidden_ability = ability3
                            return
                ability3 = input('Enter Hidden Ability: ')
                clear_two_lines()
        
    def add_Dex_Entry(self):
        if any(attribute is None for attribute in [self.number,self.name,self.type1,self.ability]):
            cprint(color('All fields must be filled!','error'))
            return
        else:
            self.cursor.execute(f'''call insert_data
                                ('{self.number}',
                                '{self.name}',
                                '{self.type1}',
                                '{self.type2}',
                                '{self.ability}',
                                '{self.ability2}',
                                '{self.hidden_ability}')''')
            clear_console()
            cprint(color('Pokemon added to Pokedex!\n','success'),justify='center')
            cprint(self.data_table(self.name),justify='center')
            cprint('\nWould you like to enter stats for this Pokemon?')
            selection = minput()
            clear_two_lines()
            if selection == b'0':
                self.clear_data()
            else:
                AS().update_stat(self.name)
            self.clear_data()
            
    def clear_data(self):
        self.name = self.number = self.type1 = self.type2 = self.ability = self.ability2 = self.hidden_ability = None
        self.options = ['Name:','Pokedex Number:', 'Primary Type:', 'Secondary Type:',
                        'Ability:', 'Ability #2:', 'Hidden Ability:']

    #def old_main(self):
        clear_console()
        cprint(prompt('Enter Pokemon Name:'),justify='center')
        self.name = self.validate_Name(input())
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

        self.main()
    
    def set_option(self,number= None,version=None):
            while (number not in self.job_map) and (number != b'0') or (int(number) == version) :
                cprint(color('Invalid Entry. Try Again!','error'))
                number = minput()
                clear_line()
            return number
        
    def main(self):
        main_frame = APD().main_frame
        cprint(main_frame(options=self.options),justify='center')
        selection = self.set_option(minput())
        while True:
            if selection == b'0':
                self.clear_data()
                clear_console()
                return
            else:
                for key in self.job_map:
                    if selection == key:
                        self.index = int(selection)
                        clear_console()
                        cprint('\n',main_frame(options=self.options,index=self.index),justify='center')
                        self.job_map[selection]()
                        clear_console()
                        cprint(main_frame(options=self.options),justify='center')
                        selection = self.set_option(minput())

class Add_MegaEvolution(Add_Pokemon):
    def __init__(self):
        Add_Pokemon.__init__(self)

    def add_Mega_dex_entry(self, number,name,type1,type2,ability):
        self.cursor.execute(f'''call insert_mega_data ('{number}','{name}','{type1}','{type2}','{ability}')''')
        print(C().color_string('success','\nMega Evolution added to Pokedex!\n'))

    def get_form_name(self,name):
        print(f'{name} has multiple forms. Please select one of the following:\n')
        print('1. Mega X\n2. Mega Y\n')
        form = input('Enter form: ')
        while form not in ['1','2']:
            print(C().color_string('error','\nInvalid!\n'))
            form = input('Enter form: ')
        if form == '1':
            return name + ' X'
        if form == '2':
            return name + ' Y'
        
    

    def main(self,name=None,number=None):
        if name is None:
            name = VP().set_name(input('Enter Pokemon Name or Number: '))
        while True:
            if name in ['Charizard','Mewtwo']:
                self.name = self.get_form_name(name)
                for pokemon in self.dex:
                    if name == pokemon[1]:
                        self.number = pokemon[0]
            else:          
                if (number is not None) and (name is None):
                    self.number = number
                    for pokemon in self.dex:
                        if number == int(pokemon[0]):
                            self.name = pokemon[1]
                else:         
                    while (name == None) and (number == None):
                        name = VP().set_name(input('Enter Mega Pokemon Name or Number: '))
                        if name == 'N':
                            return
                        else:
                            self.name = name
                            for pokemon in self.dex:
                                if name == pokemon[1]:
                                    self.number = pokemon[0]
                    else:
                        self.name = name
                        for pokemon in self.dex:
                                if name == pokemon[1]:
                                    self.number = pokemon[0]
                                

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

            self.add_Mega_dex_entry(self.number, self.name, self.type1, self.type2, self.ability)
            VP().view_mega_pokemon(self.name)

            proceed = input(f'\nAdd another Mega Pokémon?{C().color_string('error','\n(Press ENTER to continue)\n')}')
            if proceed.upper() == 'N':
                return

class Add_Form(Add_Pokemon):
    pass

class Add_Gigantamax(Add_Pokemon):
    pass

if __name__ == '__main__':
    M = Add_MegaEvolution()
    A = Add_Pokemon()
    A.main()