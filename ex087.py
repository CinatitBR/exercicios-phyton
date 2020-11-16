matriz = [
    [],
    [],
    []
]
vpar = c3 = maior = 0
for v in range(0, 3):  # Representa cada vetor interno
    for i in range(0, 3):  # Representa cada índice do vetor interno (voluna)
        matriz[v].append(int(input(f'Valor da posição {[v, i]}: ')))  # Número será adicionado no final do vetor interno
        if matriz[v][i] % 2 == 0:  # Soma valores pares
            vpar += matriz[v][i]
        if i == 2:  # Soma da 3ª coluna
            c3 += matriz[v][2]
        if v == 1:  # Se for a 2ª linha (vetor 1)
            if matriz[v][i] > maior:
                maior = matriz[v][i]
print('-=' * 30)
for v in range(0, 3):  # Esse laço organizará o desenho
    for n in range(0, 3):
        print(f'[ {matriz[v][n]:^3} ]', end='')
    print()
print('-=' * 30)
print(f'A soma dos números pares é {vpar}.')
print(f'A soma dos números da 3ª coluna é {c3}.')
print(f'O maior número da 2ª linha é {maior}.')