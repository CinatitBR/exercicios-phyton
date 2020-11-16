frase = str(input('Digite uma frase: ')).strip().lower()

print(f'Quantas vezes a letra A aparece: {frase.count("a")}')
print(f'A posição em que a letra A aparece a 1ª vez: {frase.find("a")+1}')
print(f'Última ocorrência da letra A: {frase.rfind("a")+1}')
