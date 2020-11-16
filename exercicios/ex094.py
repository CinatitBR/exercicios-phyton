pessoas = []
dados = {}
mulheres = []
acima_media = []
tot_idade = media_idade = 0
while True:
    dados['nome'] = str(input('Qual o seu nome? '))
    dados['idade'] = int(input('Qual a sua idade? '))
    tot_idade += dados['idade']
    dados['sexo'] = ' '
    while dados['sexo'] not in 'MF':
        dados['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    pessoas.append(dados.copy())
    r = ' '
    while r not in 'SN':
        r = str(input('Deseja continuar inserindo os dados? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break
media_idade = tot_idade / len(pessoas)
for dic in pessoas:  # Para cada dicionário no vetor pessoas
    if dic['sexo'] == 'F':
        mulheres.append(dic['nome'])
    if dic['idade'] > media_idade:
        acima_media.append(dic.copy())
print('-=' * 20)
print(f'{len(pessoas)} pessoas foram cadastradas.')
print(f'A média de idade das pessoas cadastradas é {media_idade:.2f} anos.')
print(f'Mulheres cadastradas: ', end='')
for m in mulheres:
    print(m, end=', ')
print()
print(f'Pessoas com idade acima da média: ')
for dic in acima_media:
    for key, v in dic.items():
        print(f'{key}: {v}')