running = True
while running:
    print('\nYou can exit by entering \'q\' at any time')
    response = input("What is a thing that you like about programming? ")
    if response == 'q':
        break
    with open ('programming_poll.txt', 'a') as file_object:
        file_object.write(response + '\n')
