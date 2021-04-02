# Ler o ano e dizer se é bissexto.
# Regras:
#   De 400 em 400 anos é ano bissexto.
#   De 100 em 100 anos não é ano bissexto.
#   De 4 em 4 anos é ano bissexto.
from time import sleep
ano = int(input('Digite o ano do seu interesse: '))
print('Processando...')
sleep(1.20)
if ano % 400 == 0 :
    print('Esse é um ano Bissexto!\n')
elif ano % 100 == 0 :
    print('Esse não é um ano Bissexto!\n')
elif ano % 4 == 0 :
    print('Esse é um ano Bissexto!\n')
else:
    print('Esse não é um ano Bissexto!\n')

#Outra forma (peguei na internet.)
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('Esse é um ano Bissexto!\n')
else:
    print('Esse não é um ano Bissexto!\n')
