# from chandra.childClass import Child

class BaseClass1:

    def __init__(self,name):
        print("this is from baseclass constructor")
        # self.db_name='my_oracle_db'
        self.nm=name
        # print("self.nm ", self.nm)







    def basemethod1(self):
        print(self)
        print(f"Hey {self.nm}, I'm from base class base method")
        num=len(self.nm)
        print("the length of name is = ", num)
        print("the oracle db name is : ", self.db_name)


    def basemethod2(self, name):
        print(f"Hey {name}, I'm from base class basemethod2 ----------- ")



if __name__ == '__main__':
    from chandra.baseClass2 import BaseClass2
    config=BaseClass1()
    print("from base class ----- ")
    config.basemethod1('vivek')

    print(__name__)    # directly running the same file where it is defined. = __main__
                       # indirect call - then __name__ will become name of the file