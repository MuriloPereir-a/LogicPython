#ler valores, mostrar o maior e o menor entre eles e mostrar a média de todos os valores
r = ''
s = 0
smaller = 0
bigger = 0
c = 0
while r != 'n':
    x = int(input('Enter value: '))
    print('Want to continue [y/n]', end=' ')
    r = str(input())
    c = c + 1
    s += x
    if c == 1:
        bigger = x
        smaller = x
    if x > bigger:
        bigger = x
    if x < smaller:
        smaller = x

print('The biggest value is: {}. the smallest value is: {}. Their avg is: {:.2f}.'.format(bigger, smaller, s/c ))