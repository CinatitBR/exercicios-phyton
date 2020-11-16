salario = float(input('Qual é o seu salário? R$'))
aumento = salario

if salario > 1250:
    aumento += (10/100) * salario
    print(f'Seu salário R${salario:.2f} com 10% de aumento será R${aumento:.2f}')
else:
    aumento += (15/100) * salario
    print(f'Seu salário R${salario:.2f} com 15% de aumento será R${aumento:.2f}')

