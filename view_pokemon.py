from Pokemon import Pokemon as P

class View_Pokemon(P):
    def __init__(self):
        P.__init__(self)
        self.name = None

    def validate_Name(self, name):
        try:
            self.name = int(name)
            if (self.name  not in self.num_list) or (not(0 < self.name <= 1008)):
                print('\nInvalid')
                self.name = None    
            else:
                self.name = str(name)
     
        except ValueError:
            if (name == 'N') or (name in self.name_list):
                self.name = name
    
            else:
                print("\nInvalid")

    def view_pokemon(self):
        while self.name == None:
            self.validate_Name(input("\nWhich Pokemon? (N to quit)\n").capitalize())
            if self.name != 'N':
                for pokemon in self.dex:
                    if (self.name == pokemon['name']) or (self.name == pokemon['number']):
                        self.show_stats(pokemon)
                        self.name = None


 
    

if __name__ == '__main__':
    View_Pokemon().view_pokemon()