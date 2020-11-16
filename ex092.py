from datetime import date
dados = {
    'nome': str(input('Insira seu nome: ')),
    'idade': int(date.today().year) - int(input('Ano de nascimento: ')),
    'carteira': int(input('Carteira de trabalho (0 se não tiveer): '))
}
if dados['carteira'] != 0:
    dados['contratacao'] = int(input('Ano de contratação: '))
    dados['salario'] = int(input('Salário: R$'))
    dados['aposentadoria'] = (dados['contratacao'] - (date.today().year - dados['idade'])) + 35
print('-=' * 30)
for key, v in dados.items():
    print(f'{key}: {v}')