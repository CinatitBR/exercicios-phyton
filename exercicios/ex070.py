total = pro1000 = c = precoBarato = 0
nomeBarato = ''
while True:
    nome = str(input('Nome do produto: ')).strip().upper()
    preco = float(input('Preço do produto: R$'))
    c += 1  # Verifica se está no 1º laço
    total += preco  # Gasto total
    if preco > 1000:  # Produtos que custam mais de R$1000
        pro1000 += 1
    if c == 1 or preco < precoBarato:  # Inicializar produto mais barato se estiver no 1º laço
        nomeBarato = nome
        precoBarato = preco
    op = ' '  # Inicialização da variável op
    while op not in 'SN':  # Usuário escolhe se quer continuar ou não
        op = str(input('Você quer continuar comprando? [S/N]')).strip().upper()[0]
    if op in 'N':
        break
print(f'O total gasto nessa compra foi R${total:.2f}')
print(f'{pro1000} produtos comprados custam mais de R$1000.00')
print(f'O produto mais barato foi: {nomeBarato} - R${precoBarato:.2f}')
