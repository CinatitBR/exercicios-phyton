cont = soma = 0
n = int(input('Digite um número [999 para encerrar]: '))

while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número [999 para encerrar]: '))
print(f'Foram digitados {cont} números. A soma entre eles é {soma}.')
