maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'{p}ª pessoa, informe seu peso:  '))
    if p == 1:
        menor = peso
    elif peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso

print(f'O maior peso é {maior}')
print(f'O menor peso é {menor}')







