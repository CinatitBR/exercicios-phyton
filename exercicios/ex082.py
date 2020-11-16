numeros = []
pares = []
impares = []
while True:  # Usuário digita todos os números
    n = int(input('Digite um número: '))
    numeros.append(n)
    op = ' '
    while op not in 'sn':
        op = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    if op == 'n':
        break
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print('-=-' * 15)
print(f'Todos os números digitados: {numeros}')
print(f'Números PARES: {pares}')
print(f'Números ÍMPARES: {impares}')