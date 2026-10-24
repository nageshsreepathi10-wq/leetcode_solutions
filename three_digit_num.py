#num=int(input())
#count=0
'''
for i in num:
    count+=1
if count==3:
    print('three digit number')
else:
    print('not a three digit number')'''
temp=0
'''while num>0:
    temp=num%10
    num=num//10
    count+=1
if count==3:
    print('three digit number')
else:
    print('not')'''


num=int(input())
a,b=0,1
for i in range(num):
    print(a,end=' ')
    a,b=b,a+b
    
    
    
