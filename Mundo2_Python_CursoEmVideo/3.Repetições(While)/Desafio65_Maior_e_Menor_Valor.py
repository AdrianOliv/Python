# Ler varios numeros até pedir para sair.
# Mostrar média, maior e menor.
num = soma = digi = 0
maior = menor = 0
usu = ''

while usu != 'n':
    num = int(input('Valor: '))
    digi += 1
    soma += num
    if digi == 1 and num != 0:
        maior = menor = num
    elif num > maior:
        maior = num
    elif num < menor:
        menor = num
    usu = input('Continuar(y/n): ')

print(f'\nA média dos números é {soma/(digi)}.')
print(f'O menor valor digitado foi {menor}!')
print(f'O maior valor digitado foi {maior}!')
