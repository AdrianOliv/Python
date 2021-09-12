from funcoes_do_jogo import *
from time import sleep

# Instanciar cartas em uma variável.
cartas = cartoes()

# Variável que guardará a idade do usuário.
idade = int()

# Loop do Jogo
while True:
    if play():
        titulo()
        print('Pense em uma idade (pode ser a sua)...')
        sleep(3)
        print('Agora...')
        sleep(2)
        print('Olhe com atenção para as tabelas abaixo...\n')
        sleep(2)
        idade = 0
        for carta in cartas:
            print(f'\n\033[7;40m  Cartão nº {cartas.index(carta)+1}  \033[m\n')
            if advinha_idade(carta):
                idade += carta[0]
                print(idade)
            titulo()
        print('A idade que você pensou foi...')
        sleep(3)
        print('...')
        sleep(2)
        print(f'\n    --> {idade} anos <--')
        input('\nClique para reiniciar o jogo...')
    else:
        fim()
        break
