# Programa de indentificação de números primos.
from time import sleep
num = int(input('Digite um número: '))
for i in range(2, num+1):
    if num % i == 0 and i != num:
        print('\033[31mNão é um número Primo!\033[m')
        break
    elif i == num:
        print('\033[32mÉ um número Primo!\033[m')
print('\nProcess...')
sleep(1.5)
print('Fisinh!')
