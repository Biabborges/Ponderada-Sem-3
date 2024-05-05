class Animal:
    def __init__(self, name, species, happiness):
        # Inicializa um animal com seu nome, espécie e nível inicial de felicidade.
        self.name = name
        self.species = species
        self.happiness = happiness

    def feed(self, amount):
        # Aumenta o nível de felicidade do animal pela quantidade fornecida.
        self.happiness += amount

class Enclosure:
    def __init__(self, name):
        # Inicializa um recinto com um nome e uma lista vazia de animais.
        self.name = name
        self.animals = []

    def add_animal(self, animal):
        # Adiciona um animal ao recinto.
        self.animals.append(animal)

class Zoo:
    def __init__(self):
        # Inicializa um zoológico com listas vazias para animais e recintos.
        self.animals = []
        self.enclosures = []

    def create_animal(self, animal):
        # Adiciona um animal ao zoológico.
        self.animals.append(animal)

    def create_enclosure(self, enclosure):
        # Adiciona um recinto ao zoológico.
        self.enclosures.append(enclosure)

    def feed_animal(self, name, amount):
        # Alimenta um animal específico no zoológico e aumenta seu nível de felicidade.
        for animal in self.animals:
            if animal.name == name:
                animal.feed(amount)

    def receive_visitors(self):
        # Calcula a felicidade total de todos os animais em todos os recintos.
        total_happiness = 0
        for enclosure in self.enclosures:
            for animal in enclosure.animals:
                total_happiness += animal.happiness
        return total_happiness
