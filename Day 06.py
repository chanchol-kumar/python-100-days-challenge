### Variables and Data Types


a = 123456789
print(a)        # 123456789
print(type(a))  # <class 'int'>

b = 12345.6789
print(b)        # 12345.6789
print(type(b))  # <class 'float'>

c = "Hello World"
print(c)        # Hello World
print(type(c))  # <class 'str'>

d = True
print(d)        # True
print(type(d))  # <class 'bool'>

e = None
print(e)        # None
print(type(e))  # <class 'NoneType'>

f = complex(3,2)
print(f)        # (3+2j)
print(type(f))  # <class 'complex'>

# list: A list is an ordered collection of data with elements separated by a comma and enclosed within square brackets.Lists are mutable and can be modified after creation.
list = [1,2,3,[-5,7],["Hello World"], 2.5 ]
print(list)        # [1, 2, 3, [-5, 7], ['Hello World'], 2.5]
print(type(list))  # <class 'list'>

# Tuple: A tuple is an ordered collection of data with elements separated by a comma and enclosed within parentheses. Tuples are immutable and can not be modified after creation.
tuple = ("banana"), ("cherry"), ("mango")
print(tuple)        # ('banana', 'cherry', 'mango')
print(type(tuple))  # <class 'tuple'>

# Mapped data: dict
# dict: A dictionary is an unordered collection of data containing a key:value pair. The key:value pairs are enclosed within curly brackets.
dictionary = {"Car": "BMW", "Year": 2023}
print(dictionary)        # {'Car': 'BMW', 'Year': 2023}
print(type(dictionary))  # <class 'dict'>
