"""Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы."""

import random as rd

num = [i for i in range(50)]
rd.shuffle(num)
print(num)


def merge_sort(array, revers=False):
    if len(array) < 2:
        return array[:]
    sep_num = len(array) // 2
    left = merge_sort(array[:sep_num], revers=revers)
    right = merge_sort(array[sep_num:], revers=revers)
    sorted_array = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if revers:  # бонус с разворотом сортировки =))
            if left[i] > right[j]:
                sorted_array.append(left[i])
                i += 1
            else:
                sorted_array.append(right[j])
                j += 1
        else:
            if left[i] < right[j]:
                sorted_array.append(left[i])
                i += 1
            else:
                sorted_array.append(right[j])
                j += 1
    while i < len(left):
        sorted_array.append(left[i])
        i += 1
    while j < len(right):
        sorted_array.append(right[j])
        j += 1
    return sorted_array


sorted_array = merge_sort(num, revers=False)
print(sorted_array)
