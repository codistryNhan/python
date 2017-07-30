#Looping through a dictionary
#use items()

person = {'firstname':'Jack',
          'lastname':'Smith',
          'username':'jSmith'
         }

for key, value in person.items():
  print(key + " " + value) 

#looping through keys only
for key in person.keys():
  print(key)


#loop through values only
for value in person.values():
  print(value)

#nesting in dicitonaries
#append dictionaries into an array

alien_1 = {'color':'green', 'hp':'100'}
alien_2 = {'color':'green', 'hp':'200'}
alien_3 = {'color':'blue', 'hp':'300'}

aliens = [alien_1, alien_2, alien_3]

for alien in aliens:
  print(alien)

#create 10 aliens
aliens = []

for x in range(10):
  alien = {'color':'green', 'hp':'10'}
  aliens.append(alien)

print(len(aliens))

for alien in aliens:
  print(alien)
