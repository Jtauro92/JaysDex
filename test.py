import pandas as pd

df = pd.read_csv('dex.csv')

pd.options.display.max_rows = 1008



df2 = (df[['number','name','type1','type2']])
az_dex = df2.sort_values(by='name')
num_dex = df2.sort_values(by='number')
pokedex = num_dex.to_string(index=False)


#print(az_dex.to_string(index=False))
name = input('Enter Pokemon:\n').capitalize()
pokemon = df[df['name'] == name]

if pokemon['name'].item() == 'Venusaur':
    print('ok')
print(pokemon['sp.atk'].item())

class menu:

    def main_menu(self):
        print('''
              __________________
             |                  |
             | {}. Pokedex      |
             | {}. Select PKMN  |
             | {}. Compare PKMN |
             | (). Exit         |
             |__________________|
              ''')
        
    def pokedex_menu(self):
        print('''
              __________________
             |                  |
             | {}. Sort         |
             | {}. Group        |
             | {}. Select PKMN  |
             | {}. Compare PKMN |
             | (). Exit         |
             |__________________|
              ''')
    
    def sort_menu(self):
        print('''
              __________________
             |                  |
             | {}. By Name      |
             | {}. By Number    |
             | {}. By Stat      | 
             | {}. Exit         |
             | (). Main menu    |
             |__________________|
              ''')
        
    def sort_name_Menu(self):
        print('''
              __________________
             |                  |
             | {}. Ascending    |
             | {}. Descending   |
             |__________________|
              ''')
        
    def select_menu(self):
        print('''
              __________________
             |                  |
             | {}. Stats        |
             | {}. Forms        |
             | {}. Pokedex      |
             | (). Exit         |
             |__________________|
              ''')
#show menu
#1.View Pokedex
    #Shows the dataframe, with just the name and number columns
    #It then shows another menu
        #sort dex
            #Sort by name or number:
                #Ascending or descending
            #sort by type:
                #Select type
                #shows dex
                    #sort by stat
            #sort by stat:
                #Which stat:
                    #Ascending or descending
        #selct pokemon
        #compare pokemon
        #Main menu 
        #Exit

#2.Select Pokemon
    #The user enters a Pokemon name or number or 0 to quit.
        #If 0 it goes back to main menu
    #The dex shows you the pokemon number, name, type, and ability
        #The program then reads in the string from the corresponding file
        #named after the pokemon. This is the pokemon's summary.
        #If it evolves the summary will go even further to say:
            #If basic:
            #{Pokemon} evolves into:
            #A{Pokemon+1} number name and type
            #If {Pokemon+2} is stage 2
                #B{Pokemon+2} number name and type

            #If stage 1 
            #{Pokemon} evolves from:
            #A{Pokemon-1} number namer and type
            #{Pokemon} evolves into:
            #B{Pokemon+1} number name and type

            #If stage 2:
            #{Pokemon}evolves from:
            #A{Pokemon-1} number namer and type
            #B{Pokemon-2} number namer and type

    #Then another menu appears. The user can either select a pokemon or:
        #Stats
            #Shows the pokemon stats and shows bar graph using matplotlib.
        #Forms
            #Shows various forms
                #Select forms or '' to go back
        #Compare
            #Using the compare method from the comparison class
            #select a pokemon to compare or 0 to go back:
            #After entering a pokemon to compare yours to:
            #It shows both pokemon stats side by side and a bar gragph
            #appears layered on top of each other.
            #Select another pokemon to compare to or 0 to quit

        #Pokedex
        #Main menu
        #Exit

#3.Compare pokemon
        #Ask for two pokemon to compare
        #It shows the pokemon's stat's side by side and a bar graph