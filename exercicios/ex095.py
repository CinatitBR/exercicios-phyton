jogadores = []
dados = {}

while True:
    dados['nome'] = str(input('Nome do jogador: '))
    dados['partidas'] = int(input('Quantas partidas você jogou? '))
    dados['gol_partida'] = []
    for i in range(dados['partidas']):
        dados['gol_partida'].append(int(input(f'Quantidade de gols na {i+1}ª partida: ')))
    dados['tot_gols'] = sum(dados['gol_partida'])
    jogadores.append(dados.copy())
    r = ' '
    while r not in 'SN':
        r = str(input('Deseja continuar cadastrando? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
print('-=' * 20)
print(f'{"Nº":<5} {"Nome"}')
for i, j in enumerate(jogadores):  # Para cada índice e jogador em jogadores
    print(f'{i:<5} {j["nome"]}')
print('-=' * 20)
while True:
    r = int(input('(-1 para cancelar) Você quer ver os detalhes de qual jogador? [Nº] '))
    if r == -1:
        break
    for key, v in jogadores[r].items():
        print(f'{key}: {v}')
print('PROGRAMA ENCERRADO')