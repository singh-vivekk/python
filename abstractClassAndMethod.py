from abc import ABCMeta, abstractmethod

class AbstractClass(metaclass=ABCMeta):

    @abstractmethod                         #This decorator from abc library makes the abstractMethod abstract.
    def abstractMethod(self):
        print("Abstract method")
        return

class ConcreteClass(AbstractClass):

    def __init__(self):
        self.me = "me"

# Will get a TypeError without the following two lines:
# Error - TypeError: Can't instantiate abstract class ConcreteClass with abstract methods abstractMethod
    def abstractMethod(self):
        print("from abstractMethod implementation")
        return 0

c = ConcreteClass()
c.abstractMethod()