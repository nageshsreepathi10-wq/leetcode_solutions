while True:
    balance=10000
    print('welcome to ATM')
    print('1.check balance')
    print('2.deposit amount')
    print('3.withdraw amount')
    print('4.exit')
    choice=int(input('enter the choice'))

    if choice==1:
        print(f'balance is:{balance}')
    elif choice==2:
        amount=int(input('enter the amount to deposit'))
        if amount>0:
            balance+=amount
            print('amount is deposited successfully')
            print(f' your available balance is:{balance}')
        else:
            print('the amount is less')
    elif choice==3:
        amount=int(input('enter the amount'))
        if amount<=balance:
            balance-=amount
            print('amount withdrawn successfully')
            print(f'your available balance is:{balance}')
        else:
            print('insufficient amount')
    elif choice==4:
        break
    else:
        print('invalid option')
            
