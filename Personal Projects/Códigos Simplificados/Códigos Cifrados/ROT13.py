alfa = ("A", "B", "C", "D", "E",
        "F", "G", "H", "I", "J",
        "K", "L", "M", "N", "O",
        "P", "Q", "R", "S", "T",
        "U", "V", "W", "X", "Y", "Z")

code = str()
msg2 = str()

msg = str(input('Mensagem: ').upper().strip())

for i in msg:
    if i not in alfa:
        code += i
    else:
        code += alfa[(alfa.index(i) + 13) % 26]
       
print(f'O código é: {code}')

for i in code:
    if i not in alfa:
        msg2 += i
    else:
        msg2 += alfa[(alfa.index(i) + 13) % 26]
        
print(f'A msg descriptografada: {msg2}')
