print('Вевдите координаты 2-х точек')
x1 = int(input('Введите x1: '))
y1 = int(input('Введите y1: '))
x2 = int(input('Введите x2: '))
y2 = int(input('Введите y2: '))
k = (y1-y2)/(x1-x2)
b = y1-k*x1
print(f'y = {k} x + {b}')