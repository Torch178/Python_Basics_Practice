from itertools import count
from itertools import accumulate, takewhile
for i in count(3):
    print(i)
    if i >= 20:
        break

#accumulate creates list with the difference between each progressive value going up by 1
#Ex: 0+1=1, 1+2=3, 3+3=6, etc.
numbers = list(accumulate(range(8)))
print(numbers)

#takewhile filters out values from a list given a function paramater as the filtering criteria
print(list(takewhile(lambda x: x <= 6, numbers)))


#-----------------------------------------------------
#Operator Overloading
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    #Operator Overload function
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x,y)

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

point1 = Point(1, 4)
point2 = Point(3, 7)
print(point1 + point2)

#-----------------------------------------------------
#Data Hiding / Encapsulation
#double underscore (__) is used to hide data within class from being accessed
#outside of the class scope
class myClass:
    __hiddenVar = 0

    def add(self, increment):
        self.__hiddenVar += increment
        print(self.__hiddenVar)

mc = myClass()
mc.add(4)

#print(mc.__hiddenVar) --Incorrect, will throw an error

