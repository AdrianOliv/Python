#Programa que mostra dobro, triplo e raiz de um número
n = int(input('Digite um número: '))
print('''O dobro desse número é {}
O triplo é {} e
A raiz é {:.2f}'''.format(n*2,n*3,n**(1/2)))
