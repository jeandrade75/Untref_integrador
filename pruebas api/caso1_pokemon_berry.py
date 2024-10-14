import unittest
import requests

# Define la URL base
BASE_URL = "https://pokeapi.co/api/v2/berry/1/"

class TestPokeApi(unittest.TestCase):
    
    def setUp(self):
        # Hacer el GET a la API y guardar la respuesta en setUp
        self.response = requests.get(BASE_URL)
        self.data = self.response.json()

    def test_status_code(self):
        # Verificar que el request fue exitoso (status code 200)
        self.assertEqual(self.response.status_code, 200, f"Error: Status code {self.response.status_code}")

    def test_size(self):
        # Verificar que el size sea 20
        self.assertEqual(self.data["size"], 20, f"Error: Expected size 20, but got {self.data['size']}")
    
    def test_soil_dryness(self):
        # Verificar que el soil_dryness sea 15
        self.assertEqual(self.data["soil_dryness"], 15, f"Error: Expected soil_dryness 15, but got {self.data['soil_dryness']}")
    
    def test_firmness_name(self):
        # Verificar que el name en firmness sea soft
        self.assertEqual(self.data["firmness"]["name"], "soft", f"Error: Expected firmness name 'soft', but got {self.data['firmness']['name']}")

if __name__ == "__main__":
    unittest.main()

