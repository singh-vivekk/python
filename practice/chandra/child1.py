from chandra.baseClass1 import BaseClass1

# BaseClass
#        -> Child(baseClass) : Simple Inheritance
# BaseClass / Child
#       -> Child2 (BaseClass , Child) : Multiple inheritance
# BaseClass
#       -> Child1
#           -> grandChild : Multilevel

class Child(BaseClass1):

    def childMethod1(self, name):
        print(f"Hey {name}, I'm from child1 class child method1")


obj=Child()
# print(dir(obj))
obj.basemethod1('vivek')
# obj.childMethod1('Child')
# obj.childMethod1('Child2')





# parent (BaseClass) -> Child2 (all features of BaseClass), it can have some more features of its own
# __main__
# __init__