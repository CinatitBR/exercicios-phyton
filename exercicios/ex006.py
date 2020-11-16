print('\033[31m-=-\033[m' * 10, '\033[1;30mBem-vindo!\033[m', '\033[31m-=-\033[m' * 10)
a = float(input('\033[4;35mDigite um número:\033[m '))

print(f'''\033[1;33mO número é\033[m {a} 
\033[1;33mSeu dobro é\033[m {2 * a}
\033[1;33mSeu triplo é\033[m {3 * a}
\033[1;33mSua raiz quadrada é\033[m {a ** (1/2):.2f}''')