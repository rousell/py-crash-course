from users import User

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
