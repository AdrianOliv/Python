# Lotto Program

from random import randint

def sortear():
    lista = list()
    while len(lista) != 6:
        n = randint(1, 49)
        if n not in lista:
            lista.append(n)
    return lista


lista = list()
ll = list()
n = o = 0

print("\033[7;45m~" * 40)
print(f"{'LOTTO PROGRAM':^40}")
print("~" * 40)
print(f"{'Vamos jogar?':40}\033[m")

while True:
    lista.clear()
    ll.clear()
    
    while True:
        o = str(input("Digite 'Y' para Sim e 'N' para Não: ").upper())
        if o in "YN":
            break
        else:
            print("\033[31mOpção Incorreta!\033[m")
            
    if o == "N":
        break
    
    print()
    print("_" * 40)
    while len(ll) != 6:
        try:
            n = (int(input(f"N° {len(ll)+1}: ")))
            if n not in ll and n > 0 and n < 50:
                ll.append(n)
            else:
                print("\033[7;41mValor Incorreto!\033[m")
        
        except:
            print("\033[31mNúmero Inteiro não digitado!\033[m")
    print("_" * 40)
    
    lista = sortear()
    
    print("\n")
    print("~•" * 20)
    print()
    
    print("> Os números sorteados foram:")
    print(f"\033[32m    {sorted(lista)}\033[m\n")
    
    print("> Números escolhidos por você: ")
    print("    ", end ="")
    for i in sorted(ll):
        if i in lista:
            print("\033[32m", end ="")
        print(i, end = " ")
        print("\033[m", end = "")
    print("\n")
    print("~•" * 20)
    print("\nContinuar?")

print("\n\n\033[41mPROGRAMA FINALIZADO\033[m\n")
