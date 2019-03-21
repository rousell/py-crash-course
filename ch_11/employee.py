class Employee():
    """Represents Employee"""
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
        self.annual_raise = 5000

    def give_raise(self, alternative_raise=0):
        if alternative_raise != 0 and type(alternative_raise) is int:
            self.annual_raise = alternative_raise
        else:
            self.annual_raise = 5000
        self.annual_salary += self.annual_raise
        return self.annual_salary
