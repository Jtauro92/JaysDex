from Pokemon import Pokemon as P
import csv

class add_stats(P):
    def __init__(self):
        P.__init__(self)
        self.name = ''
        
 
    def validate_Name(self, name):
        if (name == ('N')) or (name in self.name_list):
            self.name = name
        else:
            self.name = True
            print('\nInvalid')
    


    def adjust_stat(self,name):
        bag = []
        num = None
        stat = None
        with open('dex.csv','r',newline='')as dex:
            pokedex = csv.DictReader(dex)
            for pokemon in pokedex:
                if pokemon['name'] == name:
                    print('\n(Current)')
                    self.show_stats(pokemon)
            
                    while stat == None:
                        stat = input('\nWhich stat? (N to quit)\n')
                        if stat.lower() in self.attributes[5:]:
                    
                            while num == None:
                                num = input(f'\n{stat} or N to quit: ').upper()
                                if num != 'N':
                                    try:
                                        num = int(num)
                                        if 0 < num <= 600:
                                            pokemon[stat] = num

    
                                        else:
                                            print('\nInvalid')
                                            num = None
                                            
                                    except ValueError:
                                        print("\nInvalid")
                                        num = None
                            stat = None
                            num = None
                        elif stat.lower() == 'n':
                            pass
                          
                        else:
                            print('\nInvalid\n')
                            stat = None
                            num = None
                    print('\n'+'+'*45,"\n(Updated)")
                    self.show_stats(pokemon)
                bag.append(pokemon)
            with open('dex.csv','w',newline='') as dex:
                writer = csv.DictWriter(dex, fieldnames=self.attributes)
                writer.writeheader()
                writer.writerows(bag)
  
    def add_stat(self):
        self.validate_Name(input('\nChange which Pokemon\'s stats? (N to quit)\n').capitalize())

        while self.name != (None):
            if self.name != 'N':
                self.adjust_stat(self.name)
                print('\n', end=('='*45))
                self.validate_Name(input('\n\nChange which Pokemon\'s stats? (N to quit)\n').capitalize())
            elif self.name == True:
                self.validate_Name(input('\n\nChange which Pokemon\'s stats? (N to quit)\n').capitalize())
            elif self.name == 'N':
                self.name = None
            

if __name__ == '__main__':
    add_stats().add_stat()