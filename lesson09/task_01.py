"""1. Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
Требуется вернуть количество различных подстрок в этой строке.
Примечания:
* в сумму не включаем пустую строку и строку целиком;"""

import hashlib


def all_strings(s: str):
    assert len(s) > 0, 'Строка не может быть пустой'
    sum_s = 0
    len_s = len(s)
    sub_list = set()
    for i in range(1, len_s):
        for j in range((len_s - i + 1)):
            if hashlib.sha1(s[j:j + i].encode('utf-8')).hexdigest() not in sub_list and s[j:j + i] != ' ':
                sub_list.add(hashlib.sha1(s[j:j + i].encode('utf-8')).hexdigest())
        sum_s += len(sub_list)
        sub_list.clear()
    return sum_s


s = input('Введите строку: ')
print(all_strings(s))
