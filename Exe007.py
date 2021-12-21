'''Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar
quantas cédulas de cada valor serão entregues. OBS:
considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1'''

withD = int(input('withdrawal amount: '))
total = withD
bill = 50
bills = 0
while True:
    if total >= bill:
        total -= bill
        bills += 1
    else:
        if bills > 0:
            print(f'{bills} bills of ${bill}')
        if bill == 50:
            bill = 20
        elif bill == 20:
            bill = 10
        elif bill == 10:
            bill = 1
        bills = 0
        if total == 0:
            break