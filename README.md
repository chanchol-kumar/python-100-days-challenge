# Python 100 Days Challenge(Code with Harry)

## Day 01 : Introduction to Programming & Python

```python
print("Hello World")
print(5)
```

## Day 02 : Some Amazing Python Programs - The Power of Python

```python
# Some Super Project of python

1. Jervis
2. Love Calculator
3. Face recognition
4. Flappy Bird
5. Snake Game
```

## Day 03 : Modules and Pip
```
- pip
- cmd >> pip

- module : 1. Built in modules
           2. External modules

1. pip install pandas
2. pip install --upgrade pip
3. pip install scikit-learn
```
```python
import pandas
import sklearn
```

## Day 04 : Our First Python Program

```python
print("Hello World")    # Hello World
print(5)                # 5       
print(6+5)              # 11
print(6-5)              # 1
print(6*5)              # 30
```

## Day 05 : Comments, Escape Sequences & Print Statement

```python
# 1. Comments : 
# this is for single line comment
""" 
this is for multiple line comment
"""

# 2. Escape Sequences : 
print("This is newline \nfollow this.")
print("My favorite book is \"Bhagavad Gita.\"")

# 3. Print Statement : 
print("Hello Python",6,5,sep=" ~ ",end="\n")
```

## Day 06 : Variables & Data Types

```python
a = 123456789
print(a)        # 123456789
print(type(a))  # <class 'int'>
```

```python
b = 12345.6789
print(b)        # 12345.6789
print(type(b))  # <class 'float'>
```

```python
c = "Hello World"
print(c)        # Hello World
print(type(c))  # <class 'str'>
```

```python
d = True
print(d)        # True
print(type(d))  # <class 'bool'>
```

```python
e = None
print(e)        # None
print(type(e))  # <class 'NoneType'>
```

```python
f = complex(3,2)
print(f)        # (3+2j)
print(type(f))  # <class 'complex'>
```

```python
# list: A list is an ordered collection of data with elements separated by a comma and enclosed within square brackets.Lists are mutable and can be modified after creation.
list = [1,2,3,[-5,7],["Hello World"], 2.5 ]
print(list)        # [1, 2, 3, [-5, 7], ['Hello World'], 2.5]
print(type(list))  # <class 'list'>

```

```python
# Tuple: A tuple is an ordered collection of data with elements separated by a comma and enclosed within parentheses. Tuples are immutable and can not be modified after creation.
tuple = ("banana"), ("cherry"), ("mango")
print(tuple)        # ('banana', 'cherry', 'mango')
print(type(tuple))  # <class 'tuple'>
```

```python
# Mapped data: dict
# dict: A dictionary is an unordered collection of data containing a key:value pair. The key:value pairs are enclosed within curly brackets.
dictionary = {"Car": "BMW", "Year": 2023}
print(dictionary)        # {'Car': 'BMW', 'Year': 2023}
print(type(dictionary))  # <class 'dict'>
```

## Day 07 : Arithmetic Operator

```python
## Calculator with Python

a = 15
b = 6

print(a + b)    # Addition = 21
print(a - b)    # Subtraction = 9
print(a * b)    # Multiplication = 90
print(a / b)    # Division = 2.5
print(a % b)    # Modular arithmetic = 3
print(a ** b)   # Exponential = 11390625
print(a // b)   # Floor division = 2


n = 15
m = 7
ans1 = n+m
print("Addition of",n,"and",m,"is", ans1)
ans2 = n-m
print("Subtraction of",n,"and",m,"is", ans2)
ans3 = n*m
print("Multiplication of",n,"and",m,"is", ans3)
ans4 = n/m
print("Division of",n,"and",m,"is", ans4)
ans5 = n%m
print("Modulus of",n,"and",m,"is", ans5)
ans6 = n//m
print("Floor Division of",n,"and",m,"is", ans6)
ans7 = n**m
print("Exponential of",n,"and",m,"is", ans6)
```

## Day 08 : Calculator using Python

- Exercise 01 : Create a calculator capable of performing addition, subtraction, multiplication and division operations on two numbers.Your program should format the output in a readable manner!

```python
print("\n <------ Calculator ------>\n")

a = 15
b = 6

print("The addition of",a,"+",b," = ",a+b)
print("The addition of",a,"-",b," = ",a-b)
print("The addition of",a,"*",b," = ",a*b)
print("The addition of",a,"/",b," = ",a/b)
```

## Day 09 : Typecasting in Python

- Python supports a wide variety of functions or methods like: int(), float(), str(), ord(), hex(), oct(), tuple(), set(), list(), dict(), etc. for the type casting in python.

```python
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
```
- Python converts a smaller data type to a higher data type to prevent data loss.

## Day 10 : Taking User Input in Python

```python
# variable = input()
n = input("Enter a value : ")
print(n)
```

```python
a = input("Enter a value : ")
b = input("Enter a value : ")
print(a + b)    # a = 1; b = 2; output = 12 
```

- But input function returns the value as string. Hence we have to typecast them whenever required to another datatype.

```python
a = input("Enter a value : ")
b = input("Enter a value : ")
#print(int(a) + int(b)) ---->ValueError: invalid literal for int() with base 10
print(int(a) + float(b))    # a = 1; b = 2; output = 3.0
```

- variable = data_type(input())

```python
a = int(input("Enter an integer value: "))
b = int(input("Enter an integer value: "))
print(a + b) # a = 1; b = 2; output = 3
```

## Day 11 : String in python

- Use double quotation
```python
text = "He said, \"I am a happy person.\" "
print(text)
```

- use single quotation
```python
text = 'He said, "I am a happy person." '
print(text)
```

- multiple line string (use """ """)
```python
text ="""Hey,how are you?
I am fine and You?
I am fine also."""
print(text)
```

- multiple line string (use ''' ''')
```python
text ='''Hey,how are you?
I am fine and You?
I am fine also.'''
print(text)
```

- Accessing character of a string
```python
str = "Harry"
print(str)      # Calculate string length
print(len(str)) # length = 4
print(str[0])   # H
print(str[1])   # a
print(str[2])   # r
print(str[3])   # r
print(str[4])   # y
#print(str[5]) # its not working.because of its length
```

-  Accessing character of a string using for loop
```python
country = "Bangladesh"
for charcter in country:
    print(charcter)
```


## Day 12 : Strings Slicing & Operations on Strings in Python

- length of string
```python
str = "Bangladesh"
length = len(str)
print("Length : ",length)   # Length : 10
```

- String slicing ---> print ( variable [start index : end index] )
```python
print(str[0:6])             # Bangla
print(str[0:len(str)])      # Bangladesh
print(str[0:length -4])     # Bangla
print(str[:length])         # Bangladesh ---> python's initial index is 0
print(str[6:length])        # desh
```
- Slicing using negetive index
```python
print(str[-4:length])        # desh ---> str[length-4 : length]
```

```python
# Quick Quiz :
s = "Harry"
print(s[-4:-2])    # ar ---> print(s[5-4 : 5-2]) ---> print(s[1 : 3])
```
