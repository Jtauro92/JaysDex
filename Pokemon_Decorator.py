from database import dex, ability_list, type_list


def name_check(func):
    def wrapper(self, name:str):
        if not (name.isnumeric()):
            name = name.capitalize()
            func(self, name)
    return wrapper

def number_check(func):
    def wrapper(self, number:int):
        if ((isinstance(number, int) or number.isnumeric()) and 
            (0<= int(number) <= 1025)):
            number = int(number)
            func(self, number)
    return wrapper

def type_check(func):
    def wrapper(self, type1: str):
        type1 = type1.upper()
        if type1 in type_list:
            func(self, type1)
    return wrapper

def ability_check(func):
    def wrapper(self, ability:str):
        ability = ability.capitalize()
        if ability in ability_list:
            func(self, ability)
    return wrapper
    


