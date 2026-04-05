# Write code below 💖
gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

print('Q1) Do you like Dawn or Dust? ')
print('    1) Dawn')
print('    2) Dusk')

answer1 = int(input())

if(answer1==1):
  gryffindor+=1
  ravenclaw+=1
elif(answer1==2):
  hufflepuff+=1
  slytherin+=1
else:
  print('Wrong input.')



print('Q2) When I’m dead, I want people to remember me as: ')
print('   1) The Good')
print('   2) The Great')
print('   3) The Wise')
print('   4) The Bold')

answer2 = int(input())

if(answer2==1):
  hufflepuff+=2
elif(answer2==2):
  slytherin+=2
elif(answer2==3):
  ravenclaw+=2
elif(answer2==4):
  gryffindor+=2
else:
  print('Wrong input.')

print('Q3) Which kind of instrument most pleases your ear?')
print('   1) The violin')
print('   2) The trumpet')
print('   3) The piano')
print('   4) The drum')

answer3 = int(input())

if(answer3==1):
  slytherin+=4
elif(answer3==2):
  hufflepuff+=4
elif(answer3==3):
  ravenclaw+=4
elif(answer4==4):
  gryffindor+=4
else:
  print('Wrong input.')

print('🦁 Gryffindor: ' + str(gryffindor))
print('🦅 Ravenclaw: ' + str(ravenclaw))
print('🦡 Hufflepuff: ' + str(hufflepuff))
print('🐍 Slytherin: ' + str(slytherin))



