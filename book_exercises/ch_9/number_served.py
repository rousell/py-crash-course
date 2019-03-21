from restaurant import Restaurant

eating_place = Restaurant("Otaku South", "ramen")
print(eating_place.number_served)

eating_place.number_served = 5
print(eating_place.number_served)

eating_place.set_number_served(10)
print(eating_place.number_served)

eating_place.increment_number_served(40)
print(eating_place.number_served)
