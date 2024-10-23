import requests
import unittest

class TestPokeApiPikachu(unittest.TestCase):

    def setUp(self) -> None:
        self.url = 'https://pokeapi.co/api/v2/pokemon/pikachu/'

    def test_pikachu_data(self):
        # Hacer la solicitud GET
        response = requests.get(self.url)
        
        # Verificar que la solicitud sea exitosa
        self.assertEqual(response.status_code, 200)
        
        # Convertir la respuesta a JSON
        pikachu_data = response.json()
        
        # Verificar que la experiencia base (base_experience) sea mayor a 10 y menor a 1000
        base_experience = pikachu_data['base_experience']
        self.assertGreater(base_experience, 10)
        self.assertLess(base_experience, 1000)
        
        # Verificar que uno de sus tipos sea "electric"
        types = [t['type']['name'] for t in pikachu_data['types']]
        self.assertIn('electric', types)

if __name__ == '__main__':
    unittest.main()


