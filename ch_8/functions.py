# import car_module
# from car_module import build_car
# from car_module import build_car as bc
# import car_module as cm
from car_module import *

## Message
def display_message():
    """Display Chapter 8's Topic"""
    print("We are learning about functions in this chapter!")

# display_message()

## Favorite Book
def favorite_book(title):
    """Display favorite book"""
    print("One of my favorite books is " + title)

# favorite_book("Harry Potter")

## T-Shirt, Large Shirts
def make_shirt(size='L', text='I love Python'):
    """Display Specified Shirt"""
    print("Please make a " + size + " shirt with the text: " + text)

# make_shirt("XS", "Kansas City Kansas City Kansas City")
# make_shirt(size="M", text="Music City Code")
# make_shirt("M")
# make_shirt()

## Cities
def describe_city(city, country="the United States of America"):
    """Display City Information"""
    print(city + " is in " + country)

# describe_city("Nashville")
# describe_city("Washington D.C.")
# describe_city("Bogotá", "Columbia")

## City Names
def city_country(city, country):
    return city.title() + ", " + country.title()

# print(city_country("Santiago", "Chile"))
# print(city_country("Taipei", "Taiwan"))
# print(city_country("anchorage", "alaska"))

## Album
def make_album(artist_name, album_title, num_of_tracks=''):
    if num_of_tracks:
        album = {'artist_name': artist_name, 'album_title': album_title, 'num_of_tracks': num_of_tracks}
    else:
        album = {'artist_name': artist_name, 'album_title': album_title}
    return album

# print(make_album('Mitski', 'Be the Cowboy', 14))
# print(make_album('Robyn', 'Honey'))
# print(make_album('Soccer Mommy', 'Clean'))

## User Albums
running = True
# while running:
#     print("\nThis is a place for you to put in your favorite album. Enter 'q' at any time to quit.")
#     artist = input("Please enter the artist's name: ")
#     if artist == 'q':
#         break
#     album = input("Please enter the album name: ")
#     if album == 'q':
#         break
#     print(make_album(artist, album))

## Magicians, Great Magicians
magicians = ['David Copperfield', 'Siegfried and Roy', 'Penn and Teller']
def show_magicians(mages):
    for m in mages:
        print(m)

def make_great(mages):
    great_mages = []
    for m in mages:
        m += " the Great"
        great_mages.append(m)
    return great_mages

# great_mages = make_great(magicians)
# show_magicians(great_mages)

## Sandwiches
def print_sandwich(*ingredients):
    """Print the desired sandwich"""
    print("The sandwich should be made with " + ', '.join(ingredients))

# print_sandwich('bread', 'ham', 'cheese')
# print_sandwich('wrap', 'chicken', 'ceaser')
# print_sandwich('bread', 'bacon', 'lettuce', 'tomato')

## User Profile
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

# p = build_profile('Lauren','Rouse',gender='female',has_pet=True,currently_reading='Information: A History, a Theory, a Flood')
# print(p)

## Cars
def non_module_build_car(manufacturer, model, **info):
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for k,v in info.items():
        car[k] = v
    return car

# print(non_module_build_car('Nissan','Pathfinder',color='tan',make=1998))
# print(car_module.build_car('Nissan','Pathfinder',color='tan',make=1998))
# print(build_car('Nissan','Pathfinder',color='tan',make=1998))
# print(bc('Nissan','Pathfinder',color='tan',make=1998))
# print(cm.build_car('Nissan','Pathfinder',color='tan',make=1998))
print(build_car('Nissan','Pathfinder',color='tan',make=1998))