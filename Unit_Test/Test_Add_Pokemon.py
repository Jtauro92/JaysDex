from Pokemon import Pokemon as P


def test_validation():
   assert P().validate_pokemon(name='Bulbasaur') == True