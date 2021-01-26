def my_division(number1, number2=0):
    if number2 == 0:
        return "Деление на ноль, введите не нулевое значение"
    else:
        return number1 / number2


in_value = ""

while in_value != 'Конец ввода':
    in_value = input('Введите два числа через пробел (целые):')
    numbers = in_value.split()
    if len(numbers) < 3:

        if numbers[0].isnumeric() and numbers[1].isnumeric():
            num1 = int(numbers[0])
            num2 = int(numbers[1])
            print(my_division(num1, num2))
        else:
            print("Введены не числовые значения")
