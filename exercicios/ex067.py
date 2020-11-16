while True:
    num = int(input('[-1 para encerrar] Você quer ver a tabuada de qual número? '))
    if num < 0:
        break
    print('-' * 20)
    for i in range(1, 11):
        print(f'{num} X {i:2} = {num * i}')
    print('-' * 20)
print('-=-' * 7)
print('PROGRAMA ENCERRADO')
print('-=-' * 7)

