# Programa que lê a idade do atleta e identifica a categoria de competição.
import datetime
print('-=' * 20)
print('{:^40}'.format('CATEGORIA DE ATLETA'))
print('-=' * 20)
idade = datetime.date.today().year - int(input('Digite o ano do seu nascimento: '))
if idade <= 9 :
    print('Sua categoria é: MIRIM!')
elif idade <= 14 :
    print('Sua categoria é: INFANTIL!')
elif idade <= 19 :
    print('Sua categoria é: JUNIOR!')
elif idade == 20 :
    print('Sua categoria é: SÊNIOR!')
else:
    print('Sua categoria é: MASTER!')
