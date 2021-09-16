def caesar_cipher(text, key = 1, decipher = False):
    """Decifrar códigos através da Cifra de Cesar, com deslocamento 'key' informado.

    Args:
        text ([str]): [Texto a ser cifrado/desvendado]
        key (int, optional): [Chave para deslocamento das letras no alfabeto]. Defaults to 1.
        decipher (bool, optional): [Habilita a decifragem, sem ela, considera conversão em código]. Defaults to False.

    Returns:
        [str]: [código/texto formatado]
    """
    result = str()
    for letter in text:
        if letter not in text:
            result += letter
        else:
            if decipher:
                result += alfa[(alfa.index(letter) - key) % 26]
            else:
                result += alfa[(alfa.index(letter) + key) % 26]
    return result


def titulo():
    print(f"\n\033[7;40m{'Cifra de Cesar':^40}\033[m\n")


# Variables
alfa = ("A", "B", "C", "D", "E",
        "F", "G", "H", "I", "J",
        "K", "L", "M", "N", "O",
        "P", "Q", "R", "S", "T",
        "U", "V", "W", "X", "Y", "Z")
msg = str()
key = str()
code = str()

# Program
titulo()
msg = str(input("Mensagem: ").upper().strip())
key = int(input("Chave: "))
code = caesar_cipher(msg, key)
print(f'A mensagem cifrada é: {code}')
print(f'A mensagem desvendada é: {caesar_cipher(code, key, decipher = True)}\n')
