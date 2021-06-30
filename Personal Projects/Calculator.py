from time import sleep

# Funções
def Titulo():
    print('\033[7;40m-' * 40)
    print(f'{"CALCULADORA":^40}')
    print('-' * 40)

def Numeros():
    a = float(input('\nDigite primeiro numero: '))
    b = float(input('Digite segundo numero: '))
    return a, b

def Soma(x):
    print(f"\nA soma é {x[0] + x[1]}")

def Diferença(x):
    print(f"\nA diferença é {x[0] - x[1]}")

def Produto(x):
    print(f"O produto é {x[0] * x[1]}")

def Divisão(x):
    print(f"A divisão é {x[0] / x[1]}")

def Maior(x):
    if x[0] > x[1]:
        print(f"O maior valor é {x[0]}")
    else:
        print(f"O maior valor é {x[1]}")


# Programa
Titulo()
while True:
    print('''\033[m\033[33m[1] - SOMAR
[2] - DIMINUIR
[3] - MULTIPLICAR
[4] - DIVIDIR
[5] - MAIOR
[6] - SAIR DO PROGRAMA\033[m''')
    option = int(input("\nO que deseja fazer: "))
    if option == 1:
        Soma(Numeros())
    elif option == 2:
        Diferença(Numeros())
    elif option == 3:
        Produto(Numeros())
    elif option == 4:
        Divisão(Numeros())
    elif option == 5:
        Maior(Numeros())
    elif option == 6:
        break
    else:
        print('\033[31mOpção incorreta... \033[m')
    sleep(0.6)
    print("-" * 40)
   
print('\n\033[31mPrograma Finalizado\033[m')
