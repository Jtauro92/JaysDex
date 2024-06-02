from view_pokemon import View_Pokemon as P

class add_stats(P):
    def __init__(self):
        P.__init__(self)
        self.name = ''

    def set_name(self,name):
        if name.isnumeric() == False:
            name = name.title()
            if name in self.name_list:
                return name
        else:
            name = int(name)
            if name in self.num_list:
                for pokemon in self.dex:
                    if name == pokemon[0]:
                        return pokemon[1]
            else:
                print('\nInvalid')
        
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
            print('\nInvalid')
            return None
    
    def update_stat(self,pokemon):
        stat = self.set_stat(input('Which stat: '))
        if stat is None:
            return
        else:
            value = self.set_value(input(f'{stat}: '))
            if value is None:
                return
            else:
                self.cursor.execute(f"UPDATE stats SET {stat} = {value} WHERE P_Name = '{pokemon}'")
                self.mydb.commit()
                print(f'\n{pokemon}\'s {stat} has been updated to {value}')

    def add_stats(self):
        self.name = self.set_name(input('Enter Pokemon Name: '))
        if self.name is None:
            return
        else:
            self.update_stat(self.name)
            

if __name__ == '__main__':
    print(add_stats().add_stats())