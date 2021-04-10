# Proframa Orientado a Objeto
# Primeiras Tentativas

class Cube(object):
    def __init__(self,aresta):
        self.aresta = aresta
    
    def area(self):
        return self.aresta * self.aresta
    
    def volume(self):
        return Cube.area(self) * 6
        
c = Cube(4)
print(c.area())
print(c.volume())
