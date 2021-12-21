'''Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar
quantas cédulas de cada valor serão entregues. OBS:
considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1'''

withD = int(input('withdrawal amount: '))
total = withD
ballot = 50
ballots = 0
while True:
    if total >= ballot:
        total -= ballot
        ballots += 1
    else:
        if ballots > 0:
            print(f'{ballots} bills of ${ballot}')
        if ballot == 50:
            ballot = 20
        elif ballot == 20:
            ballot = 10
        elif ballot == 10:
            ballot = 1
        ballots = 0
        if total == 0:
            break