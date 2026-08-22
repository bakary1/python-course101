######################################
## Day 14 - Python Datetime function
######################################

from datetime import datetime

# Examples

# Getting date information
now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
timestamp = now.timestamp()

# Formatting date output with strftime
now = datetime.now()
t = now.strftime("%H:%M:%S")
print(f"time: {t}")
time_one = now.strftime("%d-%m-%Y, %H:%M:%S")
print(time_one)

# String to Time Using strptime
date_string = "5 December, 2019"
date_object = datetime.strptime(date_string, "%d %B, %Y")
print(date_string)
print(date_object)

# Using date from datetime
from datetime import date

d = date(2026, 1, 1)
print(d)
print(f"Current date: {d.today()}")
today = d.today()
print(f"Current year: {today.year}")
print(f"Current month {today.month}")
print(f"Current day {today.day}")

# Time Objects to Represent Time
from datetime import time

a = time()
print(f"a: {a}")
b = time(10, 30, 15)
print(b)
c = time(11, 30, 15, 2321)
print(c)


# Difference Between Two Points in Time Using timedelta
from datetime import timedelta

t1 = timedelta(weeks=12, days=10, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print(f"t3: {t3}")

# Exercises: Level 1

# 1. Get the current day, month, year, hour, minute and timestamp from datetime module
from datetime import datetime

now = datetime.now()
print(f"Day: {now.day}")
print(f"Month: {now.month}")
print(f"year: {now.year}")
print(f"Hour: {now.hour}")
print(f"Minute: {now.minute}")
print(f"Time: {now.time()}")

# 2. Format the current date using this format: "%m/%d/%Y, %H:%M:%S")
formatted_date = now.strftime("%m/%d/%Y, %H:%M:%S")
print(formatted_date)

# 3. Today is 5 December, 2019. Change this time string to time.
date_string = "5 December, 2019"
date_object = datetime.strptime(date_string, "%d %B, %Y")
print(date_object)

# 4. Calculate the time difference between now and new year.
today = date(2026, 8, 22)
new_years = date(2027, 1, 1)
print(f"Difference: {new_years - today}")

# 5. Calculate the time difference between 1 January 1970 and now.
t = datetime.now().date()
b = date(1970, 1, 1)
print(f"Difference: {t - b}")
