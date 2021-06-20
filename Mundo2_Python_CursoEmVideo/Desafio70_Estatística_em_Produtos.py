# Lêr nome e preço de vários produtos.
# Qual total gasto na compra, Quantos custam mais de mil.
# Qual o nome do prod mais barato?

i = 'y'
s = hund = p_cheap = 0
cheap = str()
while i == 'y':
    prod = input('Nome prod: ')
    price = float(input('Preço: '))
    if price >= 1000:
        hund += 1
    if s == 0:
        cheap = prod
        p_cheap = price
    elif price < p_cheap:
        p_cheap = price
        cheap = prod
    s += price
    i = input('Continue (y/n)...')

print(f'O total gasto foi R${s}.')
print(f'{cheap} foi o prod mais barato.')
print(f'{hund} produtos acima de mil.')
print('Programa Finalizado!')
