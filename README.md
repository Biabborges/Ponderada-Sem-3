# Zoo API

## Funcionalidades

- Criação de animais com nome, espécie e nível de felicidade.
- Criação de recintos para abrigar os animais.
- Alimentação dos animais para aumentar sua felicidade.
- Recebimento de visitantes, onde a felicidade dos animais e a qualidade dos recintos influenciam o número de visitantes.

## Estrutura do Projeto

O projeto é dividido em três classes principais:

1. **Animal**: Representa um animal do zoológico, com atributos como nome, espécie e nível de felicidade. Possui o método `feed()` para alimentar o animal e aumentar sua felicidade.

2. **Enclosure**: Representa um recinto do zoológico, onde os animais são abrigados. Possui uma lista de animais e o método `add_animal()` para adicionar animais ao recinto.

3. **Zoo**: Representa o zoológico em si, contendo listas de animais e recintos. Possui métodos para criar animais e recintos, alimentar animais e calcular a felicidade total dos animais para receber visitantes.

## Testes Unitários

O projeto inclui testes unitários para garantir o correto funcionamento das funcionalidades da API. Os testes são executados automaticamente usando o módulo `unittest` do Python.

## Exemplo de Uso

```python
from zoo import Zoo, Animal, Enclosure

# Criar instâncias de animais e recintos
lion = Animal("Leão", "Felino", 50)
enclosure = Enclosure("Savanas")

# Criar instância do zoológico
zoo = Zoo()

# Adicionar animal ao zoológico
zoo.create_animal(lion)

# Adicionar recinto ao zoológico
zoo.create_enclosure(enclosure)

# Alimentar animal
zoo.feed_animal("Leão", 30)

# Receber visitantes e calcular felicidade total
total_happiness = zoo.receive_visitors()
print("Total de felicidade dos animais:", total_happiness)
```