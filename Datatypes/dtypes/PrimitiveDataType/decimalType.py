from decimal import *
# b=6.0
a=Decimal(5.000043343283).quantize(Decimal('0.0000000001'), rounding=ROUND_CEILING)
b=Decimal(8.00004343223).quantize(Decimal('0.0000000001'), rounding=ROUND_FLOOR)
c=Decimal(18.00004343223).quantize(Decimal('0.0000000001'), rounding=ROUND_FLOOR)
# y=[b,a]
print(a)
print(b)
# print(y)
#
# z=[float(x) for x in y]
# print(z)

finalval=[(1,2,'vivek',a),(1,2,'Sagar',b),(1,2,'Akshay',c)]
# print(finalval)
# print(type(finalval))
# print(finalval[1][3])

# newfval=[x for x in ]

print("\n\n-------\n\n")
# print(a)
#
# c=b-a
# # using format() to print value till 2 decimal places
# print ("The value of number till 2 decimal place(using format()) is : ",end="")
# print ("{0:.8f}".format(c))
#
# print(a)
# # print(b)
# x=7
# d="{0:.8f}".format(x)
#
# print(d)