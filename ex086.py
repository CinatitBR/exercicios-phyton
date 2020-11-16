matriz = [
    [],
    [],
    []
]

for v in range(0, 3):  # Representa cada vetor interno
    for i in range(0, 3):  # Representa cada índice do vetor interno
        matriz[v].append(int(input(f'Valor da posição {[v, i]}: ')))
print('-=' * 30)
for v in range(0, 3):  # Organizará o desenho
    for i in range(0, 3):
        print(f'[ {matriz[v][i]:^3} ]', end='')
    print()