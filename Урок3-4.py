def my_func(x, y):
    """Расчетная часть"""
    n = abs(y)
    i = 0
    s = 1
    while i < n:
        s = s * x
        i = i + 1
    if y > 0:
        return s
    else:
        return 1 / s


n_value = True
while n_value:
    w_value = input('Введите два числа, втрое число должно быть целым и положительным (для расчетв n1^n2, при вводе '
                    'одиночного любого символа работа '
                    'программы будет прекращена ')
    w_value = w_value.split()
    if len(w_value) != 2:
        print("Введено не два числа")
        if len(w_value) == 1:
            print('Введен одиночный символ, работа программы буде прекращена')
            n_value = False
    else:
        v_value = True
        try:
            float(w_value[0])
        except ValueError:
            print("Ошибка ввода числа - " + ValueError)
            v_value = False
        try:
            int(w_value[1])
        except ValueError:
            print("Ошибка ввода числа - " + ValueError)
            v_value = False

        if v_value:
            print(my_func(float(w_value[0]), int(w_value[1])))
