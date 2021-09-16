def rot13(text):
    """Função do ROT-13, cifra de cezar com 13 deslocamentos.

    Args:
        text ([str]): [texto a ser codificado/encontrado]

    Returns:
        [str]: [resultado da conversão.]
    """
    result = str()
    for letter in text:
        if letter not in alfa:
            result += letter
        else:
            result += alfa[(alfa.index(letter) + 13) % 26]
    return result


# Variáveis
alfa = ("A", "B", "C", "D", "E",
        "F", "G", "H", "I", "J",
        "K", "L", "M", "N", "O",
        "P", "Q", "R", "S", "T",
        "U", "V", "W", "X", "Y", "Z")

# Main
msg = str(input('Mensagem: ').upper().strip())
print(f'\nO resultado é: {rot13(msg)}')
print(f'O código revertido é: {rot13(rot13(msg))}\n')
