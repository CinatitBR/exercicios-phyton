# Versão diminuída
cedulas = [50, 20, 10, 1]
valor = int(input('Digite o valor a ser sacado: R$'))
for i in cedulas:  # i irá cobrir todos os elementos da lista cédulas
    quant = valor // i  # Quantidade de notas i
    valor = valor % i
    if quant > 0:
        print(f'Total de {quant} notas de R${i:.2f}')

# Versão grande
'''cedula50 = cedula20 = cedula10 = cedula1 = 0
print('-=-' * 8)
print('      BANCO IGÃO')
print('-=-' * 8)
while True:
    valor = int(input('Digite o valor a ser sacado: R$'))
    if valor >= 50:
        cedula50 = valor // 50
        valor = valor % 50
        print(f'Total de {cedula50} cédulas de R$50.')
    if valor >= 20:
        cedula20 = valor // 20
        valor = valor % 20
        print(f'Total de {cedula20} cédulas de R$20.')
    if valor >= 10:
        cedula10 = valor // 10
        valor = valor % 10
        print(f'Total de {cedula10} cédulas de R$10.')
    if valor >= 1:
        cedula1 = valor // 1
        print(f'Total de {cedula1} cédulas de R$1.')
    print('-' * 30)
    op = str(input('Você quer sacar mais algum valor? [S/N] ')).strip().upper()[0]
    while op not in 'SN':
        op = str(input('Você quer sacar mais algum valor? [S/N] ')).strip().upper()[0]
    if op in 'N':
        print('Operação encerrada. Tenha um bom dia, volte sempre!')
        break'''
