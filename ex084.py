pessoas = []
dados = []  # Nome e Peso
maiorPeso = menorPeso = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: Kg ')))
    if len(pessoas) == 0:
        maiorPeso = menorPeso = dados[1]
    else:
        if dados[1] > maiorPeso:  # MAIOR peso
            maiorPeso = dados[1]
        if dados[1] < menorPeso:  # MENOR peso
            menorPeso = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    r = ' '
    while r not in 'sn':
        r = str(input('Deseja cadastrar mais pessoas? [S/N] ')).strip().lower()[0]
    if r == 'n':
        break
print(f'Foram {len(pessoas)} pessoas cadastradas.')
print(f'O maior peso cadastrado foi {maiorPeso}Kg. Peso de ', end='')  # Maior peso
for v in pessoas:  # Para cada vetor interno do array pessoas
    if v[1] == maiorPeso:
        print(f'[{v[0]}] ', end='')
print(f'\nO menor peso cadastrado {menorPeso}Kg. Peso de ', end='')
for v in pessoas:
    if v[1] == menorPeso:
        print(f'[{v[0]}] ', end='')