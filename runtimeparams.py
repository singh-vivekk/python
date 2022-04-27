import argparse

parser = argparse.ArgumentParser(description='Module Description : to get the run time params')

parser.add_argument("-num","--number", type= int, help=('enter a number'))
parser.add_argument("-dist","--distance", type= int, help=('enter distance in kms'))

pars = parser.parse_args()

x=pars.number
y=pars.distance

if not pars.number:
    x = 0

# if not None:
#     print("value is None")
#
# if not False:
#     print("value is False")
#
# if not 0:
#     print("value is not 0")

rng = range(x)
j=0
for i in rng:
    j=i+j

print("sum of numbers = ", j)
print("Entered number is : ", x)
print("Entered distance is : ", y)
