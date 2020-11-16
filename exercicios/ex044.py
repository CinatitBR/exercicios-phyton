preco = float(input('Qual o preço inicial do produto? R$'))
op = int(input('Qual a forma de pagamento? Digite:\n[ 1 ] Dinheiro/Cheque\n[ 2 ] à vista no cartão\n[ 3 ] em até 2x no cartão\n[ 4 ] 3x ou mais no cartão\n'))

if op == 1:
    print(f'O valor total a ser pago será R${preco - (10/100 * preco):.2f}')
elif op == 2:
    print(f'O valor total a ser pago será R${preco - (5/100 * preco):.2f}')
elif op == 3:
    print(f'Você vai pagar em 2 de R${preco / 2:.2f}')
    print(f'O valor total a ser pago será R${preco:.2f}')
elif op == 4:
    preco = preco + (20/100 * preco)
    op = int(input('Em quantas vezes você quer parcelar? '))
    print(f'Você vai pagar em {op}x de R${preco / op:.2f}')
    print(f'O valor total a ser pago será R${preco:.2f}')
else:
    print(f'A opção {op} é inválida! Tente novamente.')