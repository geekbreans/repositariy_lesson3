in_value = ""
big_value = 0
tmp_value = 0

while in_value != 'F':
    in_value = input('Введите  числа через пробел, при вводе символа F,работа программы будт завершена: ')
    numbers = in_value.split()

    tmp_value = 0

    for s in numbers:
        try:
            m = float(s)
            print(m)
            tmp_value = tmp_value + m
        except ValueError:
            if s == 'F':
                in_value = 'F'
                big_value = big_value + tmp_value
                print(f'Сумма введенных чисел равна {tmp_value}, всего введено чисел на сумму {big_value}, так как '
                      f'введен симвло F работа программы будет завершена')
                exit()
    big_value = big_value + tmp_value
    print(f'Сумма введенных чисел равна {tmp_value}, всего введено чисел на сумму {big_value}')
