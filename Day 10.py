# variable = input()

n = input("Enter a value : ")
print(n)


a = input("Enter a value : ")
b = input("Enter a value : ")
print(a + b) # a = 1; b = 2; output = 12 

# But input function returns the value as string. Hence we have to typecast them whenever required to another datatype.
a = input("Enter a value : ")
b = input("Enter a value : ")
#print(int(a) + int(b)) ---->ValueError: invalid literal for int() with base 10
print(int(a) + float(b)) # a = 1; b = 2; output = 3.0

# variable = data_type(input())
a = int(input("Enter an integer value: "))
b = int(input("Enter an integer value: "))
print(a + b) # a = 1; b = 2; output = 3
