# Lab 2 
# Create a script named greeting.py. Define a variable that contains the current hour (0-23). Display one of the greetings below based on the current hour
current_hour = int(input("Enter the current hour (0-23): "))


if 4 <= current_hour < 9:
    print("Good morning!")
elif 9 <= current_hour < 17:
    print("Good afternoon!")
elif 17 <= current_hour < 24:
    print("Good evening!")
elif 0 <= current_hour < 4:
    print("What are you doing up so late??")
else:
    print("Invalid hour")

if current_hour == 1:
    print("Time: 1:00AM")
elif current_hour == 2:
    print("Time: 2:00AM")
elif current_hour == 3:
    print("Time: 3:00AM")
elif current_hour == 4:
    print("Time: 4:00AM")
elif current_hour == 5:
    print("Time: 5:00AM")
elif current_hour == 6:
    print("Time: 6:00AM")
elif current_hour == 7:
    print("Time: 7:00AM")
elif current_hour == 8:
    print("Time: 8:00AM")
elif current_hour == 9:
    print("Time: 9:00AM")
elif current_hour == 10:
    print("Time: 10:00AM")
elif current_hour == 11:
    print("Time: 11:00AM")
elif current_hour == 12:
    print("Time: 12:00PM")
elif current_hour == 13:
    print("Time: 1:00PM")
elif current_hour == 14:
    print("Time: 2:00PM")
elif current_hour == 15:
    print("Time: 3:00PM")
elif current_hour == 16:
    print("Time: 4:00PM")
elif current_hour == 17:
    print("Time: 5:00PM")
elif current_hour == 18:
    print("Time: 6:00PM")
elif current_hour == 19:
    print("Time: 7:00PM")
elif current_hour == 20:
    print("Time: 8:00PM")
elif current_hour == 21:
    print("Time: 9:00PM")
elif current_hour == 22:
    print("Time: 10:00PM")
elif current_hour == 23:
    print("Time: 11:00PM")
else:
    print("Invalid hour")