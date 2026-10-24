total=0
while True:
    a=int(input('enter a number'))
    b=int(input('enter a number'))
    operator=input('enter a operator')
    #user=input('if you want to continue{y/N}')
    add=a+b
    sub=a-b
    mul=a*b
    div=a/b
    if operator=='+':
        print(f'addition {add}')
        total+=add
    elif operator=='-':
        print(f'subtraction{sub}')
        total+=sub
    elif operator=='*':
        print(f'multiplication{mul}')
        total+=mul
    elif operator=='/':         
        print(f'division{div}')
        total+=div
    else:
        print('invalid operator')
    user=input('if you want to continue{Y/N}').lower()
    if user=='n':
        print(f'total calculation :{total}')
        break
