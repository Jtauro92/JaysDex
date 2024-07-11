from Pokemon import *
from view_pokemon import color as C, View_Pokemon as VP
from add_stats import add_stats as AS
from menu import Add_Pokemon_Display as APD


color = C().color_rich
def clear_line():
    print("\033[A\033[2K\033[A\033[2K", end='', flush=True)

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
        name = input('\nEnter Pokemon Name: ')
        while name.isnumeric() == True:
            name = int(name)
            if name == 0:
                return
            else:
                clear_line()
                cprint(color('Numbers are invalid!','error'))
            name = input('Enter Pokemon Name: ')

        else:
            name = name.title()
            if name == '':
                    clear_line()
                    cprint(color('Name cannot be empty!','error'))
                    name = self.validate_Name()
            for pokemon in self.dex:
                if name == pokemon['Name']:
                    clear_line()
                    cprint(color('This Pokemon already exist!','error'))
                    name = self.validate_Name()
                    
        self.options[0] = f'Name:               {name}'
        self.name = name

    def validate_Number(self):
        number = input('\nEnter Pokedex Number: ')
        while number.isnumeric() == False:
            clear_line()
            cprint(color('Only numbers are valid!','error'))
            number = input('Enter Pokedex Number: ')
        else:
            number = int(number)
            if number == 0:
                        return
            if not (0<number<=1025):
                        clear_line()
                        cprint(color('Invalid Pokedex Number!','error'))
                        number = self.validate_Number()
            else:
                for pokemon in self.dex:
                    if number == pokemon['Number']:
                        clear_line()
                        cprint(color('This Pokemon already exist!','error'))
                        number = self.validate_Number()
                        
        self.options[1] = f'Pokedex Number:     {number}'
        self.number = number
    
    def set_Type(self):
        type = input('\nEnter Primary Type: ')
        while type.isnumeric() == True:
            if type == '0':
                return
            else:
                clear_line()
                cprint(color('Numbers are invalid!', 'error'))
                type = input('Enter Primary Type: ')
        else:
            type = type.upper()
            if (type not in self.type_list):
                clear_line()
                cprint(color('This type doesn\'t exist!','error'))
                type = self.set_Type()
        
        self.options[2] = f'Primary Type:       {type}'       
        self.type1 = type

    def set_Type2(self):
        if self.type1 == None:
            clear_line()
            cprint(color('\nPrimary Type must be set first!','error'))
            return
            
        else:
            type2 = input('\nEnter Secondary Type: ')
            while type2.isnumeric() == True:
                if type2 == '0':
                    return
                else:
                    clear_line()
                    cprint(color('Numbers are invalid!','error'))
                    type2 = input('Enter Secondary Type: ')
            else:
                type2 = type2.upper()
                if (type2 == self.type1) or (type2 == ''):
                    type2 = ''
                elif (type2 not in self.type_list):
                    clear_line()
                    cprint(color('This type doesn\'t exist!','error'))
                    self.set_Type2()

        self.options[3] = f'Secondary Type:     {type2}'
        self.type2 = type2

    def set_Ability(self):
        ability = input('\nEnter Ability: ')
        while ability.isnumeric() == True:
            if ability == '0':
                return
            else:
                clear_line()
                cprint(color('Numbers are invalid!', 'error'))
                ability = input('Enter Ability: ')
        else:
            ability = ability.title()
            if (ability not in self.ability_list):
                clear_line()
                cprint(color('This ability doesn\'t exist!','error'))
                self.set_Ability()

        self.options[4] = f'Ability:            {ability}'
        self.ability = ability

    def set_Abitlity2(self):
        if self.ability == None:
            clear_line()
            cprint(color('Primary Ability must be set first!','error'))
            return
        ability2 = input('\nEnter Ability #2: ')
        while ability2.isnumeric() == True:
            if ability2 == '0':
                return
            else:
                clear_line()
                cprint(color('Numbers are invalid!', 'error'))
                ability2 = input('Enter Ability #2: ')
        else:
            ability2 = ability2.title()
            if (ability2 == self.ability) or (ability2 == ''):
                ability2 = ''
            elif (ability2 not in self.ability_list):
                clear_line()
                cprint(color('This ability doesn\'t exist!','error'))
                self.set_Abitlity2()

        self.options[5] = f'Ability #2:         {ability2}'
        self.ability2 = ability2

    def set_Hidden_Ability(self):
        if self.ability == None:
            clear_line()
            cprint(color('Primary Ability must be set first!','error'))
            return
        ability3 = input('\nEnter Hidden Ability: ')
        while ability3.isnumeric() == True:
            if ability3 == '0':
                return
            else:
                clear_line()
                cprint(color('Numbers are invalid!', 'error'))
                ability3 = input('Enter Hidden Ability: ')
        else:
            ability3 = ability3.title()
            if (ability3 == self.ability) or (ability3 == self.ability2) or (ability3 == ''):
                ability3 = ''
            elif (ability3 not in self.ability_list):
                clear_line()
                cprint(color('This ability doesn\'t exist!','error'))
                self.set_Hidden_Ability()

        self.options[6] = f'Hidden Ability:     {ability3}'
        self.hidden_ability = ability3
        
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
            cprint(color('\nWould you like to enter stats for this Pokemon?'))
            selection = minput()
            if selection == b'0':
                return
            else:
                AS().update_stat(self.name)
                cprint(color('\nWould you like to add another Pokemon?'))
                selection = minput()
                if selection == b'0':
                    return

            self.clear_data()
            
    def clear_data(self):
        self.name,self.number,self.type1,self.type2 = None,None,None,None
        self.type1 = None
        self.type2 = None
        self.ability = None
        self.ability2 = None
        self.hidden_ability = None
        self.options = ['Name:', 
                        'Pokedex Number:', 
                        'Primary Type:', 
                        'Secondary Type:', 
                        'Ability:', 
                        'Ability #2:', 
                        'Hidden Ability:']

    def old_main(self):
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
            while (number not in self.job_map) and (number not in [b'8',b'0']) or(int(number) == version) :
                cprint('\n[bold red]Invalid Entry. Try Again![/bold red]')
                number = minput()
                print("\033[A\033[2K\033[A", end='', flush=True)
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
                        cprint(main_frame(options=self.options,index=self.index),justify='center')
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
    M = Add_Pokemon()
    M.main()