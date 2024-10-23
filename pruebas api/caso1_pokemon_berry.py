import requests
import unittest

class TestPokeApi(unittest.TestCase):

    def setUp(self) -> None:
        self.url = 'https://pokeapi.co/api/v2/berry/1'

    def test_berry_data(self):
        # Hacer la petición GET
        response = requests.get(self.url)
        
        # Verificar que la solicitud sea exitosa
        self.assertEqual(response.status_code, 200)
        
        # Convertir la respuesta a JSON
        berry_data = response.json()
        
        # Verificar que el tamaño (size) sea 20
        self.assertEqual(berry_data['size'], 20)
        
        # Verificar que soil_dryness sea 15
        self.assertEqual(berry_data['soil_dryness'], 15)
        
        # Verificar que en firmness, el nombre (name) sea "soft"
        self.assertEqual(berry_data['firmness']['name'], 'soft')

if __name__ == '__main__':
    unittest.main()


