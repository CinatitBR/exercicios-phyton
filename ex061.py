termo = int(input('Digite o 1º termo da P.A: '))
razao = int(input('Digite a razão da P.A: '))
i = 0

while i < 10:
    print(termo, end=' | ')
    termo += razao
    i += 1

