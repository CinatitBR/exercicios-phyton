dados_jogador = {
    'nome': str(input('Nome: ')),
    'partidas': int(input('Quantidade de partidas jogadas: ')),
    'gols_partida': []  # Quantidade de gols em cada partida
}
for i in range(dados_jogador['partidas']):  # Jogador insere quant de gols em cada partida
    dados_jogador['gols_partida'].append(int(input(f'Quantidade de gols na {i+1}ª partida: ')))
dados_jogador['tot_gols'] = sum(dados_jogador['gols_partida'])
print('-=' * 20)
for key, v in dados_jogador.items():
    print(f'{key}: {v}')
print('-=' * 20)
print(f'O jogador {dados_jogador["nome"]} jogou {dados_jogador["partidas"]} partidas.')
for i, gols in enumerate(dados_jogador['gols_partida']):
    print(f'{"=>":>5} Fez {gols} gols na {i+1}ª partida.')
print(f'Um total de {dados_jogador["tot_gols"]} gols.')