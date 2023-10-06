# String In python

# use double quotation
text = "He said, \"I am a happy person.\" "
print(text)

# use single quotation
text = 'He said, "I am a happy person." '
print(text)

# multiple line string (use """ """)
text ="""Hey,how are you?
I am fine and You?
I am fine also."""
print(text)

# multiple line string (use ''' ''')
text ='''Hey,how are you?
I am fine and You?
I am fine also.'''
print(text)

# Accessing character of a string
str = "Harry"
print(str)      # Calculate string length
print(len(str)) # length = 4
print(str[0])   # H
print(str[1])   # a
print(str[2])   # r
print(str[3])   # r
print(str[4])   # y
#print(str[5]) # its not working.because of its length

#  Accessing character of a string using for loop
country = "Bangladesh"
for charcter in country:
    print(charcter)
