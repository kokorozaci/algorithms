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


# Вариант 2

def counter(num):
    a = []
    print("a: ", end=''), show_size(a)
    while num > 0:
        a.append(num%10)
        num //= 10
        print("a: ", end=''), show_size(a)
    b = len([1 for c in a if c%2 == 0])
    c = len([1 for c in a if c%2 != 0])
    print("a: ", end=''), show_size(a)
    print("b: ", end=''), show_size(b)
    print("c: ", end=''), show_size(c)
    return  f'четных цифр: {b}, нечетных цифр: {c}'

num = int(input('введите число: '))
print(counter(num))
#
# введите число: 7895533505
# a:  type= <class 'list'>, size= 64, object= []
# a:  type= <class 'list'>, size= 96, object= [5]
# 	 type= <class 'int'>, size= 28, object= 5
# a:  type= <class 'list'>, size= 96, object= [5, 0]
# 	 type= <class 'int'>, size= 28, object= 5
# 	 type= <class 'int'>, size= 24, object= 0
# a:  type= <class 'list'>, size= 96, object= [5, 0, 5]
# 	 type= <class 'int'>, size= 28, object= 5
# 	 type= <class 'int'>, size= 24, object= 0
# 	 type= <class 'int'>, size= 28, object= 5
# a:  type= <class 'list'>, size= 96, object= [5, 0, 5, 3]
# 	 type= <class 'int'>, size= 28, object= 5
# 	 type= <class 'int'>, size= 24, object= 0
# 	 type= <class 'int'>, size= 28, object= 5
# 	 type= <class 'int'>, size= 28, object= 3
# a:  type= <class 'list'>, size= 128, object= [5, 0, 5, 3, 3]
# 	 type= <class 'int'>, size= 28, object= 5
# 	 type= <class 'int'>, size= 24, object= 0
# 	 type= <class 'int'>, size= 28, object= 5
# 	 type= <class 'int'>, size= 28, object= 3
# 	 type= <class 'int'>, size= 28, object= 3
# a:  type= <class 'list'>, size= 128, object= [5, 0, 5, 3, 3, 5]
# 	 type= <class 'int'>, size= 28, object= 5
# 	 type= <class 'int'>, size= 24, object= 0
# 	 type= <class 'int'>, size= 28, object= 5
# 	 type= <class 'int'>, size= 28, object= 3
# 	 type= <class 'int'>, size= 28, object= 3
# 	 type= <class 'int'>, size= 28, object= 5
# a:  type= <class 'list'>, size= 128, object= [5, 0, 5, 3, 3, 5, 5]
# 	 type= <class 'int'>, size= 28, object= 5
# 	 type= <class 'int'>, size= 24, object= 0
# 	 type= <class 'int'>, size= 28, object= 5
# 	 type= <class 'int'>, size= 28, object= 3
# 	 type= <class 'int'>, size= 28, object= 3
# 	 type= <class 'int'>, size= 28, object= 5
# 	 type= <class 'int'>, size= 28, object= 5
# a:  type= <class 'list'>, size= 128, object= [5, 0, 5, 3, 3, 5, 5, 9]
# 	 type= <class 'int'>, size= 28, object= 5
# 	 type= <class 'int'>, size= 24, object= 0
# 	 type= <class 'int'>, size= 28, object= 5
# 	 type= <class 'int'>, size= 28, object= 3
# 	 type= <class 'int'>, size= 28, object= 3
# 	 type= <class 'int'>, size= 28, object= 5
# 	 type= <class 'int'>, size= 28, object= 5
# 	 type= <class 'int'>, size= 28, object= 9
# a:  type= <class 'list'>, size= 192, object= [5, 0, 5, 3, 3, 5, 5, 9, 8]
# 	 type= <class 'int'>, size= 28, object= 5
# 	 type= <class 'int'>, size= 24, object= 0
# 	 type= <class 'int'>, size= 28, object= 5
# 	 type= <class 'int'>, size= 28, object= 3
# 	 type= <class 'int'>, size= 28, object= 3
# 	 type= <class 'int'>, size= 28, object= 5
# 	 type= <class 'int'>, size= 28, object= 5
# 	 type= <class 'int'>, size= 28, object= 9
# 	 type= <class 'int'>, size= 28, object= 8
# a:  type= <class 'list'>, size= 192, object= [5, 0, 5, 3, 3, 5, 5, 9, 8, 7]
# 	 type= <class 'int'>, size= 28, object= 5
# 	 type= <class 'int'>, size= 24, object= 0
# 	 type= <class 'int'>, size= 28, object= 5
# 	 type= <class 'int'>, size= 28, object= 3
# 	 type= <class 'int'>, size= 28, object= 3
# 	 type= <class 'int'>, size= 28, object= 5
# 	 type= <class 'int'>, size= 28, object= 5
# 	 type= <class 'int'>, size= 28, object= 9
# 	 type= <class 'int'>, size= 28, object= 8
# 	 type= <class 'int'>, size= 28, object= 7
# a:  type= <class 'list'>, size= 192, object= [5, 0, 5, 3, 3, 5, 5, 9, 8, 7]
# 	 type= <class 'int'>, size= 28, object= 5
# 	 type= <class 'int'>, size= 24, object= 0
# 	 type= <class 'int'>, size= 28, object= 5
# 	 type= <class 'int'>, size= 28, object= 3
# 	 type= <class 'int'>, size= 28, object= 3
# 	 type= <class 'int'>, size= 28, object= 5
# 	 type= <class 'int'>, size= 28, object= 5
# 	 type= <class 'int'>, size= 28, object= 9
# 	 type= <class 'int'>, size= 28, object= 8
# 	 type= <class 'int'>, size= 28, object= 7
# b:  type= <class 'int'>, size= 28, object= 2
# c:  type= <class 'int'>, size= 28, object= 8
# четных цифр: 2, нечетных цифр: 8