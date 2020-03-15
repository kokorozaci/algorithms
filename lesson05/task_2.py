"""
Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив,
элементы которого — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’]
"""

from collections import deque, Counter

HEX_STR = '0123456789ABCDEF'
HEX_NUM = {n: i for i, n in enumerate(HEX_STR)}
BASE = 16

a = [i for i in ((input('Введите первое число: ')).upper())]
b = [i for i in ((input('Введите второе число: ')).upper())]


def sum_col(a, b):
    sum_ab = Counter({n+1: HEX_NUM[i] for n, i in enumerate(reversed(a))}) + \
          Counter({n+1: HEX_NUM[i] for n, i in enumerate(reversed(b))})
    d = deque()
    for i in range(1, len(sum_ab)+2):
        if sum_ab[i] - BASE >= 0:
            sum_ab[i] -= BASE
            sum_ab[i+1] += 1
        if i == len(sum_ab)+1 and sum_ab[i+1] == 0:
            break
        d.appendleft(HEX_STR[sum_ab[i]])
    return list(d)


print(f'0x{"".join(a)} + 0x{"".join(b)} = 0x{"".join(sum_col(a,b))}')


def hex_mul_simple(a, b):  # умножение на цифру
    c = a.copy()
    for _ in range(HEX_NUM[b]-1):
        c = sum_col(c, a)
    return c


def hex_mul(a, b):
    cnt = 0
    res = ['0']
    for n in reversed(b):
        c = hex_mul_simple(a, n)
        for _ in range(cnt):
            c.append('0')
        cnt += 1
        res = sum_col(res, c)
    return res


print(f'0x{"".join(a)} * 0x{"".join(b)} = 0x{"".join(hex_mul(a, b))}')
