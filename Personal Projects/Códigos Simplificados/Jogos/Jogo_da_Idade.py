# Jogo da Idade Advinhada
from time import sleep

def Titulo():
    print("\033[7;44m", end = "")
    print("-" * 40)
    print(f"\033[7;41m{'Jogo das Idades':^40}")
    print("\033[7;44m", end = "")
    print("-" * 40)
    print("\033[m", end = "")

def Base():
    global base
    for a in range(6):
        base.append(list())
        base[a].append(2 ** a)

def Tabelas():
    global base
    for a in range(1,64):
        k = 0
        for b in range (5, -1, -1):
            if a == base[b][0]:
                break
            elif base[b][0] < a:
                if k != a and (k + base[b][0]) <= a:
                    k += base[b][0]
                    base[b].append(a)

def Jogar():
    while True:
        op = str(input(f"{'Você quer jogar? (y/n): ':>32}"))
        if op in "Yy":
            return True
        elif op in "Nn":
            return False
        else:
            print("\033[31m", end = "")
            print(f"{'Incorreto!':^40}")
            print("\033[m", end = "")

def Idade():
    global num
    while True:
        op = str(input("SIM(y) ou NÃO(n): "))
        if op in "Yy":
            num += a[0]
            break
        elif op in "Nn":
            break
        else:
            print("\033[31m", end = "")
            print(f"{'Incorreto!':^40}")
            print("\033[m", end = "")
        

# Variables
base = list()
k = int()
num = int()

# Program
Titulo()
Base()
Tabelas()

while True:
    # Loop Jogo
    if Jogar():
        num = 0
        # Tabelas
        for a in base:
            print("Sua idade aparece aqui?\n")
            for b in range(32):
                if b > 1 and b % 8 == 0:
                    print("\n")
                print(f"{a[b]:^4}", end = " ")
            print("\n")
            Idade()
            print("\033[31m")
            print("_" * 40)
            print("\033[m\n")
        sleep(2)
        print("Pelo meu palpite...")
        sleep(2)
        print("A sua idade é...")
        sleep(3)
        print("=>  ", num, "  <=")
        print()
    else:
        break
