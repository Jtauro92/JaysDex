from database import type_list

"""Class to store information about a Pokemon."""
class Pokemon_Info:
    def __init__(self, name: str = 'Unknown', number: int = 0, 
                 type1: str = 'Normal', type2: str = 'None', 
                 ability1: str = 'None', ability2: str = 'None', 
                 hidden_ability: str = 'None'):
        self.name = name
        self.number = number
        self.type1 = type1
        self.type2 = type2
        self.ability1 = ability1
        self.ability2 = ability2
        self.hidden_ability = hidden_ability
        
    # String representation of the Pokemon_Info object
    def __str__(self):
        return (f"Name: {self.name} \nNumber: {self.number}"
                +f"\nType1: {self.type1} \nType2: {self.type2}"
                +f"\nAbility1: {self.ability1} \nAbility2: {self.ability2}"
                +f"\nHidden Ability: {self.hidden_ability}")

    # Representation for debugging
    def __repr__(self):
        return (f"Pokemon_Info(name={self.name}, number={self.number}, "
                f"type1={self.type1}, type2={self.type2}, "
                f"ability1={self.ability1}, ability2={self.ability2}, "
                f"hidden_ability={self.hidden_ability})")
        
    # Getters and Setters
    def get_name(self) -> str:
        return self.name
    
    def set_name(self,  name: str) -> bool:
        if self.validate_string(name, "Name") is False:
            return False
        else:
            self.name = name.title()
            print(f"Name set to: {self.name}")
            return True


    def get_number(self) -> int:
        return self.number
    
    def set_number(self, number: int) -> bool:
        try:
            number = int(number)
            if number < 0:
                print("Error: Number cannot be negative.")
            else:
                self.number = number
                print(f"Number set to: {self.number}")
                return True
        except ValueError:
            print("Error: Number must be an integer.")

        return False
    
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
    pikachu = Pokemon_Info()

    while pikachu.set_type1(input("Type? ")) == False:
        print(pikachu.type1)
        print("Please try again.\n")
    print(pikachu.get_type1())
    
    