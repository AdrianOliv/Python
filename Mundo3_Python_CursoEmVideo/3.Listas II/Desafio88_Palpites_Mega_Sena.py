# Programa de palpites da Mega-Sena

from random import randint 
l = []
o = 1

while o != 2:
    l.clear()
    print('\033[36m-=' * 20)
    print(f'{"PALPITES PARA A MEGA-SENA":^40}')
    print('-=' * 20)
    p = int(input('\n\033[mQtd de palpites que vc deseja: '))
    
    for i in range(p):
       l.append(list())
       while len(l[i]) != 6:
            n = randint(1, 60)
            if n not in l[i]:
                l[i].append(n)
    for i in l:
        print(f'{l.index(i)+1:<2}° Palpite: {sorted(i)}')
    
    while True:
        print('\n1 - Novo Jogo')
        o = int(input('2 - Sair           O que deseja fazer? '))
        print("\n")
        if o == 1 or o == 2:
            break
        else:
            print('\033[31mOpção Inválida!\033[m')
            
print("\nPROGRAMA FINALIZADO\n")
