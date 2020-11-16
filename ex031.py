d = float(input('Qual a distância total da viagem (em Km)? '))

if d <= 200:
    preco = 0.50 * d
    print(f'A distância da viagem é {d}Km.\nO preço da passagem será R${preco:.2f}')
else:
    preco = 0.45 * d
    print(f'A distância da viagem é {d}Km.\nO preço total da passagem será R${preco:.2f}')
