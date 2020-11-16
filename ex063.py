# 0, 1, 2, 3, 5, 8, 13
n = int(input('Você quer ver quantos termos da sequencia de fibonacci? '))
a = 0
b = 1
resultado = a + b
print(a, end=' | ')
while n > 1:
    print(resultado, end=' | ')
    resultado = a + b
    a = b
    b = resultado
    n -= 1
