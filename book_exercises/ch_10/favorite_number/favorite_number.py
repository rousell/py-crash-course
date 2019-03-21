import json

try:
    with open('favorite_number.json') as f_obj:
        fav_num = json.load(f_obj)
except:
    fav_num = input("What is your favorite number? ")
    with open('favorite_number.json', 'w') as file_object:
        json.dump(fav_num, file_object)
else:
    print("I know your favorite number! It is " + fav_num)
