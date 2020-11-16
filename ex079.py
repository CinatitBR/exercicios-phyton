numeros = []
while True:
    n = int(input('Digite um número: '))
    if n not in numeros:
        numeros.append(n)
        print('Número adicionado com sucesso!')
    else:
        print(f'O número é repetido, portanto não foi adicionado.')
    op = ' '
    while op not in 'sn':
        op = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    if op == 'n':
        break
print('-=-' * 15)
print(f'Os números adicionados foram {sorted(numeros)}')