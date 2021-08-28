# Programa com uma função "Escreva()" que recebe um texto
# e mostra uma mensagem com tamanho adaptável.

def escreva(text):
    print('~' * len(text))
    print(text)
    print('~' * len(text))

escreva('Olá Mundo!')
escreva('AdrianOliv')