abc = 'a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z'
abc = abc.split(',')
i = int(input('Введите номер буквы в алфавите: '))
print(abc.pop(i-1))
