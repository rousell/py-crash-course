## Restaurant, Three Restaurants
class Restaurant():
    def __init__(self, name, food_type):
        self.restaurant_name = name
        self.cuisine_type = food_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name + " serves " + self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant is open!")

    def set_number_served(self, num):
        self.number_served = num

    def increment_number_served(self, num):
        self.number_served += num

food_place = Restaurant("Otaku South", "ramen")
# print(food_place)
# print(food_place.restaurant_name)
# print(food_place.cuisine_type)
# food_place.describe_restaurant()
# food_place.open_restaurant()

food_place_2 = Restaurant("Five Points Pizza", "pizza")
food_place_3 = Restaurant("Thida Thai", "thai")

# food_place_2.describe_restaurant()
# food_place_3.describe_restaurant()

class IceCreamStand(Restaurant):
    def __init__(self, name, food_type):
        """
        Initialize attributes of the parent class
        Defines Ice Cream Stand attributes
        """
        super().__init__(name, food_type)
        self.flavors = ['vanilla', 'coffee', 'strawberry']
        self.name = name

    def display_flavors(self):
        """Displays ice cream stand flavors"""
        print(self.name + " has the following ice cream flavors: " + ', '.join(self.flavors))

oberweis_store = IceCreamStand("Oberweis", "Ice Cream")
# oberweis_store.describe_restaurant()
# oberweis_store.display_flavors()

