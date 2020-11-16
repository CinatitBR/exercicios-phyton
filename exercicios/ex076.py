produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20,
            'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print(f'{"LISTA DE MATERIAIS":=^32}')
for i in range(0, len(produtos), 2):  # Verifica cada elemento da tupla, pulando de 2 para pegar apenas o nome do produto
    print(f'{produtos[i]:.<22}R$ {int(produtos[i + 1]):>7.2f}')
print('=' * 32)