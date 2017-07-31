#Write
#the open() takes 2 arguments, the second argument 'w' tells to open in write mode
#open('file.txt', 'w')
# 'w' - write, 'r' - read, 'a' - append, 'r+' read and write
#use write()

#to write a string on its own line, use \n

filename = 'programming.txt'

with open(filename, 'w') as file_object:
  file_object.write("I love programming.\n")
  file_object.write("I love dogs too.\n")
