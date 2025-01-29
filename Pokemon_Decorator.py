from database import dex, ability_list, type_list

class ValidName:
    def __init__(self):
        self.name = None
        
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        try:
            value = value.title()
            instance.__dict__[self.name] = value if any(value == pokemon['Name'] for pokemon in dex) else 'Default'
            in_dex = True
        except AttributeError:
            instance.__dict__[self.name] = 'Default'
            in_dex = False
        in_dex = False

class ValidNumber:
    def __init__(self):
        self.number = None
        
    def __set_name__(self, owner, number):
        self.number = number

    def __get__(self, instance, owner):
        return instance.__dict__[self.number]
    
    def __set__(self, instance, value):
        try:
            value = int(value)
            instance.__dict__[self.number] = value if 0 <= value <= 1025 else 0
        except ValueError:
            instance.__dict__[self.number] = 0
            
class ValidType:
    def __init__(self):
        self.type = None
        
    def __set_name__(self, owner, type):
        self.type = type
    
    def __get__(self, instance, owner):
        return instance.__dict__[self.type]
    
    def __set__(self, instance, value):
        try:
            value = value.upper()
            
            instance.__dict__[self.type] = value if any(value == t for t in type_list) else 'Normal'
        except AttributeError:
            instance.__dict__[self.type] = 'Normal'
            
class ValidType2(ValidType):
    def __set__(self, instance, value):
        try:
            value = value.upper()
            if any(value == t for t in type_list) and value != instance.type1:
                instance.__dict__[self.type] = value 
            else:
                instance.__dict__[self.type] = None
        except AttributeError:
            instance.__dict__[self.type] = None
            
class ValidAbility:
    def __init__(self):
        self.ability = None
        
    def __set_name__(self, owner, ability):
        self.ability = ability
        
    def __get__(self, instance, owner):
        return instance.__dict__[self.ability]
    
    def __set__(self, instance, value):
        try:
            value = value.title()
            instance.__dict__[self.ability] = value if any(value == a for a in ability_list) else 'Sturdy'
        except AttributeError:
            instance.__dict__[self.ability] = 'Sturdy'
            
class ValidAbility2(ValidAbility):
    def __set__(self, instance, value):
        try:
            value = value.title()
            if (any(value == a for a in ability_list)) and (value != instance.ability):
                instance.__dict__[self.ability] = value
            else:
                instance.__dict__[self.ability] = None
        except AttributeError:
            instance.__dict__[self.ability] = None
            
class ValidHiddenAbility(ValidAbility):
    def __set__(self, instance, value):
        try:
            value = value.title()
            if (any(value == a for a in ability_list)) and (value not in [instance.ability, instance.ability2]):
                instance.__dict__[self.ability] = value
            else:
                instance.__dict__[self.ability] = None
        except AttributeError:
            instance.__dict__[self.ability] = None
            
if __name__ == '__main__':
    v = ValidName()
    v.name = 0
    print(v)