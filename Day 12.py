### Day 12 : Strings Slicing and Operations on Strings in Python

# length of string
str = "Bangladesh"
length = len(str)
print("Length : ",length)   # Length : 10

# String slicing ---> print(variable[start index : end index])
print(str[0:6])             # Bangla
print(str[0:len(str)])      # Bangladesh
print(str[0:length -4])     # Bangla
print(str[:length])         # Bangladesh ---> python's initial index is 0
print(str[6:length])        # desh

# Slicing using negetive index
print(str[-4:length])        # desh ---> str[length-4 : length]

# Quick Quiz :
s = "Harry"
print(s[-4:-2])    # ar ---> print(s[5-4 : 5-2]) ---> print(s[1 : 3])