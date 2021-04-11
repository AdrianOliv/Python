# Programa que identifica pessoas maiores de idade.
from time import sleep
s = 0
for i in range(7):
    idade = int(input(f'Pessoa {i+1}, digite a sua idade: '))
    if idade >= 21 :
        s += 1
print(f'\n{s} pessoas são maiores de idade!\n')
sleep(2)
