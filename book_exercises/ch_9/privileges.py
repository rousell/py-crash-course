class Privileges():
    def __init__(self, privileges):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        """Displays Admin User privileges"""
        print("The Admin User has the following privileges: " + ', '.join(self.privileges))