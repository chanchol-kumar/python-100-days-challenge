# Python supports a wide variety of functions or methods like: int(), float(), str(), ord(), hex(), oct(), tuple(), set(), list(), dict(), etc. for the type casting in python.

a = "1"         # string
b = "2"         # string
print(a + b)    # string + string = string

# Two Types of Typecasting:
#1.Explicit Conversion (Explicit type casting in python)
a = "1" 
b = "2"
print(int(a) + int(b)) # convert string to integer

#2.Implicit Conversion (Implicit type casting in python).
a = 1.5         # float number
b = 2           # int number
print(a + b)    # a + b = 3.5

# Python converts a smaller data type to a higher data type to prevent data loss.
