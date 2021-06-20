# Digitar uma frase e dizer quantas vezes a letra 'a' aparece
# Em que posição ela aparece a primeira vez e na ultima vez
txt = input('Digite um texto: ').strip().lower()
print(txt.count('a'))
print(txt.find('a')+1)
print(txt.rfind('a')+1)
