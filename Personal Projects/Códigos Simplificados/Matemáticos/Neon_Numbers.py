# Neon Number
# Where 9 -> 9*9 -> 8+1 -> 9

# Functions
def Num():
    global n, n2
    try:
        n = int(input("Ínicio: "))
        n2 = int(input("Fim: "))
        return True
    except:
        print("\033[31mTermo Inválido!\033[m")
        return False

def Neon(n, n2):
    global num, neon
    neon.clear()
    for i in range(n, n2 + 1):
        num = 0
        for j in str(i ** 2):
            num += int(j)
        if num == i:
            neon.append(num)
    if len(neon) > 0:
        print("Números Neon: ", end = "")
        for i in neon:
            print(i, end = "  ")
        print()
    else:
            print("Nenhum número encontrado.")
            

# Variables
n = int()
n2 = int()
num = int()
neon = list()

# Program
print(f"\033[7;40m{'Neon Number':^40}\033[m")
while True:
    print("\nDigite o 1° e último termo a analisar...")
    if Num():
        Neon(n, n2)
    else:
        break
