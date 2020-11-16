numeros = (float(input('Digite o 1º número: ')), float(input('Digite o 2º número: ')),
           float(input('Digite o 3º número: ')), float(input('Digite o 4º número: ')))

print(f'Você digitou os valores {numeros}')
print(f'O valor 9 apareceu {numeros.count(9)} vezes.')
if 3 not in numeros:
    print('O valor 3 não aparece em nenhuma posição.')
else:
    print(f'A primeira posição em que o valor 3 aparece: {numeros.index(3)+1}ª')
print(f'Os números pares são: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')