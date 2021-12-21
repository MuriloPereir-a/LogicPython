'''Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''

id = cheap = tot = mThan1K = count = 0
cheapest = ' '
while True:
    id += 1
    name = str(input(f'Product #{id} name: '))
    price = float(input(f'Product #{id} price: '))
    tot += price
    count += 1
    if count == 1:
        cheap = price
    if count >= 2 and price < cheap:
        cheap = price
        cheapest = name
    if price > 1000:
        mThan1K += 1
    rep = ' '
    while rep not in 'YN':
        rep = str(input('Want to continue? [Y/N]')).strip().upper()[0]
    if rep == 'N':
        break
print('\n')
print(f'Total: {tot}')
print(f'More than $1000: {mThan1K}')
print(f'Cheapest product: {cheapest} (${cheap})')


