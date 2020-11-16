n1 = float(input('Insira sua primeira nota: '))
n2 = float(input('Insira sua segunda nota: '))
media = (n1+n2) / 2

if media < 5:
    print(f'Você foi REPROVADO! Sua média foi {media:1.f}')
elif 7 > media >= 5:
    print(f'Você foi para RECUPERAÇÃO! Sua média foi {media:.1f}')
else:
    print(f'Você foi APROVADO! Sua média foi {media:.1f}')
