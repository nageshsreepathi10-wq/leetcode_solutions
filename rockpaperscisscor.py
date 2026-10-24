import random
userchoice=input('enter rock,paper,scissor=')
moves=['rock','paper','scissor']
compchoice=random.choice(moves)
print(f'userchoice:  {userchoice}\ncompchoice:  {compchoice}')
if userchoice==compchoice:
    print('tie')
elif (userchoice=='rock' and compchoice=='scissor') or (userchoice=='paper' and compchoice=='rock') or (userchoice=='scisscor' and compchoice=='paper'):
    print('you win')
elif userchoice in moves:
    print('comp win')
else:
    print('invalid')
