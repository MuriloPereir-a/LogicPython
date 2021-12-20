x = int(input('Enter value for X: '))
y = int(input('Enter value for Y: '))
c = 0
print('[1] Sum')
print('[2] Multiply')
print('[3] Higher')
print('[4] New numbers')
print('[5] Get out')

while c != 5:
    c = int(input('Choose one: '))
    if c == 1:
        print('Sum: {}'.format(x+y))
    if c == 2:
        print('Mult: {}'.format(x*y))
    if c == 3:
        if x>y:
            print('Higher: {}'.format(x))
        else:
            print('Higher: {}'.format(y))
    if c == 4:
        x = int(input('New value for X: '))
        y = int(input('New value for Y: '))
    if c == 5:
        print('Bye!')
