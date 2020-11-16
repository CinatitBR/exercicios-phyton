pessoa18 = homem = mulher20 = 0
while True:
    print('=' * 20)
    print('     CADASTRO')
    print('=' * 20)
    idade = int(input('Informe sua idade: '))  # Idade
    sexo = ' '  # Inicialização da variável sexo
    while sexo not in 'FM':  # Obriga o usuário a digitar corretamente
        sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()
    print('-' * 25)
    if idade > 18:  # Se tiver mais de 18 anos
        pessoa18 += 1
    if sexo in 'M':  # Se for homem
        homem += 1
    if 'F' in sexo and idade < 20:  # Mulher menos de 20 anos
        mulher20 += 1
    op = ' '  # Inicialização da variável op
    while op not in 'SN':  # Usuário escolhe se quer continuar ou não
        op = str(input('Você quer continuar o cadastro? [S/N] ')).strip().upper()
    if 'N' in op:  # Se usuário quiser encerrar
        break
print(f'{pessoa18} pessoas têm mais de 18 anos.')
print(f'{homem} homens foram cadastrados.')
print(f'{mulher20} mulheres têm menos de 20 anos.')
