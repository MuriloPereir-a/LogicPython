from random import randint
from time import sleep

itens = ('Rock','Paper','Scissors')
pc = randint(0,2)
print('''Opções: 
[ 0 ] Rock
[ 1 ] Paper 
[ 2 ] Scissors''')
play = int(input('Choose one: '))
print('ONE')
sleep(1)
print('TWO')
sleep(1)
print('THREE')
sleep(1)
print('-=-'*9)
print('PC CHOSE: {}'.format(itens[pc]))
print('PLAYER CHOSE: {}'.format(itens[play]))

print('-=-'*9)

if pc == 0:
    if play == 0:
        print('Draw')
    elif play == 1:
        print('Player won!')
    elif play == 2:
        print('PC won!')
if pc == 1:
    if play == 0:
        print('PC won!')
    elif play == 1:
        print('Draw!')
    elif play == 2:
        print('Player won!')
if pc == 2:
    if play == 0:
        print('Player won')
    elif play == 1:
        print('PC won!')
    elif play == 2:
        print('Draw!')