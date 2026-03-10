tries = 0
guess = 0

while (guess != 6 and tries < 5):
  guess = int(input("Guess the number:  "))
  tries+=1
if(tries==5):
  print('Not this time')
else:
  print("You got it!")