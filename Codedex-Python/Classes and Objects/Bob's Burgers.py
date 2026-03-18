# Write code below 💖
class Restaurant:
  name = ''
  category = ''
  rating = 0.0
  delivery = True

bobs_burger = Restaurant()
bobs_burger.name = 'Bob\'s Burgers'
bobs_burger.category = 'American Diner'
bobs_burger.rating = 4.7
bobs_burger.delivery = False
print(vars(bobs_burger))

mc_donalds = Restaurant()
mc_donalds.name = 'McDonald''s'
mc_donalds.category = 'Fast food'
mc_donalds.rating = 3.6
mc_donalds.delivery = True
print(vars(mc_donalds))

dominos_pizza = Restaurant()
dominos_pizza.name = 'Domino''s pizza'
dominos_pizza.category = 'Fast food'
dominos_pizza.rating = 3.9
dominos_pizza.delivery = True
print(vars(dominos_pizza))