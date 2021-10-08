from grafo import Grafo

def obtener_aristas(grafo):
    aristas = []
    for v in grafo:
        for w in grafo.adyacentes(v):
            aristas.append((v,w,grafo.peso(v,w)))
    return aristas


def camino_minimo_bf(grafo, origen):
    distancia = {}
    padre = {}
    for v in grafo: # O(V)
        distancia[v] = float("inf")
    distancia[origen] = 0
    padre[origen] = None
    aristas = obtener_aristas(grafo) # O(V + E)
    for i in range(len(grafo)):
        for v,w, peso in aristas: # O(V*E)
            if distancia[v] + peso < distancia[w]:
                padre[w] = v
                distancia[w] = distancia[v] + peso
    for v, w, peso in aristas:
        if distancia[v] + peso < distancia[w]:
            return None # Si vuelvo a iterar y encuentro una mejoria hay un ciclo negativo
    return padre, distancia

    # complejidad O(V*E)

def camino_minimo_dijkstra(grafo,origen) :
    dist = {}
    padre = {}

    for v in grafo:
        dist[v] = float("inf") # inicializo todos los vertices en el infinito
    
    dist[origen] = 0
    padre[origen] = None
    q = Heap()
    q.encolar((0,origen))

    while not q.esta_vacio():
        v = q.desencolar()
        for w in grafo.adyacentes(v):
            if dist[v] + grafo.peso(v,w) < dist[w]:
                dist[w] = dist[v] + grafo.pesado(v, w)
                padre[w] = v
                q.encolar((dist[w], w))
                #o sino: q.actualizar(w, dist[w])
    return padre, dist 


def algoritmo_johnson(grafo, origen):
