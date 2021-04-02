nome = input('Nome Completo: ').title().split()
print('Olá \033[31m{} {}\033[m, tudo bem?'.format(nome[0], nome[len(nome)-1]))
print('Olá \033[4;34m{} {}\033[m, tudo bem?'.format(nome[0], nome[len(nome)-1]))
