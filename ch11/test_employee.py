#Unit Test for Employee Class

import unittest
from employee import Employee

class EmployeeTest(unittest.TestCase):
  def setUp(self):
    first_name = "John"
    last_name = "Smith"
    salary = 5000

    self.employee = Employee(first_name, last_name, salary)

  def test_give_default_raise(self):
    self.employee.give_raise()
    self.assertEquals(10000, self.employee.salary)

  def test_give_custom_raise(self):
    self.employee.give_raise(10000)
    self.assertEquals(15000, self.employee.salary)

unittest.main()
