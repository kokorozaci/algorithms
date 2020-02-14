a = int(input('Введите a: '))
b = int(input('Введите b: '))
c = int(input('Введите c: '))
if b < a < c or (b > a > c and c < b):
    print(f'Среднее число: {a}')
elif a < b < c or (a > b > c and a > c):
    print(f'Среднее число: {b}')
else:
    print(f'Среднее число: {c}')
