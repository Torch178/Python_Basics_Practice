class Teddy:
    quantity = 200

    #constructor
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def change_color(self, color):
        print("This is a method")
        self.color = color

teddy1 = Teddy("Ted", "red")
teddy2 = Teddy("Christian", "blue")
print(teddy1.name)
print(teddy1.color)

teddy1.change_color("white")
print(teddy1.color)

#------------------------------------------------------
#Functional Vs OOP
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_data(self):
        self.name = input("Enter name: ")
        self.age = input("Enter age: ")

    def put_data(self):
        print(self.name)
        print(self.age)

student1 = Student("", "")
# student1.get_data()
# student1.put_data()

#------------------------------------------------------
#Inheritance

class ScienceStudent(Student):
    def science(self):
        print("This is a science function")


a = ScienceStudent("", "")
a.science()
# a.get_data()
# a.put_data()

#------------------------------------------------------
#Multiple Inheritances
class A:
    def a_method(self):
        print("This is A method")

class B:
    def b_method(self):
        print("This is B method")

class C(A,B):
    def c_method(self):
        print("This is C method")

cObject = C()
cObject.a_method()
cObject.b_method()
cObject.c_method()

#Alternatively class B(A): class C(B) to inherit from multiple classes

#------------------------------------------------------
#Recursion
def factorial(x):
    if(x == 1):
        return 1
    else:
        return x*factorial(x-1)

result = factorial(5)
print(result)

#------------------------------------------------------
#Sets
numbers = {1,2,3,4,5,6,7,8,9,10}
print(numbers)

print(5 in numbers)
numbers.add(9)
print(numbers)
numbers.remove(4)
print(numbers)

seta = {1,2,3,4,5}
setb = {4,5,6,7,8}

#Union - combo excluding duplicates
print(seta | setb)
#Intersection - shared values only
print(seta & setb)
#Difference - removes shared values from result
print(seta - setb)
