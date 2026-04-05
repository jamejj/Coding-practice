# Write code below 💖
items_list = ['🍔 Cheeseburger','🍟 Fries','🥤 Soda','🍦 Ice Cream','🍪 Cookie']

def welcome():
  print(f'Welcome, please enter a number of your meal: {items_list}')

welcome()

meal_number = int(input('Meal number: '))

def get_item(item_number):

  if item_number == 1:
    return items_list[0]
  elif item_number == 2:
    return items_list[1]
  elif item_number == 3:
    return items_list[2]
  elif item_number == 4:
    return items_list[3]
  elif item_number == 5:
    return items_list[4]
  else:
    return 'This item not exist'

print(get_item(meal_number))
