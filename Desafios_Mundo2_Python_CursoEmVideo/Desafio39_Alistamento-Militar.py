# Faça um programa que leia o ano de nascimento e
# Diga se já é possível se alistar no exército.
from datetime import date
ano = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano
if idade < 18 :
    print('''    Sua idade ainda está abaixo do obrigatório.
    Faltam {} anos para se alistar.'''.format(18 - idade))
elif idade > 18 :
    print('''\033[31m    Sua idade já está acima a {} anos.
    Dirija-se a uma junta militar proxima de você!\033[m'''.format(idade - 18))
else:
    print('Você já está na idade para servir!')
