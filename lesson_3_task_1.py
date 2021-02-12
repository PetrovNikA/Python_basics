# Задание 1
# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

a = input('Первое число: ')
b = input('Второе число: ')


def my_div(x, y):
    try:
        x, y = float(x), float(y)
        result = x / y
    except ZeroDivisionError:
        return 'Деление на ноль!'
    except ValueError:
        return 'Введено не числовое значение'
    return result


c = my_div(a, b)
print(c)
