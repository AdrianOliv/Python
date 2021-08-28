# Programa de boletim escolar
# Uma lista com nome e notas do aluno.
# Mostrar Média e permitir pesquisa de aluno

l = []
ll = []

print('=' * 40)
print(f"{'BOLETIM - ACESSO PEDAGOGICO':^40}")
print('=' * 40)

while True:
    ll.append(str(input("Nome do Aluno: ")))
    ll.append(float(input("1° Nota: ")))
    ll.append(float(input("2° Nota: ")))
    l.append(ll[:])
    ll.clear()
    
    while True:
        o = input("Continuar(y/n): ")
        if o in 'YyNn':
            break
        else:
            print("\033[31mValor Incorreto!\033[m")
    if o in 'Nn':
        break

print('=' * 40)
print("\n\033[33mBOLETIM GERAL")
print(f"{'Aluno':.<10} Média\n")
for i in l:
    print(f"{i[0]:.<10} {(i[1] + i[2]) / 2}")
 
print("\033[m\n")       
print('=' * 40)
print(f'{"BOLETIM - ACESSO PUBLICO":^40}')
print('=' * 40)

while True:
    aluno = str(input("Qual aluno deseja verificar: "))
    
    for i in l:
        if i[0] == aluno:
            print(f"\n{'Aluno':<10}|{'Nota1':<8}|{'Nota2':<8}|{'Média':<8}")
            print(f"{aluno:<10}|{i[1]:<8}|{i[2]:<8}|{(i[1]+i[2])/2:<8}\n")
            break
        elif l.index(i) == (len(l)-1):
            print("\033[31mAluno Inexistente!\033[m")
            
    while True:
        o = input("Continuar(y/n): ")
        if o in 'YyNn':
            break
        else:
            print("\033[31mValor Incorreto!\033[m")
    if o in 'Nn':
        break
