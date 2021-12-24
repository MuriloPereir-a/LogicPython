#Construa uma lista (usuário há de a formar), maior e menor valores com suas respectivas posições.

c = int(input('How many values?: '))
xwt = []
for i in range(0, c):
    xwt.append(int(input(f'#{i + 1}° value: ')))
print(xwt)
print(f'Biggest value is: {max(xwt)}')
print(f'Smaller value is: {min(xwt)}')
print(f'Biggest in: {xwt.index(max(xwt))+1} pos, and smaller in: {xwt.index(min(xwt))+1}')
