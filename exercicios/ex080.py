numeros = []
for i in range(0, 5):  # Laço irá rodar 5 vezes
    n = int(input(f'Digite o {i+1}º número: '))  # Usuário insere número
    if i == 0 or n >= numeros[-1]:  # Se for a primeira vez do laço ou se n for maior que o último valor da lista
        numeros.append(n)  # Se n for maior que o último valor da lista, n será adicionado ao final dela
        print('Adicioado ao final da lista...')
    else:
        for pos in range(len(numeros)):  # Esse laço irá cobrir todos os índices do vetor
            if n <= numeros[pos]:
                numeros.insert(pos, n)  # Se n for menor que um número, será adicionado no lugar dele jogando os outros para frente
                print(f'Adicionado na posição {pos} da lista...')
                break
print(f'Os números digitados em ordem crescente: {numeros}')