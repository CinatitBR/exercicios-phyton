numeros = []
for n in range(5):
    numeros.append(int(input(f'Digite o {n+1}º número: ')))
print(f'Os números digitados foram: {numeros}')
print(f'O maior valor digitado foi {max(numeros)}, nas posições ', end='')  # Maior valor digitado
for p, n in enumerate(numeros):
    if n == max(numeros):
        print(f'{p}...', end='')
print(f'\nO menor valor digitado foi {min(numeros)}, nas posições ', end='')  # Menor valor digitado
for p, n in enumerate(numeros):
    if n == min(numeros):
        print(f'{p}...', end='')