'''
My first code. 

@author JGraham
created 25/06/19
'''
import datetime
current_time = datetime.datetime.now()


if current_time.hour < 12:
    print("Good morning, Coffee Time")
elif current_time.hour < 13:
    print("Wow, Lunch")
elif current_time.hour < 18:
    print("Good afternoon")
else:
    print("Good evening, enjoy your chill time")
