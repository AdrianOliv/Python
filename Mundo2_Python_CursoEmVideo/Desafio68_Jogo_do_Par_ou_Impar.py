# Programa que joga Par ou Impar com o pc.
# É interrompido quando jogador perder e mostrar o num de vitorias.
from random import randint

tentativas = 0
win = True

# Programa roda enquanto jogar estiver ganhando.
while win:
    # Escolha do jogador.
    player = input('Par ou Impar?  ').capitalize()
    
    # Se Jogados escolher então pc recebe o outro.
    if player == 'Par':
        pc = 'Impar'
    elif player == 'Impar':
        pc = 'Par'
    else:
        print('Opção Incorreta.')
    
    # Número da máquina.
    num = randint(1,10)
    print(f'O número sorteado foi {num}.')
    if num % 2 == 0:
        i = 'Par'
    else:
        i = 'Impar'

    if player == i:
        print('\033[32mVocê ganhou!\033[m\n')
        tentativas += 1
    else:
        print('\033[31mVocê perdeu!\033[m')
        print(f'Você ganhou {tentativas} vezes.')
        break
