#User Class
#another example for class

class User():
  def __init__(self, first_name, last_name, city):
    self.first_name = first_name
    self.last_name = last_name
    self.city = city
    self.login_attempts = 0

  def describe_user(self):
    print("First Name: " + self.first_name)
    print("Last Name: " + self.last_name)
    print("City: " + self.city)
    print("Login Attempts: " + str(self.login_attempts))

  def greet_user(self):
    print("Good Morning " + self.first_name + " " + self.last_name)

  def increment_login_attempts(self):
    self.login_attempts += 1

  def reset_login_attempts(self):
    self.login_attempts = 0

class Privileges():
  def __init__(self):
    self.privileges = ["can add post", "can delete post", "can ban user"]

  def show_privileges(self):
    for priv in self.privileges:
      print(priv)

class Admin(User):
  def __init__(self, first_name, last_name, city):
    super().__init__(first_name, last_name, city)
    self.privilege = Privileges()

admin = Admin("John", "Smith", "San Francisco")
admin.privilege.show_privileges()
