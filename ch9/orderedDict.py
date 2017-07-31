from collections import OrderedDict

dict = OrderedDict()

dict['firstname'] = 'John'
dict['lastname'] = 'Smith'
dict['city'] = 'San Francisco'

for key,value in dict.items():
  print(key + " " + value)
