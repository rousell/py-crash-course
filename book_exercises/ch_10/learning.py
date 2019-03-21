## Learning Python

# with open('learning_python.txt') as file_object:
#     full_text = file_object.read()
#     print(full_text)
#     print(full_text)
#     print(full_text)


# with open('learning_python.txt') as file_obj:
    # for line in file_obj:
    #     print(line.rstrip())
#     lines = file_obj.readlines()

# for line in lines:
#     print(line.rstrip())

## Learning C
with open('learning_python.txt') as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip().replace('Python', 'C'))