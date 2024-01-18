#dictionaries
people = {
    "name": "Cody",
    "age": 30
}
print(people["name"])
print(people["age"])

numbers = {
    1: "one",
    2: "two",
    3: "three"
}
print(1 in numbers)
print(5 in numbers)

print(numbers.get(1))
print(numbers.get(5, "Key not found"))

#tuple
fruit = ("apple", "banana", "mango")
print(fruit)
print(fruit[0])
#cannot assign values to tuple, will cause error, static collection
#fruit[0] = "pineapple"

#list slicing
numbers = [0, 100, 200, 300, 400, 500, 600]
#3 - 5 index range
print(numbers[3:5])
#beginning to index 3
print(numbers[:3])
#1 - 6 index, skip every two
print(numbers[1:6:2])

#advanced lists
list = [x**2 for x in range(10) if x**2 % 2 == 0]
print(list)

#string formatting
numbers = [10, 8, 2024]
newstring = "Date : {0}/{1}/{2}".format(numbers[0],numbers[1], numbers[2])
print(newstring)

a = "{x}/{y}".format(x = 100, y = 200)
print(a)

#string functions
print(" is next to ".join(["apple", "bannana", "mango"]))
newstring = "Hello There"
newstring  = newstring.replace("There", "World")
print(newstring)

a = "This is a string"
print(a.startswith("hello"))
print(a.endswith("string"))

print(a.upper())
print(a.lower())

#number functions
print(min(1,2,3,4,5))
print(max(1,2,3,4,5))
print(abs(-200))