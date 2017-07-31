]#use open() to open file
#open('digits'.txt)
#read() to read file
#read() returns an empty string when it reaches EOF
  #so we use rstrip() on contents
try:
  with open('digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

except FileNotFoundError:
  print("File not found"
)
#Reading line by line
#use a for loop to read each line

filename = 'paragraph.txt'

try:

  with open(filename) as file_object:
    for line in file_object:
      print(line)

except FileNotFoundError:
  print(filename + " not found!")
