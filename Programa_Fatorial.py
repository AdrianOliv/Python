def fat(x):
    if x <= 1:
        print('\033[34mO fatorial de 1 e 0 é igual a: 1\033[m')
    else:
        for i in range(x-1, 0, -1):
            x = x * i
        print(f'\033[32mO fatorial é: {x}\033[m')
            
var = int(input('Digite o num: '))
fat(var)
