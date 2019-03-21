try:
    with open('cats_and_dogs/cats.txt') as f_obj:
        print("Cats:\n" + f_obj.read())

    with open('cats_and_dogs/dogs.txt') as f_obj:
        print("Dogs:\n" + f_obj.read())
except:
    print("File(s) not found!")