# Programa que lê idade e sexo.
# Mostrar qtd pessoas > 18.
# Quantos homens.
# Mulheres < 20.
cont_idade = cont_sexo = cont_fem = 0
cont = 'y'
sexo = 'a'
while cont == 'y' or cont == 'yes':
    idade = int(input('Qual a sua idade? '))
    while True:
        sexo = input('Qual o seu sexo? (m/f): ').lower()
        if sexo == 'f' or sexo == 'm':
            break
    if idade > 18:
        cont_idade += 1
    if sexo == 'm':
        cont_sexo += 1
    if idade < 20 and sexo == 'f':
        cont_fem += 1
    
    cont = input('Você quer continuar? (y/n) ').lower()

print(f'\nForam registrados {cont_idade} pessoas acima de 18 anos.')
print(f'Foram registrados {cont_sexo} homens.')
print(f'Foram registradas {cont_fem} jovens mulheres.\n')
