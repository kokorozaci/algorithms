"""Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
которые не меньше медианы, в другой — не больше медианы.."""

from random import shuffle, randint

m = 9
num = [i for i in range(2*m + 1)]
num1 = [randint(-50, 50) for i in range(2*m + 1)]
num2 = [7, 13, 18, 10, 12, 9, 6, 1, 8, 14, 16, 9, 17, 3, 15, 4, 5, 11, 2]  # если в массиве медиана встречается 2 раза
# то это не медиана? Программа должна выдавать ошибку или находить значение этого числа?...
shuffle(num)
print(num)

def median(array):
    i = 0
    min_m = None
    max_m = None
    for n in range(len(array)):
        if min_m and array[n] < min_m:
            continue  # если число меньше элемента меньшего чем медиана сразу проверяем следующее число
        elif max_m and array[n] > max_m:
            continue  # то же для большего
        for nn in array:
            if array[n] > nn:
                i += 1
            elif array[n] < nn:
                i -= 1
        print(array[n], i)  # прмежуточные значения
        if not i:
            return array[n]  # если количество элементов до и после числа равно, то оно медиана, дальше не ищем
        elif i > 0:
            max_m = array[n]
            i = 0
        elif i < 0:
            min_m = array[n]
            i = 0

med = median(num)
print(med)