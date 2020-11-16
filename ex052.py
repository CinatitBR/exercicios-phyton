num = int(input('Digite um número inteiro: '))
total = 0
for i in range(1, num + 1):
    if num % i == 0:
        total += 1
if total == 2:
    print(f'O número {num} é PRIMO, pois foi foi divisivel {total} vezes.')
else:
    print(f'O número {num} NÃO é primo, pois foi divisiel {total} vezes')