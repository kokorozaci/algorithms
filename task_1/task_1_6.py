a = float(input('Длина отрезка 1: '))
b = float(input('Длина отрезка 2: '))
c = float(input('Длина отрезка 3: '))
if a+b > c and a+c > b and b+c > a:
    if a == c and c == b:
        print('Равносторонний треугольник')
    elif a != c and b != a and b != c:
        print('Разносторониий треуголиник')
    else:
        print('Равнобедренный треугольник')
else:
    print('Треугольник не существует')
