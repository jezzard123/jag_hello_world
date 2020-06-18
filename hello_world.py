'''
My first code.

@author JGraham
created 25/06/19
'''
import datetime
current_time = datetime.datetime.now()


=======
if current_time.hour < 6:
    print("Go back to bed")
elif current_time.hour < 12:
    print("Good morning, it is time for a coffee!")
elif current_time.hour < 18:
    print("Good afternoon, it is time for a tea!")
else:
    print("Good evening")

print('And what a lovely day it is indeed.')

if current_time.year == 2020:
    print("Well, aside from (insert your favorite current global crisis here).")

# Nice code!
