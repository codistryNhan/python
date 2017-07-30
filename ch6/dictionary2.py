#A list in a dictionary
pizza = {
          'crust':'thick',
          'toppings':['mushrooms','extra cheese'],
        }


print("Your crust type is: " + pizza['crust'])
print("Your toppings are: ")

for topping in pizza['toppings']:
  print(topping)


#dictionary in a dictionary
people = {
           'albert009':{
             'firstname':'albert',
             'lastname':'lee',
             'city':'San Francisco'
           },
           'johnY2k':{
             'firstname':'johny',
             'lastname':'smith',
             'city':'toronto'
           },
         }

for username,info in people.items():
  print("The username is " + username)

  for key,value in info.items():
    print("And their info are " + key + " " + value)
