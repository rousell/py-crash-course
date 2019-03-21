## People
person_0 = {'first_name': 'Thomas', 'last_name': 'Anderson', 'age': 20, 'city': 'Zion'}
person_1 = {'first_name': 'Harry', 'last_name': 'Potter', 'age': 11, 'city': 'London'}
person_2 = {'first_name': 'Hildy', 'last_name': 'Johnson', 'age': 34, 'city': 'New York'}

people = [person_0, person_1, person_2]
# for person in people:
#     print("The character " + person['first_name'] + " " + person['last_name'] +
#     " lives in " + person['city'] + " and is " + str(person['age']))

## Pets
pets = {
    'scout': {
        'kind': 'terrier',
        'owner_name': 'atticus',
    },
    'rio': {
        'kind': 'golden retriever',
        'owner_name': 'thomas',
    },
    'pandora': {
        'kind': 'black lab',
        'owner_name': 'martha',
    },
}
# for pet_name, pet_info in pets.items():
#     print(pet_name.title() + " is a " + pet_info['kind'] + " whose owner is " + pet_info['owner_name'].title())

## Favorite Places
favorite_places = {
    'Taiwan': 'Lauren',
    'Copenhagen': 'Ron',
    'Florida': 'Sam',
}

# for place, person in favorite_places.items():
#     print(place + " is " + person + "'s favorite place")

## Cities
cities = {
    'Chicago': {
        'country': 'USA',
        'approx_pop': 2700000,
        'fact': "there are 303 miles of bike lanes in Chicago",
    },
    'Milan': {
        'country': 'Italy',
        'approx_pop': 1366000,
        'fact': " was one of the few European cities which was not reached by the plague in the XIV century",
    },
    'Ho Chi Minh City': {
        'country': 'Vietnam',
        'approx_pop': 8444000,
        'fact': "its former name is Saigon",
    },
}

# for city, info in cities.items():
#     print(city + ", " + info['country'] + " has an approx. population of " + str(info['approx_pop']) +
#     " and " + info['fact'])

