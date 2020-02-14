"""Написать программу, которая генерирует в указанных пользователем границах:
a. случайное целое число,
b. случайное вещественное число,
c. случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно."""

import random as rd
abc = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'
start = input('Введите начальную границу диапазона: ')
stop = input('Введите конечную границу диапазона: ')
if '.' in start or '.' in stop:
    start, stop = float(start), float(stop)
    print(rd.uniform(start, stop))
elif start in abc and stop in abc:
    abc = abc.split(',')
    start_i = abc.index(start)
    stop_i = abc.index(stop)
    i = rd.randint(start_i, stop_i)
    print(abc.pop(i))
else:
    start = int(start)
    stop = int(stop)
    print(rd.randint(start, stop))
