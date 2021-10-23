import urllib
from urllib import request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('Erro! Não foi possível conectar.')
else:
    print('Site Conectado!')
