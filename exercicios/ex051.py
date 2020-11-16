termo1 = int(input('Digite o 1º termo da P.A: '))
razao = int(input('Digite a razão desta P.A: '))
decimo = termo1 + (10 - 1) * razao

for i in range(termo1, decimo + 1, razao):
    print(i, end=' ')
