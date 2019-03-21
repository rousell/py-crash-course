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
