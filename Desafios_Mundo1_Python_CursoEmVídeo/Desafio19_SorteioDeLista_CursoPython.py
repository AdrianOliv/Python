#Sortear 1 nome de 4 alunos digitados.
import random
a1 = input('Aluno 1: ')
a2 = input('Aluno 2: ')
a3 = input('Aluno 3: ')
a4 = input('Aluno 4: ')
lista = [a1,a2,a3,a4]
print(f'O nome sorteado é: {random.choice(lista)}!')
