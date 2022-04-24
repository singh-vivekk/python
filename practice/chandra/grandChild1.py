from chandra.child1 import Child

# BaseClass -> Child -> Child2 : Multilevel

class GrandChild(Child):

    def grandMethod(self, name):
        print(f"Hey {name}, I'm from GrandChild class grandMethod")


gcobj=GrandChild()
# print(dir(gcobj))

gcobj.basemethod1('base')
gcobj.childMethod1('Child')
gcobj.grandMethod('grandchild')


# parent (BaseClass) -> Child2 (all features of BaseClass), it can have some more features of its own
# __main__
# __init__