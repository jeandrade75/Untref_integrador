import unittest
import requests

# Definir la URL base para Pikachu
URL_PIKACHU = "https://pokeapi.co/api/v2/pokemon/pikachu/"

class TestPokeApiPikachu(unittest.TestCase):
    
    def setUp(self):
        # Hacer GET request para pikachu y guardar la respuesta
        self.response_pikachu = requests.get(URL_PIKACHU)
        self.data_pikachu = self.response_pikachu.json()

    def test_pikachu_status_code(self):
        # Verificar que la API responda con un código 200 para pikachu
        self.assertEqual(self.response_pikachu.status_code, 200, f"Error: Status code {self.response_pikachu.status_code}")
    
    def test_pikachu_base_experience(self):
        # Verificar que la experiencia base de pikachu sea mayor a 10 y menor a 1000
        base_experience = self.data_pikachu["base_experience"]
        self.assertGreater(base_experience, 10, f"Error: Expected base experience > 10, but got {base_experience}")
        self.assertLess(base_experience, 1000, f"Error: Expected base experience < 1000, but got {base_experience}")
    
    def test_pikachu_type(self):
        # Verificar que el tipo de pikachu sea "electric"
        types = [t["type"]["name"] for t in self.data_pikachu["types"]]
        self.assertIn("electric", types, f"Error: Expected type 'electric', but got {types}")

if __name__ == "__main__":
    unittest.main()

