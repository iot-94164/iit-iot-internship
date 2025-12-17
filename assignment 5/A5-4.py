import datetime

now = datetime.datetime.now()

print("Current Date and Time:", now)

day = now.strftime("%A")
print("Day of the Week:", day)
