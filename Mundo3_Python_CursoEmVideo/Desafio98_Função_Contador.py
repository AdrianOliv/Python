# Programa de contagem

from time import sleep

def contador(inicio, fim, passos):
    if passos <= 0:
        passos = 1
    print("~" * 40)
    print(f"De {inicio} a {fim}, com {passos} passos:")
    if inicio < fim:
        for cont in range(inicio, fim, passos):
            print(cont, end = " ", flush = True)
            sleep(0.7)
    else:
        for cont in range(inicio, fim, -passos):
            print(cont, end = " ", flush = True)
            sleep(0.7)
    print("FIM!")
    print()
        
contador(1,10,1)
contador(10,0,2)

print("~" * 40)
print(f"{'SUA VEZ':^40}")
inicio = int(input("Valor Inicial: "))
fim = int(input("Valor Final: "))
passos = int(input("Passos: "))
contador(inicio, fim, passos)
