# Write code below 💖
import random

def fortune():
    randInt = random.randint(0, 7)

    if randInt == 0:
        print('Don''t pursue happiness – create it.')
    elif randInt == 1:
        print('All things are difficult before they are easy.')
    elif randInt == 2:
        print('The early bird gets the worm, but the second mouse gets the cheese.')
    elif randInt == 3:
        print('Someone in your life needs a letter from you.')
    elif randInt == 4:
        print('Don''t just think. Act!')
    elif randInt == 5:
        print('Your heart will skip a beat.')
    elif randInt == 6:
        print('The fortune you search for is in another cookie.')
    else:
        print('Help! I''m being held prisoner in a Chinese bakery!')


