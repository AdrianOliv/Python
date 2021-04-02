# Ler dois numeros e dizer qual é o maior ou sesão iguais.
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
if n2 > n1 :
    print(f'{n2} é maior!')
elif n1 > n2 :
    print(f'{n1} é maior!')
else:
    print('Os dois são iguais.')
