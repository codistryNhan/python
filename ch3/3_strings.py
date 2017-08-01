#Strings
#Strings are letters, characters

message = "Hello there"

#String title()
#Uppercases the first letter of each word

name = "jake nguyen"
name = name.title()
print(name) #Jake Nguyen

#String upper()
#Capitalizes all characters of string

name = name.upper()
print(name) #JAKE NGUYEN

#String lower()
#Lower Cases all characters of string

name = name.lower()
print(name) #jake nguyen

#String Concatenation
# use + operator
firstName = "jake"
lastName = "nguyen"

name = firstName + " " + lastName
print(name) #jake nguyen

#use \n for newlines
#\t for tab

#Stripping Whitespaces
#strip() strips left and right spaces 
# "  Hello World  "  - >  "Hello World"
message = "  Hello World  "
message = message.strip()
print(message)

#rstrip() strips whitespace on right
#lstrip() strips whitespace on left
