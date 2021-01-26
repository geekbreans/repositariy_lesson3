param_insert = ('Имя', 'Фамилия', 'Год Рождения', 'Город проживания', 'Эл почта', 'телефон')
in_value = ''
big_word = ''
words = ''


def user_data_get(name='', family='', bird_year='', city='', email='', phone=''):
    """Составляет словарь по переданным в функцию значениям значениям
    имя параматетр name
    фамилия параметр family
    год рождения папаметр bird_year
    город проживания параметр city
    Эл почта параметр email
    Телефон параметр phone
    """
    if name == '':
        return 'Не введени имя'
    elif family == '':
        return 'Не введена фамилмя'
    elif bird_year == '':
        return 'Не введен год рождения'
    elif city == '':
        return 'Нет введен город проживанмя'
    elif email == '':
        return 'Не введен эл адрес'
    elif phone == '':
        return 'Не введен номер телефона'
    else:
        user_dict = dict(name=name, family=family, bird_year=bird_year, city=city, email=email, phone=phone)
        return (user_dict)


while in_value != 'Конец ввода':
    in_value = input('Для ввода информации введите 1, для просмотра введенной информации введите 2"Конец ввода" '
                     'для выхода из программы ')
    if in_value == '1':
        big_word = ''
        for p in param_insert:
            param = ""
            while param == '':
                param = input(p)
                if param == '':
                    print('Введено пустое значение, повторите ввод')
                else:
                    big_word = big_word + ' ' + param
    elif in_value == '2':
        words = big_word.split()
        if len(words) == 6:

            print(user_data_get(words[0], words[1], words[2], words[3], words[4], words[5]))
        elif len(words) == 0:
            print('Данные не введены, введите пжл данные, для этго необходимо ввести 1')

print('Введена информация')
print(user_data_get('Иван', 'Иванов', '1999', 'Зеленоград', 'ivanov@ianan.ru', '999-99-99'))
