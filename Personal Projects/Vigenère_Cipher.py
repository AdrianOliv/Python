# Vigenère Cipher
def Msg():
    global msg
    msg = str(input("Mensagem: ").upper().strip())
    if msg.isalpha():
        return True
    else:
        print("\033[31mTermo Inválido\033[m")
        return False

def Key(msg):
    global key
    key = str(input("Key: ").upper().strip())
    if key.isalpha():
        return True
    else:
        print("\033[31mTermo Inválido\033[m")
        return False

def Cipher(msg, key):
    global alfa, code
    i = 0
    while len(code) != len(msg):
        for l in key:
            if len(code) == len(msg):
                break
            else:
                code.append(alfa[(alfa.index(msg[i]) + alfa.index(l)) % 26])
                i += 1


# Variables
alfa = ("A", "B", "C", "D", "E",
        "F", "G", "H", "I", "J",
        "K", "L", "M", "N", "O",
        "P", "Q", "R", "S", "T",
        "U", "V", "W", "X", "Y", "Z")
code = list()
msg = str()
key = str()

# Program
if Msg():
    if Key(msg):
        Cipher(msg, key)
if len(code) > 0:
    print("\nCódigo: ", end = "")
    for l in code:
        print(l, end = "")
    print()
