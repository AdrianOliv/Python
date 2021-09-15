# O jogo é composto por 6 cartões que a princípio parecem conter
# números aleatórios. Estes cartões são entregues a uma pessoa,
# você pede que ele separe os cartões que possuem a idade desta
# pessoa registrada nele. Depois você recolhe os cartões separados
# pela pessoa e diz que vai adivinhar a idade desta pessoa.

# Como construir:
# https://www.ticsnamatematica.com/2014/11/entenda-como-construir-cartoes-jogo-adivinhe-idade.html

import os
from time import sleep


def limpar_tela():
    """Limpa a tela para apresentar novos dados.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def titulo():
    """Apresenta o titulo do jogo.
    """
    limpar_tela()
    print("-" * 40)
    print(f"{'Jogo das Idades':^40}")
    print("-" * 40)


def fim():
    """Apresenta a finalizaçâo do jogo.
    """
    print('\n\033[31mJogo Finalizado!')
    print('Volte sempre que quiser\033[m', end = '', flush = True)
    sleep(2)


def cartoes():
    """Cria os cartões de idade conforme base númerica do primeiro número do cartão.
    \nUsuário deve instanciar a função da seguinte forma:
        x = cartoes()

    Returns:
        [list]: [Lista com o valor dos cartões.]
    """
    # Criação das bases númericas de cada cartão.
    l_cartao = list()
    for a in range(6):
        l_cartao.append(list())
        l_cartao[a].append(2 ** a)
    
    # Inserindo as idades disponíveis em cada cartão,
    # conforme base numérica.
    for a in range(1,64):
        k = 0
        for b in range (5, -1, -1):
            if a == l_cartao[b][0]:
                break
            elif l_cartao[b][0] < a:
                if k != a and (k + l_cartao[b][0]) <= a:
                    k += l_cartao[b][0]
                    l_cartao[b].append(a)
    
    # Retorna a lista com os cartões
    return l_cartao


def play():
    """Inicializador do jogo.\n
    Pergunta se o usuário deseja iniciar o jogo ou sair dele.

    Returns:
        [True]: [Iniciar o jogo!]
        [False]: [Cancela o jogo!]
    """
    while True:
        try:
            titulo()
            print('Iniciar jogo?   1)Sim  2)Não\n')
            o = str(input('Qual sua opção: '))
        except KeyboardInterrupt:
            print('\n\033[31mPara sair, digite a opção 2!\033[m')
            sleep(3)
        else:
            if o == str(1):
                return True
            elif o == str(2):
                return False
            else:
                print("\033[31m", end = "")
                print(f"{'Incorreto!':^40}")
                print("\033[m", end = "")
                sleep(1)


def mostra_carta(carta = 1):
    """Mostra a carta a ser analisada conforme tabela 'for'.

    Args:
        carta (list, optional): [Carta única a ser mostrada]. Defaults to 1.
    """
    print('\033[32m',end = '')
    for num in carta:
        if carta.index(num) > 1 and carta.index(num) % 8 == 0:
            print('\n')
        print(f'{num:^4}', end = ' ')
    print('\033[m')


def advinha_idade(carta = []):
    """Confirma se a idade está presente na carta analisada.
    Se estiver, retornará 'True' para o jogo e somará a idade.
    Se não estiver, retornará 'False'.

    Args:
        carta (list, optional): [Lista contendo os valores da carta]. Defaults to [].

    Returns:
        [Boolean]: [True ou False, depende se a idade está ou não)]
    """
    while True:
        mostra_carta(carta)
        print('\nA sua idade aparece aqui?')
        confirma_idade = str(input('Digite "y"(sim) ou "n"(não) para responder: ').strip().lower())
        if confirma_idade == 'y':
            return True 
        elif confirma_idade != 'n':
            print('\033[31mVocê digitou errado, responda novamente...\033[m')
            sleep(3)
            titulo()
        else:
            return False
