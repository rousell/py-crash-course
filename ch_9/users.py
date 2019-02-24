class User():
    def __init__(self, first, last, age, gender):
        self.first_name = first
        self.last_name = last
        self.age = age
        self.gender = gender
        self.login_attempts = 0

    def describe_user(self):
        print(self.first_name + " " + self.last_name +
        " is a " + self.gender + " " + str(self.age) + " year old")

    def greet_user(self):
        print("Hello " + self.first_name + "! I hope you are having a good day!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user_0 = User("Fred", "Smith", 60, "male")
user_1 = User("Nellie", "Brown", 32, "female")

# user_0.describe_user()
# user_0.greet_user()

# user_1.describe_user()
# user_1.greet_user()

class Privileges():
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        """Displays Admin User privileges"""
        print("The Admin User has the following privileges: " + ', '.join(self.privileges))

class Admin(User):
    def __init__(self, first, last, age, gender):
        """
        Initialize attributes of the parent class
        Defines Admin attributes
        """
        super().__init__(first, last, age, gender)
        self.privileges = Privileges()

super_user = Admin("Peter", "Gibbons", 32, "male")
super_user.privileges.show_privileges()