n1 = float(input('Digite o 1º número: '))
n2 = float(input('Digite o 2º número: '))
n3 = float(input('Digite o 3º número: '))

if n1 > n2 and n1 > n3:
    if n2 < n3:
        print(f'{n1, n2, n3}\nO maior número é {n1}, o menor é {n2}')
    else:
        print(f'{n1, n2, n3}\nO maior número é {n1}, o menor é {n3}')
elif n2 > n1 and n2 > n3:
    if n1 < n3:
        print(f'{n1, n2, n3}\nO maior número é {n2}, o menor é {n1}')
    else:
        print(f'{n1, n2, n3}\nO maior número é {n2}, o menor é {n3}')
else:
    if n1 < n2:
        print(f'{n1, n2, n3}\nO maior número é {n3}, o menor é {n1}')
    else:
        print(f'{n1, n2, n3}\nO maior número é {n3}, o menor é {n2}')
