def int_func(my_word):
    my_word = str(my_word)
    return my_word[0].upper() + my_word[1:len(my_word)].lower()


in_value = ''

while in_value != 'F':
    in_value = input('Введите  слова через пробел (целые):')
    words = in_value.split()
    for word in words:
        print(int_func(word))
