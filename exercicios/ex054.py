from datetime import date

maior = 0
for p in range(1, 8):
    print('=' * 10, f'{p}º PESSOA', '=' * 10)
    idade = int(date.today().year) - int(input('Informe seu ano de nascimento: '))
    if idade > 20:
        maior += 1
if maior > 1:
    print(f'{maior} pessoas já atingiram a maioridade.')
    print(f'{7 - maior} ainda não atingiram.')
else:
    print(f'{maior} pessoa são MAIORES DE IDADE..')
    print('6 ainda não atingiram.')



