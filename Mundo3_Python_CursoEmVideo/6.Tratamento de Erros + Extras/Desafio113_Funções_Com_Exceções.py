# Begin
def leiaInt(x):
    while True:
        print(x, end = ' ')
        try:
            num = int(input())
            return num
        except ValueError:
            print('Você digitou um número inválido!')
        except KeyboardInterrupt:
            print('\nVocê cancelou a inserção!')
            return 0

def leiaFloat(x):
    while True:
        print(x, end = ' ')
        try:
            num = float(input().replace(',', '.'))
            return num
        except ValueError:
            print('Você digitou um número inválido!')
        except KeyboardInterrupt:
            print('\nVocê cancelou a inserção!')
            return 0


# Main
x = leiaInt("Escreva um inteiro:")
y = leiaFloat("\nEscreva um decimal: ")
print(f'\nVocê digitou o Inteiro -> {x} e o Float -> {y}.')