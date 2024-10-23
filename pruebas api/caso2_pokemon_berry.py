import requests
import unittest

class TestPokeApiBerry2(unittest.TestCase):

    def setUp(self) -> None:
        self.url = 'https://pokeapi.co/api/v2/berry/2'

    def test_berry_data(self):
        # Hacer la solicitud GET
        response = requests.get(self.url)
        
        # Verificar que la solicitud sea exitosa
        self.assertEqual(response.status_code, 200)
        
        # Convertir la respuesta a JSON
        berry_data = response.json()
        
        # Verificar que en firmness, el nombre (name) sea "super-hard"
        self.assertEqual(berry_data['firmness']['name'], 'super-hard')
        
        # Verificar que el tamaño (size) sea mayor a 20
        self.assertGreater(berry_data['size'], 20)
        
        # Verificar que soil_dryness sea 15
        self.assertEqual(berry_data['soil_dryness'], 15)

if __name__ == '__main__':
    unittest.main()

