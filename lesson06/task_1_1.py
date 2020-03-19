"""2. Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5)

1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных
программах в рамках первых трех уроков. Проанализировать результат и определить
программы с наиболее эффективным использованием памяти.
Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
b. написать 3 варианта кода (один у вас уже есть);
проанализировать 3 варианта и выбрать оптимальный;
c. результаты анализа (количество занятой памяти в вашей среде разработки)
вставить в виде комментариев в файл с кодом. Не забудьте указать версию и
разрядность вашей ОС и интерпретатора Python;
d. написать общий вывод: какой из трёх вариантов лучше и почему.
"""
import sys

print(sys.version, sys.platform)
# Python: 3.7.3 (default, Apr 24 2019, 15:29:51) OS: [MSC v.1915 64 bit (AMD64)] win32


def show_size(x, level=0):
    print('\t' * level, f'type= {x.__class__}, size= {sys.getsizeof(x)}, object= {x}')

    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_size(xx, level + 1)
        elif not isinstance(x, str):
            for xx in x:
                show_size(xx, level + 1)


# Вариант 1

def counter(num):
    a = 0
    b = 0
    print("a: ", end=''), show_size(a)
    print("b: ", end=''), show_size(b)
    print("num: ", end=''), show_size(num)
    while num > 0:
        if (num%10)%2 == 0:
            a += 1
        else: b += 1
        num //= 10
        print("a: ", end=''), show_size(a)
        print("b: ", end=''), show_size(b)
        print("num: ", end=''), show_size(num)
    return  f'четных цифр: {a}, нечетных цифр: {b}'

num = int(input('введите число: '))
print(counter(num))
#
# введите число: 7895533505
# a:  type= <class 'int'>, size= 24, object= 0
# b:  type= <class 'int'>, size= 24, object= 0
# num:  type= <class 'int'>, size= 32, object= 7895533505
# a:  type= <class 'int'>, size= 24, object= 0
# b:  type= <class 'int'>, size= 28, object= 1
# num:  type= <class 'int'>, size= 28, object= 789553350
# a:  type= <class 'int'>, size= 28, object= 1
# b:  type= <class 'int'>, size= 28, object= 1
# num:  type= <class 'int'>, size= 28, object= 78955335
# a:  type= <class 'int'>, size= 28, object= 1
# b:  type= <class 'int'>, size= 28, object= 2
# num:  type= <class 'int'>, size= 28, object= 7895533
# a:  type= <class 'int'>, size= 28, object= 1
# b:  type= <class 'int'>, size= 28, object= 3
# num:  type= <class 'int'>, size= 28, object= 789553
# a:  type= <class 'int'>, size= 28, object= 1
# b:  type= <class 'int'>, size= 28, object= 4
# num:  type= <class 'int'>, size= 28, object= 78955
# a:  type= <class 'int'>, size= 28, object= 1
# b:  type= <class 'int'>, size= 28, object= 5
# num:  type= <class 'int'>, size= 28, object= 7895
# a:  type= <class 'int'>, size= 28, object= 1
# b:  type= <class 'int'>, size= 28, object= 6
# num:  type= <class 'int'>, size= 28, object= 789
# a:  type= <class 'int'>, size= 28, object= 1
# b:  type= <class 'int'>, size= 28, object= 7
# num:  type= <class 'int'>, size= 28, object= 78
# a:  type= <class 'int'>, size= 28, object= 2
# b:  type= <class 'int'>, size= 28, object= 7
# num:  type= <class 'int'>, size= 28, object= 7
# a:  type= <class 'int'>, size= 28, object= 2
# b:  type= <class 'int'>, size= 28, object= 8
# num:  type= <class 'int'>, size= 24, object= 0
# четных цифр: 2, нечетных цифр: 8
