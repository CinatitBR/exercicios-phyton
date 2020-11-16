from random import randint

movUser = int(input('Escolha seu movimento:\n[ 1 ] Pedra\n[ 2 ] Papel\n[ 3 ] Tesoura\n'))
movPc = randint(1, 3)

if 2 != movUser != 1 and movUser != 3:
    print('Opção INVÁLIDA! Tente novamente!')
    exit()
if movUser == movPc:
    print('EMPATE! Sorte sua, não ganhei por pouco...')
elif movUser == 1 and movPc == 2:
    print('Escolhei papel.')
    print('VOCÊ PERDEU! Tenha mais sorte na próxima vez... ')
elif movUser == 2 and movPc == 1:
    print('Escolhi pedra...')
    print('VOCÊ GANHOU! Sorte de principiante...')
elif movUser == 2 and movPc == 3:
    print('Escolhi tesoura...')
    print('VOCÊ PERDEU! Tenha mais sorte da próxima vez.')
elif movUser == 3 and movPc == 2:
    print('Escolhi papel...')
    print('VOCÊ GANHOU! Sorte de principiante...')
elif movUser == 1 and movPc == 3:
    print('Escolhi tesoura...')
    print('VOCÊ GANHOU! Sorte de principiante...')
else:
    print('Escolhi pedra...')
    print('VOCÊ PERDEU! Tenha mais sorte na próxima vez.')