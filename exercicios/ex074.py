from random import randint
numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(f'Os cinco números são: ', end='')
for n in numeros:  # Exibe números sorteados
    print(n, end=' ')
print(f'\nO MAIOR número é {max(numeros)}')
print(f'O MENOR número é {min(numeros)}')
