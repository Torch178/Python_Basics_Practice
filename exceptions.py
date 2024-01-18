try:
    a = 20
    b = 0
    print(a/b)
except ZeroDivisionError:
    print('Error: division by zero')
finally:
    print("This will execute  no matter what")