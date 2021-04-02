# Ler 3 números e dizer o maior e o menor.
n1 = input('Primeiro num: ')
n2 = input('Segundo num: ')
n3 = input('Terceiro num: ')
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n1 and n3 < n2:
    menor = n3
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n1 and n3 > n2:
    maior = n3
print(f'O menor digitado foi {menor} e o maior foi {maior}')
