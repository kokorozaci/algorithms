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


# Вариант 3

def counter(num):
    print("num: ", end=''), show_size(num)
    a = 0
    b = 0
    for i in num:
        if int(i)%2:
            b += 1
        else:
            a += 1
        print("a: ", end=''), show_size(a)
        print("b: ", end=''), show_size(b)
        print("i: ", end=''), show_size(i)
    return  f'четных цифр: {a}, нечетных цифр: {b}'

num = input('введите число: ')
print(counter(num))
#
# введите число: 7895533505
# num:  type= <class 'str'>, size= 59, object= 7895533505
# a:  type= <class 'int'>, size= 24, object= 0
# b:  type= <class 'int'>, size= 28, object= 1
# i:  type= <class 'str'>, size= 50, object= 7
# a:  type= <class 'int'>, size= 28, object= 1
# b:  type= <class 'int'>, size= 28, object= 1
# i:  type= <class 'str'>, size= 50, object= 8
# a:  type= <class 'int'>, size= 28, object= 1
# b:  type= <class 'int'>, size= 28, object= 2
# i:  type= <class 'str'>, size= 50, object= 9
# a:  type= <class 'int'>, size= 28, object= 1
# b:  type= <class 'int'>, size= 28, object= 3
# i:  type= <class 'str'>, size= 50, object= 5
# a:  type= <class 'int'>, size= 28, object= 1
# b:  type= <class 'int'>, size= 28, object= 4
# i:  type= <class 'str'>, size= 50, object= 5
# a:  type= <class 'int'>, size= 28, object= 1
# b:  type= <class 'int'>, size= 28, object= 5
# i:  type= <class 'str'>, size= 50, object= 3
# a:  type= <class 'int'>, size= 28, object= 1
# b:  type= <class 'int'>, size= 28, object= 6
# i:  type= <class 'str'>, size= 50, object= 3
# a:  type= <class 'int'>, size= 28, object= 1
# b:  type= <class 'int'>, size= 28, object= 7
# i:  type= <class 'str'>, size= 50, object= 5
# a:  type= <class 'int'>, size= 28, object= 2
# b:  type= <class 'int'>, size= 28, object= 7
# i:  type= <class 'str'>, size= 50, object= 0
# a:  type= <class 'int'>, size= 28, object= 2
# b:  type= <class 'int'>, size= 28, object= 8
# i:  type= <class 'str'>, size= 50, object= 5
# четных цифр: 2, нечетных цифр: 8