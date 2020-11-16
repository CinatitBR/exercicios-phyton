from datetime import date

idade = int(date.today().year) - int(input('Informe seu ano de nascimento: '))

if idade <= 9:
    print(f'Você está na categoria MIRIM, pois possui {idade} anos de idade.')
elif idade <= 14:
    print(f'Você está na categoria INFANTIL, pois possui {idade} anos de idade.')
elif idade <= 19:
    print(f'Você está na categoria JUNIOR, pois possui {idade} anos de idade.')
elif idade <= 25:
    print(f'Você está na categoria SÊNIOR, pois possui {idade} anos de idade.')
elif idade > 25:
    print(f'Você está na categoria MASTER, pois possui {idade} anos de idade.')