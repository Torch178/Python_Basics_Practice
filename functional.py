#----------------------------------------------
#Basic Functions
def add_ten(x):
    return x + 10

def twice(func,arg):
    return func(func(arg))

print(twice(add_ten, 10))

def square(x):
    return x**2

#----------------------------------------------
#Lambda - anonymous function
result =  (lambda x:x**2)(30)

print(result)

#----------------------------------------------
#Maps
def add(x):
    return x+2

newlist = [10, 20, 30, 40, 50, 60]

result = list(map(add, newlist))
print(result)

result = list(map(lambda x:x+2, newlist))
print(result)

#----------------------------------------------
#Filters
newlist = [1, 3, 4, 5, 7, 2, 9, 11, 13]

result = list(filter(lambda x: x % 2 == 0, newlist))

print(result)

#----------------------------------------------
#Generators
def function():
    counter = 0
    while counter < 5:
        yield counter
        counter += 1

for x in function():
    print(x)

def even_numbers(x):
    for  i in range(x):
        if i % 2 == 0:
            yield i

print(list(even_numbers(21)))