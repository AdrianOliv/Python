# Programa que guarda Nome, Média e Situação de um aluno em um dicionario.

Boletim = list()
Aluno = {'Nome':'', 'Média':'', 'Situação':''}
while True:
    Aluno['Nome'] = str(input("Nome do Aluno: "))
    Aluno['Média'] = float(input("Média do Aluno: "))
    if Aluno['Média'] > 7:
        Aluno['Situação'] = '\033[32mAprovado\033[m'
    elif Aluno['Média'] < 4:
        Aluno['Situação'] = '\033[31mReprovado\033[m'
    else:
        Aluno['Situação'] = '\033[33mpara Recuperação\033[m'

    Boletim.append(Aluno.copy())

    while True:
        o = input("Continuar(y/n): ")
        if o in "YyNn":
            break
        else:
            print("\033[31mValor Incorreto!\033[m")
    if o in "Nn":
        break

print()
for a in Boletim:
    print(f"O {a['Nome']} tirou {a['Média']}, por isso foi {a['Situação']}.")