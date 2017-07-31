#Checking word count 

def count_words(filename):
  try:
    with open(filename) as file:
      contents = file.read()

  except FileNotFoundError:
    msg = "File not found"
    print(msg)

  else:
    words = contents.split()
    number_of_words = len(words)
    print("Thie file has " + str(number_of_words) + " words.")

filename = 'alice.txt'

count_words(filename)
