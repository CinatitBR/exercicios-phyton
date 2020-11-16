r1 = float(input('Digite o comprimento da 1ª reta: '))
r2 = float(input('Digite o comprimento da 2ª reta: '))
r3 = float(input('Digite o comprimento da 3ª reta: '))

if (r1 < r2 + r3) and (r2 < r1 + r3) and (r3 < r1 + r2):
    print(f'As retas com medidas {r1, r2, r3} PODEM formar um triângulo!')
else:
    print(f'As retas com medidas {r1, r2, r3} NÃO podem formar um triângulo!')