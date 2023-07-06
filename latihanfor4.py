#kiri bawah
t = 5

for i in range(1,t+1):
    print(i*'*')

#kiri atas  
t=5
for i in range(1,t+1):
    print((t-i+1)* '*')

t=5
for i in range(1,t+1):
    print((t-i+1)* ' ' + (i*'*'))
    
t=5
for i in range(1,t+1):
    print((i*' ')+(t-i+1)* '*' )
    
print('===========')
t=5
for i in range(1,t+1):
    print((t-i+1)* ' ' + (i*'*')+ ((i-1)*'*'))
  
t = 5
for i in range(1,t+1):
    print((i *' ')+(t-i+1)* '*' +(t-i)* '*')
      

t = 5 
for i in range(1,t+1):
    print((t-i+1)*'*' + (i*'*'))