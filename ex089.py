dados = [
    [],  # Nome [0]
    [],  # Notas [1]
    []   # Média [2]
]
v = 0  # Vetor
i = 0  # Índice
e = 0  # Elemento
while True:
    dados[0].append(str(input('Nome: ')))  # Adiciona nome na lista de nomes [0]
    dados[1].append([])  # Cria uma nova lista em [1] para receber duas notas
    dados[1][v].append(float(input('1ª nota: ')))  # Acessa o vetor interno da lista 'notas' e adiciona as duas notas
    dados[1][v].append(float(input('2ª nota: ')))
    v += 1  # Representa o vetor dentro de notas [1]
    r = ' '
    while r not in 'sn':
        r = str(input('Deseja continuar? [S/N] ')).strip().lower()[0]
    if r == 'n':
        break

for v in dados[1]:  # v representa vetores internos de dados[1], onde cada um contém duas notas
    dados[2].append(sum(v) / 2)  # Soma notas e adiciona no vetor média [2]

print('-=' * 30)
print(f'{"Nº":<5} {"Nome":<7} {"Média"}')
print('-' * 30)
for i, e in enumerate(dados[0]):  # 'i' representa índice, 'e' representa elemento
    print(f'{i:<5} {e:<7} {dados[2][i]:.1f}')
print('-' * 30)

while True:  # Usário escolhe aluno para ver notas
    r = int(input('Você deseja ver a nota de qual aluno? (-1 para encerrar): '))
    if r == -1:
        break
    print('-' * 35)
    print(f'As notas do(a) {dados[0][r]} são {dados[1][r]}.')
    print('-' * 35)