numeros = [
    [],  # Par [0]
    []   # Impar [1]
]
for i in range(1, 8):
    n = int(input(f'Digite o {i} número: '))
    if n % 2 == 0:  # Par
        numeros[0].append(n)
    else:  # Impar
        numeros[1].append(n)
numeros[0].sort()
numeros[1].sort()
print(f'Os números PARES são: {numeros[0]}')
print(f'Os números ÍMPARES são: {numeros[1]}')



