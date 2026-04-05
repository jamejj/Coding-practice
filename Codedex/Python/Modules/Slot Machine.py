# Write code below 💖
import random

symbols = ['🍒', ' 🍇', '🍉', '7️⃣']
results = random.choices(symbols, k=3)

print(f'{results[0]} | {results[1]} | {results[2]}')

if results[0] == '7️⃣' and results[1] == '7️⃣' and results[2] == '7️⃣':
    print('Jackpot! 💰')
else:
    print('Thanks for playing!')

'''
# Write code below 💖
import random

symbols = ['🍒', ' 🍇', '🍉', '7️⃣']
results = random.choices(symbols, k=3)

print(f'{results[0]} | {results[1]} | {results[2]}')


def play():
    while True:
        play = input('Y or N: ').upper()
        if play == 'Y':
            results = random.choices(symbols, k=3)
            print(f'{results[0]} | {results[1]} | {results[2]}')
            if results[0] == '7️⃣' and results[1] == '7️⃣' and results[2] == '7️⃣':
                print('Jackpot! 💰')
            else:
                print('Thanks for playing!')
        elif play == 'N':
            print('Bye')
            exit()

play()
'''



