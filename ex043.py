peso = float(input('Informe seu peso (em kg): '))
altura = float(input('Informe sua altura (em metros): '))
imc = peso / (altura ** 2)

if imc < 18.5:
    print(f'Você está ABAIXO DO PESO.')
elif imc < 25:
    print('Você está no PESO IDEAL.')
elif imc <= 30:
    print('Você está com SOBREPESO.')
elif imc > 40:
    print('Você está com OBESIDADE.')
else:
    print('Você têm OBESIDADE MÓRBIDA.')


