soma = 0

for i in range(1, 7):  # Usuário insere 6 números
    num = (int(input(f'Digite o {i}º número: ')))
    if num % 2 == 0:  # Se o número for par
        soma += num

print(f'A soma dos números pares digitados é {soma}')

