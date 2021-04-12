# Programa que identifica pessoas maiores de idade.
from datetime import date
from time import sleep
s = 0
for i in range(7):
    ano = int(input(f'Pessoa {i+1}, o ano do seu nascimento: '))
    if (date.today().year - ano) >= 21 :
        s += 1
print(f'\n{s} pessoas são maiores de idade!')
print(f'{7-s} pessoas ainda são menores de idade\n')
sleep(2)
