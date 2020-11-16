from time import sleep

print('\033[1;31m-=-\033[m' * 25)
print('\033[1;33mBom dia! Iremos verificar se você está autorizado a pegar o empréstimo.\033[m')
print('\033[1;31m-=-\033[m' * 25)

vCasa = float(input('\033[1;30mQual o valor da casa que você planeja comprar? R$\033[m'))
salario = float(input('\033[1;30mQual o seu salário? R$\033[m'))
anos = int(input('\033[1;30mEm quantos anos você vai pagar?\033[m '))
vMensal = vCasa / (anos * 12)

print('\033[1;32mProcessando...\033[m')
sleep(1.5)

if vMensal > (30/100 * salario):
    print('\033[1mEmpréstimo\033[m \033[1;31mNEGADO\033[m. \033[1mO valor da prestação excedeu 30% do seu salário.\033[m')
else:
    print(f'\033[1mEmpréstimo \033[1;32mAPROVADO\033[m. O valor da prestação será \033[1;31mR${vMensal:.2f}\033[m\033[m')
