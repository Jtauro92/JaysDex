from view_pokemon import View_Pokemon as P
from view_pokemon import color as C

class add_stats(P):
    def __init__(self):
        P.__init__(self)
        self.name = ''
        
    def set_stat(self,stat):
        while stat.isnumeric() == True:
            print(C().color_string('error','\nNumbers are invalid!\n'))
            stat = input('Enter Stat: ')
        else:
            stat = stat.lower()
            if stat.upper() == 'N':
                return None
            if (stat not in self.attributes[8:]):
                print(C().color_string('error','\nThis stat doesn\'t exist!\n'))
                stat = self.set_stat(input('Enter Stat: '))

        return stat
    
    def set_value(self,stat,value):
        while value.isnumeric() == False:
            if value.upper() == 'N':
                print(C().color_string('error','\nYou have chosen to cancel!\n'))
                return
            if value == '':
                return 0
            else: 
                print(C().color_string('error','\nOnly numbers are valid!\n'))
                value = input(f'{stat}: ')
        else:
            return value
        
    def update_stat(self,pokemon):
        print(f'''\n{pokemon}'s current stats''')
        self.view_stats(pokemon)
        stat = self.set_stat(input('\nWhich stat: '))
        while stat != None:
            value = self.set_value(stat,input(f'{stat}: '))
            while value is None:
                return
            else:
                self.cursor.execute(f"UPDATE stats SET {stat} = {value} WHERE P_Name = '{pokemon}'")
                print(f'\n{pokemon}\'s {stat} has been updated to {value}\n')
                stat = self.set_stat(input('\nWhich stat: '))
        else:
            print(f'''\n{pokemon}'s updated stats''')
            self.view_stats(pokemon)
            return

    def add_stats(self):
        self.name = self.set_name(input('Enter Pokemon Name: '))
        if self.name == 'N':
            return
        else:
            self.update_stat(self.name)


if __name__ == '__main__':
    add_stats().add_stats()