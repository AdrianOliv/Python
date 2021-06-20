# Programa que lê o nome, idade e sexo de 4 pessoas.
# Dizer a média de idade de todos, nome do mais velho e
# quantas mulheres tem menos de 20 anos
ma_idade = 0
s_idade = 0
n_mulheres = 0
for i in range(4):
    nome = input('Qual o seu nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo (fem/mas): ')
    s_idade += idade
    if idade > ma_idade and sexo == 'mas':
        ma_idade = idade
        ma_velho = nome
    if sexo == 'fem' and idade < 20:
        n_mulheres += 1

print(f'\033[32mA média de idade de todos é {s_idade/4}!\033[m')
print(f'\033[32mO mais velho do grupo é o {ma_velho} com {ma_idade} anos!\033[m')
print(f'\033[32mO número de mulheres jovens menor que 20 anos é {n_mulheres}!\033[m')
