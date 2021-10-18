from grafo import *
import heapq


def obtener_aristas(grafo: Grafo):
    aristas = []
    for v in grafo.obtener_vertices():
        for w in grafo.obtener_adyacentes(v):
            aristas.append((v, w, grafo.obtener_peso(v, w)))
    return aristas


def camino_minimo_bf(grafo: Grafo, origen):
    distancia = {}
    padre = {}
    for v in grafo.obtener_vertices():  # O(V)
        distancia[v] = float("inf")
    distancia[origen] = 0
    padre[origen] = None
    aristas = obtener_aristas(grafo)  # O(V + E)
    for i in range(len(grafo)):
        for v, w, peso in aristas:  # O(V*E)
            if distancia[v] + peso < distancia[w]:
                padre[w] = v
                distancia[w] = distancia[v] + peso
    for v, w, peso in aristas:
        if distancia[v] + peso < distancia[w]:
            return None, None  # Si vuelvo a iterar y encuentro una mejoria hay un ciclo negativo
    return padre, distancia

    # complejidad O(V*E)


def camino_minimo_dijkstra(grafo: Grafo, origen):
    dist = {}
    padre = {}

    for v in grafo.obtener_vertices():
        dist[v] = float("inf")  # inicializo todos los vertices en el infinito

    dist[origen] = 0
    padre[origen] = None
    q = []
    heapq.heappush(q, (0, origen))

    while len(q) != 0:
        v = heapq.heappop(q)
        for w in grafo.obtener_adyacentes(v[1]):
            if dist[v[1]] + grafo.obtener_peso(v[1], w) < dist[w]:
                dist[w] = dist[v[1]] + grafo.obtener_peso(v[1], w)
                padre[w] = v[1]
                heapq.heappush(q, (dist[w], w))
                # o sino: q.actualizar(w, dist[w])
    return padre, dist


def camino_minimo_johnson(grafo: Grafo):
    v = grafo.vertice_aleatorio()
    distancia = camino_minimo_bf(grafo, v)[1]
    if distancia is None:
        print("El grafo contiene ciclos negativos.")
    else:
        grafo_modificado = Grafo(True)
        for v in grafo.obtener_vertices():
            for w in grafo.obtener_adyacentes(v):
                peso_nuevo = grafo.obtener_peso(v, w) + distancia[v] - distancia[w]
                grafo_modificado.agregar_vertice(v)
                grafo_modificado.agregar_vertice(w)
                grafo_modificado.agregar_arista(v, w, peso_nuevo)
        distancias_totales = {}
        for v in grafo_modificado.obtener_vertices():
            distancias_totales[v] = camino_minimo_dijkstra(grafo_modificado, v)[1]
            for w in grafo_modificado.obtener_vertices():
                distancias_totales[v][w] = distancias_totales[v][w] + distancia[w] - distancia[v]
        return distancias_totales


def obtener_vertice_ideal(diccionario):
    distancias = {}
    for dep,dic in diccionario.items():
        distancias[dep] = 0
        for k,v in dic.items():
            distancias[dep] = distancias[dep] + v
   
    vertice_ideal = min(distancias.items(), key=lambda x: x[1])
    return vertice_ideal[0]

