# Programa com função que verifica maior número.

def maior(num):
    return(max(num))
    
num = ()
while True:
    num += (int(input("Núm: ")), )
    o = str(input("Continuar? "))
    print("×" * 40)
    if o in "Nn":
        break

print(f"\nO maior número digitado foi {maior(num)}.")
