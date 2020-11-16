somaIdade = 0
homemVelho = [0, 'nome']
mulher = 0

for p in range(1, 5):
    print('=' * 10, f'{p}ª Pessoa', '=' * 10)
    nome = str(input('Informe seu nome: ')).strip()
    idade = int(input('Informe sua idade: '))
    sexo = str(input('Qual o seu sexo?\nSexo [M/F]: ')).strip().upper()
    somaIdade += idade

    if sexo == 'M' and idade > homemVelho[0]:
        homemVelho[0] = idade
        homemVelho[1] = nome
    elif sexo == 'F' and idade < 20:
        mulher += 1

print(f'A média de idade do grupo é de {somaIdade / 4} anos')
print(f'O nome do homem mais velho tem {homemVelho[0]} anos e seu nome é {homemVelho[1]}')
print(f'{mulher} mulheres têm menos de 20 anos')

