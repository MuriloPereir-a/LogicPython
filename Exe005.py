'''Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:

A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''
mans = womLess20 = more18 = 0


while True:
    age = int(input('Age: '))
    sex = ' '
    while sex not in 'MF':
        sex = str(input('Sex [M/F]: ')).strip().upper()[0]
    if age > 18:
        more18 += 1
    if sex == 'M':
        mans += 1
    if sex == 'F' and age <20:
        womLess20 += 1
    rep = ' '
    while rep not in 'YN':
        rep = str(input('Want to continue [Y/N]: ')).strip().upper()[0]
    if rep == 'N':
        break


print(f'More than 18: {more18}... Mans: {mans}... Women under 20: {womLess20}')



