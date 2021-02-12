# Задание 3
# Реализовать функцию my_func(),
# которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.

def my_func(n1, n2, n3):
    n1, n2, n3 = float(n1), float(n2), float(n3)
    list_for_sum = [n1, n2, n3]
    x = max(list_for_sum) - min(list_for_sum)
    return x


print(my_func(1, 3, 5))
