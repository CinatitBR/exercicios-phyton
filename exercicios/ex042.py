a = float(input('Digite o comprimento da 1ª reta: '))
b = float(input('Digite o comprimento da 2ª reta: '))
c = float(input('Digite o comprimento da 3ª reta: '))

if (a < b + c) and (b < a + c) and (c < a + b): #PODE FORMAR TRIÂNGULO
    print(f'As retas com medidas {a, b, c} PODEM formar um triângulo!')
    if a == b == c: #TODOS OS LADOS SEMELHANTES
        print(f'Será um triângulo EQUILÁTERO!')
    elif (c != a == b) or (a != b == c) or (b != c == a): #DOIS LADOS SEMELHANTES
        print('Será um triângulo ISÓCELES!')
    else: #TODOS OS LADOS DIFERENTES
        print('Será um triângulo ESCALENO!')

else: #NÃO FORMA TRIÂNGULO
    print(f'As retas com medidas {a, b, c} NÃO podem formar um triângulo!')