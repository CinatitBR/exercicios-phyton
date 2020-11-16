soma = 0  # Irá somar valores digitados
cont = 0  # Contará quantas vezes o laço rodou
maior = 0  # Armazena maior valor
menor = 0  # Armazena menor valor
op = ''  # Onde o Usuário insere números e faz decisões

while 'N' not in op:
    op = int(input('Digite um número: '))
    soma += op
    cont += 1
    if cont == 1:
        menor = op
    elif op > maior:
        maior = op
    elif op < menor:
        menor = op
    op = str(input('Você quer continuar a digitar valores [S/N]? ')).upper().strip()

print(f'Você digitou {cont} números, e a média entre eles é {soma / cont}.')
print(f'O maior valor digitado foi {maior}.')
print(f'E o menor foi {menor}.')
