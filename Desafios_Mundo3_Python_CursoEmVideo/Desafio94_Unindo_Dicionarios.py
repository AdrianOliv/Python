# Ler nome, sexo e idade de várias pessoas em um dicionário unico.
# Guardar todos os dicionarios em uma lista
# Mostrar quantos cadastrados, média das idades,
# Lista com todas as mulheres e lista com idades acima da media

Grupo = list()
Mulheres = list()
Up_Media = list()
Pessoa = dict()
si = 0
while True:
    Pessoa['Nome'] = str(input("Nome: "))
    Pessoa['Sexo'] = str(input("Sexo(m/f): "))
    Pessoa['Idades'] = int(input("Idade: "))
    Grupo.append(Pessoa.copy())
    si += Pessoa['Idades']

    if Pessoa['Sexo'] in 'Ff':
        Mulheres.append(Pessoa.copy())

    while True:
        o = input("Continuar(y/n): ")
        if o in 'YyNn':
            break
        else:
            print("\033[31mValor Incorreto!\033[m")
    if o in 'Nn':
        break

for pessoa in Grupo:
    if pessoa['Idades'] > (si/len(Grupo)):
        Up_Media.append(pessoa['Nome'])

print(f'\nForam cadastrados {len(Grupo)} {"Pessoa" if len(Grupo) == 1 else "Pessoas"}')
print('Mulheres Cadastradas: ')
for i in Mulheres:
    print(i)
print(f'A Média das idades do grupo é {si/len(Grupo)}.')
print(f'As pessoas com idade acima da média: {Up_Media}\n')