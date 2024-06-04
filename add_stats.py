from view_pokemon import View_Pokemon as P

class add_stats(P):
    def __init__(self):
        P.__init__(self)
        self.name = ''
        
    def set_stat(self,stat):
        if not stat.isnumeric():
            stat = stat.lower()
            if stat in self.attributes[8:]:
                return stat
        else:
            print('\nInvalid')
            return None
    
    def set_value(self,value):
        if value.isnumeric():
            return value
        else:
            if value == '':
                return 0
            else:
                print('\nInvalid')
                return None
    
    def update_stat(self,pokemon):
        print(f'''\n{pokemon}'s current stats''')
        self.view_stats(pokemon)
        stat = self.set_stat(input('\nWhich stat: '))
        while stat != None:
            value = self.set_value(input(f'{stat}: '))
            while value is None:
                value = self.set_value(input(f'{stat}: '))
            else:
                self.cursor.execute(f"UPDATE stats SET {stat} = {value} WHERE P_Name = '{pokemon}'")
                print(f'\n{pokemon}\'s {stat} has been updated to {value}\n')
                stat = self.set_stat(input('Which stat: '))
        else:
            print(f'''\n{pokemon}'s updated stats''')
            self.view_stats(pokemon)
            return

    def add_stats(self):
        self.name = self.set_name(input('Enter Pokemon Name: '))
        while self.name != None:
            self.update_stat(self.name)
            self.name = self.set_name(input('\nEnter Pokemon Name: '))
        else:
            return

if __name__ == '__main__':
    add_stats().add_stats()