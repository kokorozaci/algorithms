"""4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,
… Количество элементов (n) вводится с клавиатуры."""


def sum_n(n):
    a, b = 1, 1
    for i in range(n - 1):
        a /= (-2)
        b += a
    return b


n = int(input('введите число: '))
print(summ_n(n))
