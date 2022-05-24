from datetime import date, datetime

silverLoadDate = date.today()
print(silverLoadDate)

silverLoadDateTime = datetime.now()
print(silverLoadDateTime)
print(silverLoadDateTime - 2 )

today=silverLoadDate
print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)