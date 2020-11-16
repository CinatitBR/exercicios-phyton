'''frase = list(str(input('Digite uma frase: ')).lower().replace(' ', ''))  # T e s t e
compFrase = []

for i in range(len(frase) - 1, -1, -1):  # Inverte a frase digitada e armazena na variável compFrase
    compFrase.append(frase[i])

if frase == compFrase:  # Compara frase inicial com sua forma invertida
    print(f'A frase digitada É um palíndromo.')
else:
    print(f'A frase digitada NÃO é um palíndromo.')'''

# Ou
frase = str(input('DIgite uma frase: ')).replace(' ', '').upper()
invFrase = frase[::-1]

if frase == invFrase:
    print(f'O inverso de {frase} é {invFrase}')
    print('Ela É UM PALÍNDROME.')
else:
    print(f'O inverso de {frase} é {invFrase}')
    print('Ela NÃO é um palíndrome.')


