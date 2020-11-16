exp = str(input('Digite uma expressão: '))  # Usuário digita expressão
pAberto = pFechado = 0
for c in exp:  # Verifica cada carácter da expressão
    if c == '(':
        pAberto += 1  # Armazena quantidade de parenteses Abertos
    elif c == ')':
        pFechado += 1  # Armazena quantidade de parenteses Fechados
if pAberto == pFechado:
    print('A expressão está CORRETA!')
else:
    print('A expresão está INCORRETA!')