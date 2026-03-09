# Write code below 💖
import random

question = input('Ask your question: ')
magicBall = random.randint(1, 9)

if(magicBall==1):
  print('Question: ' + question)
  print('Magic 8 Ball: Yes - definitely.')
elif(magicBall==2):
  print('Question: ' + question)
  print('Magic 8 Ball: It is decidedly so.')
elif(magicBall==3):
  print('Question: ' + question)
  print('Magic 8 Ball: Without a doubt.')
elif(magicBall==4):
  print('Question: ' + question)
  print('Magic 8 Ball: Reply hazy, try again.')
elif(magicBall==5):
  print('Question: ' + question)
  print('Magic 8 Ball: Ask again later.')
elif(magicBall==6):
  print('Question: ' + question)
  print('Magic 8 Ball: Better not tell you now.')
elif(magicBall==7):
  print('Question: ' + question)
  print('Magic 8 Ball: My sources say no.')
elif(magicBall==8):
  print('Question: ' + question)
  print('Magic 8 Ball: Outlook not so good.')
else:
  print('Question: ' + question)
  print('Magic 8 Ball: Very doubtful.')
