def my_func(num1, num2, num3):
    """ Фнкция считает сумму двух наибольщих величин переданных ей"""
    a = [num1, num2, num3]
    a.sort()
    return a[1] + a[2]


n_value = True
while n_value:
    w_value = input('Введите три числа и получите сумму наибольших двух, при вводе одиночного любого символа работа '
                    'программы будет прекращена ')
    w_value = w_value.split()
    if len(w_value) != 3:
        print("Введено не три числа")
        if len(w_value) == 1:
            print('Введено одиночный символ, работа программы буде прекращена')
            n_value = False
    else:
        v_value = True
        for w in w_value:
            if w.isnumeric() == 0:
                print('Среди введенных есть не числовые значения, повторите ввод ')
                v_value = False

        if v_value:
            print( my_func(int(w_value[0]), int(w_value[1]), int(w_value[2]), ))







