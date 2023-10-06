## Day 13 : String Methods
# String are immutable

str1 = "Bangladesh"
print(str1.upper())                 # BANGLADESH

str2 = "BANGLADESH"
print(str2.lower())                 # bangladesh

str3 = " Bangladesh is my country. "
print(str3.rstrip(" "))             # The strip() method removes any white spaces before and after the string.

str4 = "Bangladesh is my country."
print(str4.split(" "))              # create a list

str5 = "Bangladesh is my country."
print(str5.replace("my","our"))     # Bangladesh is our country.

str6 = "bangladesh is mY Country."
print(str6.capitalize())            # only 1st word capital ,otherwise lower case 
                                    # output : Bangladesh is my country.

str7 = "Bangladesh is mY Country."
print(len(str7))                    # 25
print(len(str7.center(50)))         # 50
print(str7.center(50))              #             Bangladesh is mY Country.

str8 = "Bangladesh"
print(str8.count("a"))              # 2

str9 = "Welcome to the Console !!!"
print(str9.endswith("!!!"))         # True

str10 = "Welcome to the Console !!!"
print(str10.endswith("to", 4, 10))  # True 

str11 = "He's name is Dan. He is an honest man."
print(str11.find("ishh"))           # -1
# print(str1.index("ishh"))

str12 = "WelcomeToTheConsole"
print(str12.isalnum())              # True

str13 = "Welcome"
print(str13.isalpha())              # True

str14 = "hello world"
print(str14.islower())              # True

str15 = "We wish you a Merry Christmas\n"
print(str15.isprintable())          # False

str16 = "         "                 #using Spacebar
print(str16.isspace())              # True

str17= "  "                         #using Tab
print(str17.isspace())              # True

str18 = "World Health Organization" 
print(str18.istitle())              # True

str19 = "To kill a Mocking bird"
print(str19.istitle())              # False

str20 = "Python is a Interpreted Language" 
print(str18.startswith("Python"))   # False

str21 = "Python is a Interpreted Language" 
print(str21.swapcase())             # pYTHON IS A iNTERPRETED lANGUAGE

str22 = "His name is Dan. Dan is an honest man."
print(str22.title())                # His Name Is Dan. Dan Is An Honest Man.    

