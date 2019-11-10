# Work or Sleep in?
# Prompt the user for a day of the week just
#  like the previous problem. But this time,
#  print "Go to work" if it's a work day and
#  "Sleep in" if it's a weekend day. 
# Example session:

# $ python work_or_sleep_in.py
# Day (0-6)? 5
# Go to work
# $ python work_or_sleep_in.py
# Day (0-6)? 6
# Sleep in

day = int(input("Day (0-6)? "))

if day == 1:
  print("Monday \nGo to Work!")
elif day == 2:
  print("Tuesday \nGo to Work!")
elif day == 3:
  print("Wednesday \nGo to Work!")
elif day == 4:
  print("Thursday \nGo to Work!")
elif day == 5:
  print("Friday \nGo to Work!")
elif day == 6:
  print("Saturday \nSleep in!")
elif day == 0:
  print("Sunday \n Sleep in!")
else:
  print("Not a valid entry.")
