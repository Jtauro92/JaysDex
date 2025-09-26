"""Class to store information about a Pokemon."""
class Pokemon_Info:
    
    def __init__(self, name, number, type1, type2, ability1, ability2, hidden_ability, base_stats):
        self.name = name
        self.number = number
        self.type1 = type1
        self.type2 = type2
        self.ability1 = ability1
        self.ability2 = ability2
        self.hidden_ability = hidden_ability
        self.base_stats = base_stats  # base_stats should be a dictionary with keys: 'HP', 'Attack', 'Defense', 'Sp. Atk', 'Sp. Def', 'Speed'