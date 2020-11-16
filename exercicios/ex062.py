termo = int(input('Digite o 1º termo da P.A: '))
razao = int(input('Digite a razão da P.A: '))
i = 0
op = 10
total = 10

while op != 0:
    while i < op:
        print(termo, end=' | ')
        termo += razao
        i += 1
    i = 0
    op = int(input('\nVocê quer mostrar mais quantos termos? Digite 0 se quiser encerrar: '))
    total += op
print(f'O programa foi encerrado com {total} termos exibidos.')
