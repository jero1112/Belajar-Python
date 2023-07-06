a=5
for i in range(1,a):
    for j in range(1,i):
        print(i,end= '')
        a-=1
    print(' ')
b=4
for i in range(0,b):
    for j in range(0,i+1):
        print('',end='')
    for k in range(0,b):
        print('*',end='')
    i-=1
    print('')