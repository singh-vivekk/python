import pandas as pd
import datetime
from pandas.tseries.offsets import MonthEnd, Day

startDate='20200130'
endDate='20200527'

# x=pd.to_datetime(str(endDate), format='%Y%m%d')+MonthEnd(1)
# print(x)

dateRange=[startDate,endDate]

ft =''

if len(str(startDate)) == 6:
    ft='%Y%m'
if len(str(endDate)) == 8:
    ft = '%Y%m%d'

if not isinstance(startDate, datetime.datetime):
    startDate=pd.to_datetime(startDate, format=ft)
if not isinstance(endDate, datetime.datetime):
    endDate = pd.to_datetime(endDate, format=ft)


rn1=[]
if ft:
    for date in dateRange:
        print(type(date))
        rn = pd.to_datetime(str(date), format=ft) + MonthEnd(1)
        rn1.append(rn)

# print(list(set(rn1)))



print("Start date of month is: ", startDate)
print("end date of month is: ", endDate)





dateRange=pd.date_range(startDate, endDate).tolist()
# print(dateRange)

dft=[]
for date in dateRange:
    if not isinstance(date,datetime.datetime):
        if len(str(date)) == 6:
            date=pd.to_datetime(str(date), format='%Y%m')
        elif len(str(date)) == 8:
            date=pd.to_datetime(str(date), format='%Y%m')
        else:
            raise Exception('reporting period format issue')

    dft.append(date)
print("\n\n")
# print(dft)

print("\n\n ---- from is_month_end method ----")
ldm=[]
for date in dft:
    if date.is_month_end:
        # print(date)
        # print("is month end date")
        ldm.append(date)

formatedDates_is_month_end=[]
if ft:
    for date in ldm:
        date = date.strftime(ft)
        formatedDates_is_month_end.append(date)


print(formatedDates_is_month_end)




print("\n\n ---- from MonthEnd(0) method ----")
ldm1=[]
for date in dft:
    date=date+MonthEnd(0)
    ldm1.append(date)


# print(ldm1)
# dtFormat ='%Y%m%d'
formatedDates= []

if ft:
    for date in ldm1:
        date = date.strftime(ft)
        formatedDates.append(date)

# print("\n\nbelow are the formatted month end date")
print(list(set(formatedDates)))