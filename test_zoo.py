import unittest
from zoo_classes import Zoo, Animal, Enclosure

class TestZoo(unittest.TestCase):
    def setUp(self):
        # Inicializa um objeto Zoo para testes.
        self.zoo = Zoo()

    def test_create_animal(self):
        # Testa a criação de um animal e adicioná-lo ao zoológico.
        animal = Animal("Leão", "Felino", 50)
        self.zoo.create_animal(animal)
        self.assertEqual(len(self.zoo.animals), 1)

    def test_create_enclosure(self):
        # Testa a criação de um recinto e adicioná-lo ao zoológico.
        enclosure = Enclosure("Savana")
        self.zoo.create_enclosure(enclosure)
        self.assertEqual(len(self.zoo.enclosures), 1)

    def test_feed_animal(self):
        # Testa a alimentação de um animal e verifica o nível de felicidade.
        animal = Animal("Leão", "Felino", 50)
        self.zoo.create_animal(animal)
        self.zoo.feed_animal("Leão", 30)
        self.assertEqual(animal.happiness, 80)

    def test_receive_visitors(self):
        # Testa o recebimento de visitantes no zoológico e verifica sua experiência.
        animal = Animal("Leão", "Felino", 80)
        enclosure = Enclosure("Savanas")
        enclosure.add_animal(animal)
        self.zoo.create_enclosure(enclosure)
        self.assertEqual(self.zoo.receive_visitors(), 80)

if __name__ == '__main__':
    unittest.main()
