extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
           'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    while num > 20 or num < 0:
        num = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    print(f'O número {num} por extenso é {extenso[num]}.')
    op = ' '
    while op not in 'sn':
        op = str(input('Você quer continuar? [S/N]')).strip().lower()[0]
    if op == 'n':
        break
print('PROGRAMA FINALIZADO.')