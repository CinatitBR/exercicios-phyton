n = int(input('Digite um número inteiro: '))
print(f'Bases de conversão:\nDigite 1 para Binário\nDigite 2 para Octal\nDigite 3 para Hexadecimal')
base = int(input(f'Qual será a base de conversão do número {n}? '))

if base == 1:
    print(f'O número {n} convertido para Binário é: {bin(n)[2:]}')
elif base == 2:
    print(f'O número {n} convertido para Octal é: {oct(n)[2:]}')
elif base == 3:
    print(f'O número {n} convertido para Hexadecimal é: {hex(n)[2:]}')
else:
    print('Opção inválida! Tente novamente!')
