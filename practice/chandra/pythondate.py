from datetime import date, datetime
import pytz

print("\n\n date --------------")
today = date.today()
print("Today's date:", today)
print(type(today))

print(today.strftime('%a - %d-%b,%Y'))

# strftime() - it format our datetime object

dob = '26June1998'     #DDMMYYYY
print(type(dob))
# print(type(eval(dob)))
print("------***********----------")
# print(dob.strftime('%a - %d-%b,%Y ')) (input is datetime : output is datetime)
# strptime - string parse to datetime object. (input is string : output is datetime)

new_dob = datetime.strptime(dob, '%d%B%Y' )
print(new_dob.strftime('%a - %d-%b,%Y '))


# print("\n\n datetime ----------")
# today = datetime.now()
# print("Today's date:", today)
# print(type(today))


# print("\n\n datetime ---------- timezone")
# tz_NY = pytz.timezone('America/New_York')
# datetime_NY = datetime.now(tz_NY)
# print (datetime_NY)