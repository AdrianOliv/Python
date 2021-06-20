# Ler um numero e depois escolher uma opçao de conversao.
num = int(input('Digite um número inteiro: '))
op = int(input('''
    1 - Binário
    2 - Octal
    3 - Hexadecimal
    
    Qual a base para conversao: '''))
if op == 1 :
    print(f'O numero fica: {bin(num)}')
elif op == 2 :
    print(f'O numero fica: {oct(num)}')
elif op == 3 :
    print(f'O numero fica: {hex(num)}')
else:
    print('Essa opcao nao eh valida!')
