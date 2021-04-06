def pal(nome):
    x = nome[::-1]
    if x == nome :
        print('É um Palíndromo!\n')
    else:
        print('Não é um Palíndromo!\n')

y = input('Digite o nome: ').lower()
pal(y)
