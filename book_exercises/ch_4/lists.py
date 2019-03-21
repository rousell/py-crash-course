#### LISTS

# for value in range(1,5):
#     print(value)

# numbers = list(range(2,11,2))
# print(numbers)

# squares = []
# for value in range(1,11):
#     squares.append(value**2)

# print(squares)

### List comprehension
# squares = [value**2 for value in range(1,11)]
# print(squares)

## Count to 20
# for num in range(1,21):
#     print(num)

## One Million
# for num in range(1,1000001):
#     print(num)

## Summing a Million
# mil = list(range(1,1000001))
# print(min(mil))
# print(max(mil))
# print(sum(mil))

## Odd Numbers
# for num in range(1,20,2):
#     print(num)

## Threes
# for num in range(3,31,3):
#     print(num)

## Cubes
# cubes = [num**3 for num in range(1,11)]
# print(cubes)

### Slicing
# animals = ['puppy', 'cat', 'mouse', 'monkey', 'bird', 'lemur', 'alligator', 'insect', 'poop']
# print('The first three tiems in the list are ' + str(animals[:3]))
# length = len(animals)
# starting_num = int((length - 6) / 2) + 1
# print('three items from the middle of the list are: ' + str(animals[starting_num:starting_num+3]))
# print('The last three tiems in the list are: ' + str(animals[(length - 3):]))

## My Pizzas, Your Pizzas
# pizza = ['cheese', 'great escape', 'sausage']
# friend_pizza = pizza[:]
# pizza.append('veggie')
# print('My favorite pizzas are')
# for piz in pizza:
#     print(piz)

# print("My friend's favorite pizzas are")
# for piz in friend_pizza:
#     print(piz)