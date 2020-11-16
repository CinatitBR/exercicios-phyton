aluno = {}
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média do(a) {aluno["Nome"]}: '))
aluno['Situação'] = ('Aprovado' if aluno['Média'] >= 7 else 'Reprovado')

for k, v in aluno.items():  # Para cada chave e valor em aluno.items()
    print(f'{k}: {v}')