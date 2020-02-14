"""Пользователь вводит две буквы. Определить,
на каких местах алфавита они стоят, и сколько между ними находится букв."""

abc = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'
abc = abc.split(',')
start = input('Введите первую букву: ')
stop = input('Введите вторую букву: ')
a_i = abc.index(start)+1
b_i = abc.index(stop)+1
print(f'номер {start}: {a_i}, номер {stop}: {b_i}, количество '
      f'бкув между {start} и {stop} = {abs(a_i-b_i)}')
