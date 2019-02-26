## Addition, Addition Calculator
while True:
    print("This program does addition. Enter 'q' to quit.")
    first_num = input("Please enter a number to add: ")
    if first_num == 'q':
        break
    second_num = input("Please enter an additional number to add: ")
    if second_num == 'q':
        break
    try:
        print("The sum is: " + str(int(first_num) + int(second_num)) + "\n")
    except:
        print("Both inputs must be numbers!\n")