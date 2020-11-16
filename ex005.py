a = int(input('\033[1;36mDigite um número inteiro:\033[m '))

print('\033[31m=\033[m' * 20)
print(f'O número é \033[1;35m{a}\033[m')
print(f'Seu sucessor é \033[1;35m{a+1}\033[m')
print(f'Seu antecessor é \033[1;35m{a-1}\033[1;36m')
print('\033[31m=\033[m' * 20)