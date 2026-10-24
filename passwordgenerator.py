import random
print('welcome to password generator')
letters="a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"
numbers='1','2','3','4','5','6','7','8','9','0'
symbols='@','!','#','$','%','^','&','*','(',')','+','='
n_letters=int(input('enter no. of letters in password'))
n_numbers=int(input('enter no. of numbers in numbers'))
n_symbols=int(input('enter no. of symbols in symbols'))
password=[]
for i in range(0,n_letters):
    password+=random.choice(letters)
for i in range(0,n_numbers):
    password+=random.choice(numbers)
for i in range(0,n_symbols):
    password+=random.choice(symbols)
random.shuffle(password)
#print(password)
passwords=''
for i in password:
    passwords+=i
print(passwords)

    
