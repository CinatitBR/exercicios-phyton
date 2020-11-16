op = 0
n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))

while op != 5:
    op = int(input('Escolha uma opção:\n[ 1 ] Somar\n[ 2 ] Multiplicar\n[ 3 ] Maior\n[ 4 ] Novos números\n[ 5 ] Sair do programa\n'))  # Usuário escolhe opção
    if op == 1:  # Soma
        print(f'A soma entre {n1} e {n2} é {n1 + n2}')
    elif op == 2:  # Multiplicação
        print(f'A multiplicação entre {n1} e {n2} é {n1 * n2}')
    elif op == 3:  # Maior
        if n1 > n2:
            print(f'O maior número é {n1}')
        else:
            print(f'O maior número é {n2}')
    elif op == 4:  # Novos números
        n1 = int(input('Digite o 1º número: '))
        n2 = int(input('Digite o 2º número: '))
    elif op == 5:
        print('ENCERRANDO...')
    else:
        print('Opção inválida, tente novamente...')