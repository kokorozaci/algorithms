"""
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за четыре квартала
для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и
отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""

from collections import defaultdict

dict_a = defaultdict(tuple)
for _ in range(int(input('Введите число предприятий: '))):
    a = input('Название предприятия: ')
    dict_a[a] = (int(input('Прибыль за первый квартал: ')),
                 int(input('Прибыль за второй квартал: ')),
                 int(input('Прибыль за третий квартал: ')),
                 int(input('Прибыль за четвёртый квартал: ')))

mean_value = sum(map(sum, dict_a.values()))/len(dict_a)

print('Средняя прибыль: ', mean_value)
val_more_mean = []
val_smaller_mean = []
for k, v in dict_a.items():
    if sum(v) > mean_value:
        val_more_mean.append((k, sum(v)))
    else:
        val_smaller_mean.append((k, sum(v)))
print('Предприятия с прибылью выше среднего:')
[print(f'{n[0]}. Прибыль - {n[1]}') for n in val_more_mean]
print('Предприятия с прибылью ниже среднего:')
[print(f'{n[0]}. Прибыль - {n[1]}') for n in val_smaller_mean]

