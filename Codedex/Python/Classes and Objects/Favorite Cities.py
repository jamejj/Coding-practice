# Write code below 💖
class City:
  def __init__(self, name, country, population, landmarks):
    self.name = name
    self.country = country
    self.population = population
    self.landmarks = landmarks

warsaw = City('Warsaw','Poland',1860000,['Łazienki','Stare miasto'])
print(vars(warsaw))

athens = City('Athens','Greece',3500000,['Acropol','Partenon'])
print(vars(athens))