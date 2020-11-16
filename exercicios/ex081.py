numeros = []
i = 0
while True:
    n = int(input('Digite um número: '))  # 3, 9, 2, 5, 0
    if i == 0 or n <= numeros[-1]:  # Se for a 1ª vez do laço ou se n for menor que último item da lista
        numeros.append(n)  # 9, 5, 3, 2, 0
    else:
        for p in range(len(numeros)):  # Esse laço cobre todos os índices do vetor
            if n >= numeros[p]:
                numeros.insert(p, n)
                break
    i += 1
    op = ' '
    while op not in 'sn':
        op = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    if op == 'n':
        break
print(f'Números digitados em formato Decrescente: {numeros}')
print(f'{len(numeros)} números foram digitados.')
print(f'O valor 5 ESTÁ na lista, na posição {numeros.index(5)}!' if 5 in numeros else 'O valor 5 NÃO está na lista!')

