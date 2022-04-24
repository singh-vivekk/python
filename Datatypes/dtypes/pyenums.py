#in python 3.4+
from enum import Enum, auto, unique

@unique
class Color(Enum):
    RED = auto()
    GREEN = auto()
    YELLOW = auto()
    VOILET = auto()
    PINK = auto()
    NOT_COMPLETED = ["IN-Progress", 'FAILED','PENDING','STUCK']
    ORANGE = auto()
    #VOILET = auto()    #TypeError('Attempted to reuse key: %r' % key)

print(Color)

print(Color.NOT_COMPLETED.name, " is " , Color.NOT_COMPLETED.value)
# Color.GOLDEN = 9
# print(Color.GOLDEN.name, " is " , Color.GOLDEN.value)

print(Color.NOT_COMPLETED.value)