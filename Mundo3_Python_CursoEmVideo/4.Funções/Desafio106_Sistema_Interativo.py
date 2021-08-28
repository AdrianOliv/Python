from time import sleep
from os import system

# Definições
def titulo():
    print('************  INTERACTIVE HELP  ************')
    print('Digite "fim" para sair.\n')

def valida(texto):
    """
    Validar se a entrada do usuário contém somente letras.
    : param texto = texto digitado pelo usuário.
    """
    if texto.isalpha():
	ajuda(texto)
    else:
	print('Valor digitado incorreto!')
	sleep(2.5)

def ajuda(texto):
    """
    Abre o Interactive Help nativo com as informações necessárias ao usuário.
    : param texto = função/biblio pesquisada.
    """
    print('\n')
    help(texto)
    a = input('Enter para continuar...')

def sair():
    print('************  FIM DO PROGRAMA  ************')
    sleep(3)


# Main
while True:
    system('cls')
    titulo()
    txt = str(input('Digite uma função ou biblioteca.\nPesquisar: '))
    if txt == 'fim':
	break
    else:
	valida(txt)
sair()
sleep(2)
