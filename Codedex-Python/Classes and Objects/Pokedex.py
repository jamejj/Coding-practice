# Write code below 💖
class Pokemon:
  def __init__(self, entry, name, types, description, is_caught):
    self.entry = entry
    self.name = name
    self.types = types
    self.description = description
    self.is_caught = is_caught

  def speak(self):
    print(f'{self.name} {self.name}')

  def display_details(self):
    print(f'Entry number: {self.entry}')
    print(f'Name: {self.name}')
    print(f'Type: {self.types}')
    print(f'Description: {self.description}')
    if self.is_caught == True:
      print(f'{self.name} has arleady been caught')


tepig = Pokemon(498,'Tepig',['Fire'],'Tepig is a small, quadrupedal Fire-type piglet Pokémon introduced in Generation V, known as the "Fire Pig Pokémon"',True)
tepig.speak()
tepig.display_details()

print()

rayquaza = Pokemon(384,'Rayquaza',['Dragon','Flying'],'Rayquaza is a Dragon/Flying type Pokémon introduced in Generation 3.',False)
rayquaza.speak()
rayquaza.display_details()

print()

abra = Pokemon(63,'Abra',['Psychic'],'Abra is a Psychic type Pokémon introduced in Generation 1.',True)
abra.speak()
abra.display_details()