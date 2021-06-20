# Programa que faz infinitas tabuadas.
# Finalizar ao digitar número negativo.

while True:
    num = int(input('\nDigite um número: '))
    if num < 0:
        print('\nFinalizado!')
        break
    print('\n')
    for i in range(1, 11):
        print(f'{num:>3} x {i:>3} = {num * i:>3}')
