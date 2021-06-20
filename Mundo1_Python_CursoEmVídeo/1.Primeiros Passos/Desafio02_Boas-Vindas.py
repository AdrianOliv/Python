#Crie um programa que leia o nome de alguem e dê boas vindas.
nome = input('\033[1;30mQual é o seu nome? \033[m')
print('Prazer em te conhecer \033[1;34m{}\033[m!'.format(nome))

# Outra forma de fazer!
nome = input('\033[1;35mDiga o seu nome: \033[m')
print(f'Olá \033[1;30m{nome}\033[m, seja muito bem vindo(a)!')
