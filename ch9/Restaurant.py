#A Restaurant class
#Example of a class 

class Restaurant():
  def __init__(self,restaurant_name, cuisine_type):
    self.restaurant_name = restaurant_name
    self.cuisine_type = cuisine_type
    self.number_served = 0

  def describe_restaurant(self):
    print("Restaurant Name: " + self.restaurant_name)
    print("Cusine Type: " + self.cuisine_type)
    print("Number Served: " + str(self.number_served))

  def open_restaurant(self):
    print("The restaurant is now open")

  def set_number_served(self, number):
    self.number_served = number

  def increment_number_served(self, increment):
    self.number_served += increment

class IceCreamStand(Restaurant):
  def __init__(self, restaurant_name, cuisine_type):
    super().__init__(restaurant_name, cuisine_type)
    self.flavors = ['vanilla','strawberry','chocolate']

  def get_flavors(self):
    for flavor in self.flavors:
      print(flavor)


ic = IceCreamStand('Cream King', 'ice cream')
ic.get_flavors()
