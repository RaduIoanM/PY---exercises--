# Question 1) **************************************************************************

# Prompt the user to enter a time in the format 'HH:MM' e.g. 15:20

# If the time  is after 5:00 and less than 12:00 print "Good Morning"

# If the time is after 12:00 and less than 17:00 print "Good Afternoon"

# If the time is after 17:00 and less than 21:00 print "Good Evening"

# If the time is after 21:00 and less than 5:00 print "Good Night"
print("What`s the time? HH:MM ")
hour = input("First the hour ")
print("")
minutes = input("And the minutes ")
print("")

input_hour = int(hour)
input_minutes = int(minutes)

if input_hour >= 5 and input_hour <= 5:
    print("Good morning!")
elif input_hour >12 and input_hour <=17:
    print("Good Afternoon!")
elif input_hour >17 and input_hour <=21:
    print("Good Evening!")      
elif input_hour >21 and input_hour <=24:
    print("Good Night!")
else:
    print("Rush hour")    



