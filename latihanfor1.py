# segitiga siku2 rata kiri atas
a= 8
for i in range(0,a):
    for j in range(0,a):
        print('*',end='')
    a-=1
    print('')
print('=================')

#segitiga siku2 rata kiri bawah
b=8
for i in range(0,b):
    for j in range(0,i+1):
        print('*',end=(''))
    print('')
print('==================')

#segitiga siku2 rata kanan atas
c= 8
for i in range(0,c):
    for j in range(0,i):
        print(' ',end='')
    for k in range(0,c):
        print('*',end='')
    c-=1
    print('')
print('==================')

#segitiga siku2 rata kanan bawah
d= 8
for i in range(0,d):
    for j in range(0,d-1):
        print(' ',end='')
    for k in range(0,i+1):
        print('*',end='')
    d-=1
    print('')
print('==================')

#persegi
e= 8
for i in range(0,e):
    for j in range(0,e):
        print('*',end='')
    for k in range(0,i):
        print('*',end='')
    e-=1
    print(' ')
print('==================')

f=8
for i in range(0,f):
    for j in range(0,i):
        print('',end=' ')
    for k in range(0,f):
        print('*',end=' ')
        f-=1
    print(' ')