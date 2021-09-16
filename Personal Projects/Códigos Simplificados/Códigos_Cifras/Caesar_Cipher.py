# Cifra de Cesar
# Variables
alfa = ("A", "B", "C", "D", "E",
        "F", "G", "H", "I", "J",
        "K", "L", "M", "N", "O",
        "P", "Q", "R", "S", "T",
        "U", "V", "W", "X", "Y", "Z")
msg = str()
key = str()
cifra = list()

# Program
print(f"\033[7;40m{'Cifra de Cesar':^40}\033[m")
print()
msg = str(input("Mensagem: ").upper().strip())
key = int(input("Chave: "))

for a in msg:
    if a.isspace():
        cifra.append(" ")
    else:
        cifra.append(alfa[(alfa.index(a) + key) % 26])
        
for a in cifra:
    print(a, end = "")
print()
