from abc import ABCMeta, abstractmethod

class PassVar(metaclass=ABCMeta):

    def __init__(self):
        print("Hello world! this is passvar class init method")

    @abstractmethod
    def sum(self, x,y):
        pass

    def mult(self, x,y):
        print("from abs class")
