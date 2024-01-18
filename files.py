#initial read
file = open("demo.txt", "r")
content = file.read(10)
content = file.readline()
print(content)
file.close()

#write (overwrite)
file = open("demo.txt", "w")
file.write("Hello")
file.close()

#read
file = open("demo.txt", "r")
content = file.read()
print(content)
file.close()

#append to file (no overwriting)
file = open("demo.txt", "a")
file.write("Hello")
file.close()

