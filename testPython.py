def formatString(*args):
    # print("strict pattern:  Car Brand is : ", rtparam, "  and the color is :", rtparam,"  ->",  color)
    # in python version below 3.6 -- format method
    # print("Car Brand is : {0} and the color is : \n\n {0} -> {2}, \n\n {1} : {0}".format(rtparam,mfgyear,color))

# fstring: 3.6+
    print(f"Car Brand is : {args(0)} and the color is : \n\n {args(0)} -> {args(2)}, \n\n")


#
# def testMethod():
#     print("inside test Method")
#
#
# print(__name__)

import pythonbasic

if __name__=='__main__':
    # formatString('audi', '2020', 'blue')
    # formatString('BMW', 'black')
    pythonbasic.printHelloWorld()