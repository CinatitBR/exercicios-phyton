'''n = int(input('Digite um número  para descobrir seu fatorial: '))
i = n
resultado = 1
print(f'O fatorial de {n}! = ', end='')
while i > 0:
    print(f'{i}', end='')
    if i > 1:
        print('x', end='')
    elif i == 1:
        print(' = ', end='')
    resultado = resultado * i
    i -= 1
print(f'{resultado}')'''

# Com FOR
n = int(input('Digite um número  para descobrir seu fatorial: '))
i = 0
resultado = 1

for i in range(n, 0, -1):
    resultado = resultado * i

print(f'O fatorial de {n}! é {resultado}')
