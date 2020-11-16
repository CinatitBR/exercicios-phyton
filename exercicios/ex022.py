nome = str(input('Digite seu nome completo: ')).strip()

print(f'Nome com todas as letras maiúsculas: {nome.upper()}')
print(f'Nome com todas as letras minúsculas: {nome.lower()}')
print(f'Total de letras do seu nome: {len(nome) - nome.count(" ")}')
nome = nome.split()
print(f'Seu primeiro nome é {nome[0]} e ele tem {len(nome[0])} letras')