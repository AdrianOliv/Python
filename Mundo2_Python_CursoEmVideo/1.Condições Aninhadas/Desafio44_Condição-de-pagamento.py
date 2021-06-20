# Calcular o preco final de uma compra mediante a condição de pagamento.
preco = float(input('Digite o preço do produto: '))
print('''Opções de pagamento:
    1 - Dinheiro/Cheque
    2 - Cartão a Vista
    3 - 2x no Cartão
    4 - 3x no Cartão''')
pag = int(input('Digite a opção de pagamento: '))
if pag == 1 :
    print('O valor final fica R$ {}'.format(preco * 0.90))
elif pag == 2 :
    print('O valor final fica R$ {}'.format(preco * 0.95))
elif pag == 3 :
    print('O valor permanece!')
elif pag == 4 :
    print('O valor final fica R$ {}'.format(preco * 1.20))
else:
    print('\033[31mVocê digitou uma opção inválida!\033[m')
