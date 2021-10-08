from random import seed
from random import randint

class Grafo:
    
    def __init__ (self, dirigido = False):
        '''
            Inicializa un grafo vacío.
            Por default el grafo es no dirigido.
        '''
        self.vertices = {}
        self.cantidad = 0
        self.es_dirigido = dirigido
    
    def agregar_vertice(self,vertice):
        '''
            Agrega un vertice, si el vertice
            ya existe no lo pisa.
        '''
        if vertice not in self.vertices:
            self.vertices[vertice] = {}
            self.cantidad += 1

    def borrar_vertice(self,vertice):
        '''
            Si el vertice esta en el grafo lo borra.
        '''
        if vertice in self.vertices:
            for v in self.vertices:
                if v == vertice:
                    continue
                elif vertice in self.vertices[v]:
                    self.vertices[v].pop(vertice)
            self.vertices.pop(vertice)
            self.cantidad -= 1
        else:
            raise ValueError("No se puede borrar un vertice inexistente")
            
    def agregar_arista(self,vertice1,vertice2,peso = 1):
        '''
            Agrega una arista entre dos vertices existentes
            del grafo, en caso contrario devuelve error.
            Si no se le pasa el peso, por default es 1
        '''        
        if vertice1 and vertice2 in self.vertices:
            if self.es_dirigido:
                self.vertices[vertice1][vertice2] = peso
            else:
                self.vertices[vertice1][vertice2] = peso
                self.vertices[vertice2][vertice1] = peso
        else:
            raise ValueError("No es posible agregar arista")
    
    def borrar_arista(self,vertice1,vertice2):
        '''
            Si los vertices estan unidos, borra la arista
            en caso contrario devuelve error
        '''
        if self.estan_unidos(vertice1,vertice2):
            if self.es_dirigido:
                    self.vertices[vertice1].pop(vertice2)
            else:
                self.vertices[vertice1].pop(vertice2)
                self.vertices[vertice2].pop(vertice1)
        else: 
            raise ValueError("No es posible borrar la arista")
    
    def estan_unidos(self,vertice1,vertice2):
        '''
            Verifica si dos vertices estan unidos.
            Devuelve True si lo estan o false en caso 
            contrario (o si alguna de los dos vertices 
            no existe).
        '''
        if (vertice1 or vertice2) not in self.vertices:
            return False
        if self.es_dirigido:
            if vertice2 in self.vertices[vertice1]:
                return True
            if vertice1 in self.vertices[vertice2]:
                return True
        else:
            if vertice2 in self.vertices[vertice1]:
                return True
        return False

    def obtener_peso(self,vertice1,vertice2):
        '''
            Devuelve el peso entre dos vertices
            unidos o 0 en caso que no lo esten.
        '''
        if self.estan_unidos(vertice1,vertice2):
            return self.vertices[vertice1][vertice2]
        else: return 0
    
    def obtener_adyacentes(self,vertice):
        '''
            Devuelve los adyacentes de un vertice
            o error en caso que el vertice no se 
            encuentre en el grafo.
        '''
        adyacentes = []
        if vertice in self.vertices:
            for v in self.vertices[vertice]:
                adyacentes.append(v)
        else:
            raise ValueError("Vertice inexistente, no se puede obtener las aristas")
        return adyacentes
    
    def existe_vertice(self,vertice):
        '''
            Devuelve True en caso que el vertice
            se encuentre en el grafo, False en caso 
            contrario
        '''
        if vertice in self.vertices:
            return True
        else: return False
    
    def obtener_vertices(self):
        '''
            Obtiene todos los vertices
            del grafo.
        '''
        vertices = []
        for v in self.vertices:
            vertices.append(v)
        return vertices

    def vertice_aleatorio(self):
        '''
            Devuelve un vertice aleatorio
            o None en caso que el grafo este
            vacío
        '''

        if self.cantidad == 0: return None
        
        seed()
        i = randint(0, self.cantidad - 1)
        vertices = list(self.vertices)

        return vertices[i]
    
    def obtener_entradas(self,vertice):
        '''
            Recibe el vertice al cual se le quiere
            calcular las entradas. 
            Devuelve una tupla, la lista con las entradas
            y la cantidad de entradas
        '''
        if vertice not in self.vertices:
            raise ValueError("Vertice inexistente, no puede obtenerse las entradas")
        entradas = []
        cant = 0
        for v in self.vertices:
            if v == vertice:
                continue
            else:
                if vertice in self.vertices[v]:
                    entradas.append(v)
                    cant += 1

        return entradas
    
    def cantidad_vertices(self):
        return self.cantidad
        
    def __repr__(self):
        return self.vertices

    def __str__(self):
        return str(self.vertices)
    
    def __len__(self):
        return self.cantidad
