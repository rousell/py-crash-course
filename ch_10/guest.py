## Guest
# guest_name = input("Please enter your name into the guest book: ")
# with open('guest_book.txt', 'a') as file_object:
#     file_object.write(guest_name + '\n')

## Guest Book
running = True
while running:
    guest_name = input("Please enter your name into the guest book: ")
    if guest_name == 'quit':
        break
    with open('guest_book.txt', 'a') as file_object:
        file_object.write(guest_name + '\n')
