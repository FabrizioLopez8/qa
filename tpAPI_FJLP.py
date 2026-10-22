import unittest
import requests

class PokeApiTest(unittest.TestCase):

  def test_returnsCode200(self):
    response = requests.get("https://pokeapi.co/api/v2/pokemon/")
    self.assertEqual(200, response.status_code)

  def test_getPokemonWartortleByID(self):
    response = requests.get("https://pokeapi.co/api/v2/pokemon/8")
    pokemon_data = response.json()
    assert pokemon_data["name"] == "wartortle"

  def test_getTypePokemonCount(self):
    response = requests.get("https://pokeapi.co/api/v2/type/3")
    type_data = response.json()
    print(type_data["pokemon"].count)
    assert len(type_data["pokemon"]) == 154


unittest.main(defaultTest='PokeApiTest', argv=[''], verbosity=2, exit=False)