soma = cont = 0
while True:
    n = int(input('Digite um número [999 para encerrar]: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'Foram digitados {cont} números.')
print(f'A soma entre eles é {soma}.')