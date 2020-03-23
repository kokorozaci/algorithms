"""Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный случайными числами
на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
Примечания:
a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут."""

import random as rd

num = [i for i in range(-50, 50)]
rd.shuffle(num)
print(num)

def bubble_sort(array):
    n = 1
    while n < len(array):
        j = 0
        for i in range(len(array) - n):
            if array[i] < array[i + 1]:
                array[i], array[i+1] = array[i+1], array[i]
                j += 1
        n += 1
        if not j:  # если массив отсортировался раньше, сортировка прекращается
            return

bubble_sort(num)
print(num)