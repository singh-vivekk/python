from chandra.passvariable import PassVar

class ChildVar(PassVar):

    def __init__(self):
        print("From ChildVar class init method")

    def sum(self,x,y):
        print(f"sum of {x} and {y} is = ", x+y)


    def mult(self, x,y):
        print("from child class")


objChild = ChildVar()
objChild.sum(1,2)
objChild.mult(2,3)