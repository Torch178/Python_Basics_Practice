import random

def add(a, b):
    c = a +b
    return c
result = add(100, 200)
print(result)

def square(c):
    return c*c
result = square(add(3,2))
print(result)

for x in range(1,6):
    result = random.randint(1,6)
    print(result)