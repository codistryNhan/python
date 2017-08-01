class Employee():
  def __init__(self,first,last,salary):
    self.first_name = first
    self.last_name = last
    self.salary = salary

  def give_raise(self, raise_amount = ''):
    if raise_amount:
      self.salary += raise_amount
    else:
      self.salary += 5000
