vm = int(input('Informe a velocidade do seu carro (em Km/h): '))

if vm <= 80:
    print(f'{vm}Km/h. Você não ultrapassou o limite de velocidade.')
else:
    multa = float((vm - 80) * 7)
    print(f'{vm}Km/h. Você ultrapassou o limite de velocidade, e receberá R${multa:.2f} de multa!')
