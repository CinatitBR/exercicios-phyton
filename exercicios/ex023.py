num = int(input('Digite um número inteiro de 0 a 9999: '))
unidade = (num % 10)
dezena = (num // 10) % 10
centena = (num // 100) % 10
milhar = (num // 1000)

print(f'Unidade: {unidade}\nDezena: {dezena}\nCentena: {centena}\nMilhar: {milhar}')

