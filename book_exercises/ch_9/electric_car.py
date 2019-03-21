"""A set of classes that can be used to represent electric cars"""

from car import Car

class Battery():
    def __init__(self, battery_size=70):
        """Initalize the battery's attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def upgrade_battery(self):
        """Upgrades the battery size if possible"""
        if self.battery_size < 85:
            self.battery_size = 85
        else:
            print("You have already upgraded this battery!")

    def get_range(self):
        """Print a statemnt about the range this battery provides"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge"
        print(message)

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehiles."""

    def __init__(self, make, model, year):
        """
        Initalize attributes of the parent class.
        Initalize attributes specific to the electric car
        """
        super().__init__(make, model, year)
        self.battery = Battery()