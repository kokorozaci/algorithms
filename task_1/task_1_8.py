"""Вводятся три разных числа.
Найти, какое из них является средним (больше одного, но меньше другого)"""

a = int(input('Введите a: '))
b = int(input('Введите b: '))
c = int(input('Введите c: '))
if b < a < c or c < a < b:
    print(f'Среднее число: {a}')
elif a < b < c or c < b < a:
    print(f'Среднее число: {b}')
else:
    print(f'Среднее число: {c}')
