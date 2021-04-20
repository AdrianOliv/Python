# Programa de simulacao de banco
# Simular cedulas do saque a partir do informado
# O caixa só possui notas de 50, 20 e 10

from time import sleep
i = str()
while i != 'n':
    print('=' * 20)
    print('{:^20}'.format('BANCO PY'))
    print('=' * 20)
    din = int(input('\nQual valor vc deseja? '))
    div1 = din // 50
    div2 = din % 50 // 20
    div3 = din % 50 % 20 // 10
    print('\nAguarde...')
    sleep(2)
    if (din % 50 % 20 % 10) != 0:
        print('\033[31mERRO...')
        print('Esse caixa só possui notas de 50, 20 e 10.\033[m\n')
    else:    
        print('\033[32mVocê recebera as seguintes notas:')
        if div1 != 0:
            print('    {} de R$50,00'.format(div1))
        if div2 != 0:
            print('    {} de R$20,00'.format(div2))
        if div3 != 0:
            print('    {} de R$10,00\n'.format(div3))
    i = input('\033[mDeseja continuar (y/n) ')
