from datetime import date

sexo = int(input('Você é do sexo masculino ou feminino?\n[ 1 ] MASCULINO\n[ 2 ] FEMININO\n'))
if sexo == 2:
    print('Você é do sexo feminino, portanto não precisa se alistar!')
    exit()
nasc = int(input('Por favor, informe seu ano de nascimento: '))
idade = int(date.today().year) - nasc

if idade == 18 and sexo == 1:
    print(f'Hora de alistar no exército! Você já possui {idade} anos.')
elif idade < 18 and sexo == 1:
    print(f'Você ainda não precisa se alistar no exército, faltam {18 - idade} anos\nSeu alistamento será em {(18 - idade) + int(date.today().year)}.')
elif idade > 18 and sexo == 1:
    print(f'Você está {idade - 18} anos atrasado do alistamento!\nVocê devia ter se alistado em {int(date.today().year) - (idade - 18)}.')










