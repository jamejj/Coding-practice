import datetime
import bday_messages

today = datetime.date.today()

next_birthday = datetime.date(2026,4,3)

time_until_birthday = next_birthday - today

if today == next_birthday:
    print(bday_messages.random_message)
else:
    print(f'My next birthday is {time_until_birthday} days away!')




