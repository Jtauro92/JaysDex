from database import type_list

"""Class to store information about a Pokemon."""
class Pokemon_Info:
    def __init__(self, name: str = 'Unknown', number: int = 0, 
                 type1: str = 'Normal', type2: str = 'None', 
                 ability1: str = 'None', ability2: str = 'None', 
                 hidden_ability: str = 'None'):
        self._name = name
        self._number = number
        self._type1 = type1
        self._type2 = type2
        self._ability1 = ability1
        self._ability2 = ability2
        self._hidden_ability = hidden_ability
        
    # String representation of the Pokemon_Info object
    def __str__(self):
        return (f"Name: {self._name} \nNumber: {self._number}"
                +f"\nType1: {self._type1} \nType2: {self._type2}"
                +f"\nAbility1: {self._ability1} \nAbility2: {self._ability2}"
                +f"\nHidden Ability: {self._hidden_ability}")

    # Representation for debugging
    def __repr__(self):
        return (f"Pokemon_Info(name={self._name}, number={self._number}, "
                f"type1={self._type1}, type2={self._type2}, "
                f"ability1={self._ability1}, ability2={self._ability2}, "
                f"hidden_ability={self._hidden_ability})")
        
    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, name: str) -> None:
        if self.validate_string(name, "Name"):
            self._name = name.title()
            print(f"Name set to: {self._name}")
        else:
            print("Invalid name.")

    @property
    def number(self) -> int:
        return self._number
    
    @number.setter
    def number(self, number: int) -> None:
        try:
            number = int(number)
            if 0 < number <= 1025:
                self._number = number
            else:
                raise ValueError("Number must be between 1 and 1025.")
        except ValueError as e:
            print(f"Error: {e}")
        

    
    def get_type1(self) -> str:
        return self.type1
    
    def set_type1(self, value: str) -> bool:
        value = value.upper()
        if  self.set_type(value, "Type1"):
            self.type1 = value
            print(f"Type1 set to: {self.type1}")
            return True
        else:
            return False
        
    # Validation of Types
    def set_type(self, value: str, field_name: str) -> bool:
        if self.validate_string(value, field_name):
            if self.validate_type(value):
                return True
            else:
                print(f"Error: {field_name} must be one of the following types: {', '.join(type_list)}") 
        return False
    
    # Helper method for string validation
    def validate_string(self, value: str, field_name: str) -> bool:
        value = value.strip()
        if value.isnumeric():
            print(f"Error: {field_name} cannot be numeric.")
        elif value == "":
            print(f"Error: {field_name} cannot be empty.")
        else:
            return True
        
        return False

    
    #Helper method for type validation
    def validate_type(self, value: str) -> bool:
        if value in type_list:
            return True
        else:
            return False
        
            
            
    
    # behaviors
    def display_info(self):
        print(self)

if __name__ == "__main__":
    # Example usage
    pokemon = Pokemon_Info()
    pokemon.number = 1026
    print(pokemon.number)

    
    
    