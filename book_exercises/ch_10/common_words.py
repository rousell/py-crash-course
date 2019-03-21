with open('books/don_quijote.txt') as file_object:
    text = file_object.read().lower()
    print(text.count('el'))

with open('books/peter_pan.txt') as f_obj:
    text = f_obj.read().lower()
    print(text.count('the'))