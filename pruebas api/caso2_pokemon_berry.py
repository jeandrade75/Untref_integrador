import unittest
import requests

# Definir las URLs base
URL_BERRY_1 = "https://pokeapi.co/api/v2/berry/1/"
URL_BERRY_2 = "https://pokeapi.co/api/v2/berry/2/"

class TestPokeApiBerry2(unittest.TestCase):
    
    def setUp(self):
        # Hacer GET requests para berry/1 y berry/2 y guardar las respuestas
        self.response_berry_1 = requests.get(URL_BERRY_1)
        self.data_berry_1 = self.response_berry_1.json()

        self.response_berry_2 = requests.get(URL_BERRY_2)
        self.data_berry_2 = self.response_berry_2.json()

    # Caso 2: Test para berry/2
    def test_berry_2_status_code(self):
        self.assertEqual(self.response_berry_2.status_code, 200, f"Error: Status code {self.response_berry_2.status_code}")
    
    def test_berry_2_firmness_name(self):
        self.assertEqual(self.data_berry_2["firmness"]["name"], "super-hard", f"Error: Expected firmness name 'super-hard', but got {self.data_berry_2['firmness']['name']}")
    
    def test_berry_2_size(self):
        # Verificar que el size de berry/2 sea mayor que el de berry/1
        self.assertGreater(self.data_berry_2["size"], self.data_berry_1["size"], f"Error: Expected berry/2 size to be greater than berry/1, but got {self.data_berry_2['size']} <= {self.data_berry_1['size']}")
    
    def test_berry_2_soil_dryness(self):
        # Verificar que el soil_dryness de berry/2 sea igual al de berry/1
        self.assertEqual(self.data_berry_2["soil_dryness"], self.data_berry_1["soil_dryness"], f"Error: Expected soil_dryness to be the same as berry/1, but got {self.data_berry_2['soil_dryness']}")

if __name__ == "__main__":
    unittest.main()
