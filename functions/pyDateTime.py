from datetime import date

today = date.today()
print("Today's date:", today)

##################################################
print("\n#### Example 3: Date formatting ####\n")
##################################################

# dd/mm/YY    [d1 = 24/08/2021]
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)

# Textual month, day and year  : [d2 = August 24, 2021]
d2 = today.strftime("%B %d, %Y")
print("d2 =", d2)

# mm/dd/y   [d3 = 08/24/21]
d3 = today.strftime("%m/%d/%y")
print("d3 =", d3)

# Month abbreviation, day and year    [d4 = Aug-24-2021]
d4 = today.strftime("%b-%d-%Y")
print("d4 =", d4)

##################################################
print("\n#### Example 3: Get the current date and time ####\n")
##################################################
from datetime import datetime
# datetime object containing current date and time
now = datetime.now()

print("now =", now)

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time =", dt_string)

current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

for i in range(1,1000):
    pass

now = datetime.now().time() # time object
print("now =", now)
print("type(now) =", type(now))


##################################################
print("\n#### Example 4: Current time of a timezone ####\n")
##################################################
print("\n\n")
from datetime import datetime
import pytz

tz_NY = pytz.timezone('America/New_York')
datetime_NY = datetime.now(tz_NY)
print("NY time:", datetime_NY.strftime("%H:%M:%S"))