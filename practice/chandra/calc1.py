# from chandra.childClass import Child

class Calc:

    def __init__(self,num1=0, num2=0):
        print("this is from baseclass constructor")
        self.num1=num1
        self.num2=num2
        if isinstance(num1,int) and isinstance(num2,int):
            print("valid values - we can proceed")
        else:
            msg = "Invalid numbers. it should be of int type but the given values are of type {}".format(type(num1))
            print( msg)

    def addition(self, num1=0, num2=0):
        self.num1=num1
        self.num2=num2
        print("First value is : ", self.num1)
        print("Second value is : ", self.num2)
        print("Sum is = ", self.num1+self.num2)


