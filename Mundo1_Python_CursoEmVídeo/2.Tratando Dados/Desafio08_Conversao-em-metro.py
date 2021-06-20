#Metros convertido em Milímetro e centímetros
n = float(input('Qual a metragem? '))
print(f'''Essa metragem em outras unidades é:
    {n/1000}km
    {n/100} hm
    {n/10}  dam
    {n}     m
    {n*10}  dm
    {n*100} cm
    {n*1000}mm''')
