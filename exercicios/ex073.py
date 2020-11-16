tabela = ('Flamengo', 'Palmeiras', 'Santos', 'São Paulo', 'Corinthians', 'Internacional',
          'Grêmio', 'Bahia', 'Athletico Paranaense', 'Goiás', 'Vasco da Gama', 'Atlético',
          'Botafogo', 'Fortaleza', 'Ceará SC', 'Fluminense', 'Cruzeiro', 'CSA', 'Chapecoense',
          'Avaí')

print(f'5 primeiros colocados: ', end='')
for time in range(0, 5):
    if time != 4:
        print(tabela[time], end=', ')
    else:
        print(tabela[time], end='.')

print(f'\n\nUltimos 4 colocados: ', end='')
for time in range(16, 20):
    if time != 19:
        print(tabela[time], end=', ')
    else:
        print(tabela[time], end='.')

print(f'\n\nTimes em ordem alfabética: {sorted(tabela)}')
print(f'\nO time Chapecoense está na posição {tabela.index("Chapecoense") + 1}.')

