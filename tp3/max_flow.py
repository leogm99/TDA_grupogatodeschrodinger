from grafo import Grafo
from math import inf
from collections import deque


# depth-first search
def dfs(graph: Grafo, vertex, visited):
    pass


# path de aumento utilizando BFS
def augmenting_path(graph: Grafo, vertex_source, vertex_sink):
    path_from_source_to_sink = False
    aux = [False for _ in graph.vertices.keys()]
    visited = dict(zip(graph.vertices.keys(), aux))
    visited_q = deque([vertex_source])
    visited[vertex_source] = True
    parent = {}

    while len(visited_q) != 0:
        u = visited_q.popleft()

        for v_neighbour in graph.obtener_adyacentes(u):
            if not visited[v_neighbour]:
                """ si el peso es 0, no hay camino entre los dos"""
                """ esto puede pasar porque ya maxeamos el flujo en esa arista """
                if not graph.obtener_peso(u, v_neighbour):
                    continue
                visited_q.append(v_neighbour)
                visited[v_neighbour] = True
                parent[v_neighbour] = u
                """ en caso de haber encontrado al sink, ya encontramos un path, entonces nos vamos """
                if v_neighbour is vertex_sink:
                    path_from_source_to_sink = True
                    break
    return path_from_source_to_sink, parent


# modifica la referencia al grafo
# el grafo queda como el 'residual'
def max_flow_ford_fulkerson(graph: Grafo, vertex_source, vertex_sink):
    max_flow = 0

    while True:
        exists_path, parent = augmenting_path(graph, vertex_source, vertex_sink)
        if not exists_path:
            break
        path_flow = inf
        aux_vertex = vertex_sink
        while aux_vertex is not vertex_source:
            path_flow = min(path_flow, graph.obtener_peso(parent[aux_vertex], aux_vertex))
            aux_vertex = parent[aux_vertex]

        max_flow += path_flow

        aux_vertex = vertex_sink
        while aux_vertex is not vertex_source:
            new_weight_forward = graph.obtener_peso(parent[aux_vertex], aux_vertex) - path_flow
            graph.cambiar_peso(parent[aux_vertex], aux_vertex, new_weight_forward)
            """ si no existe la arista para atras la tengo que agregar """
            if not graph.existe_arista(aux_vertex, parent[aux_vertex]):
                graph.agregar_arista(aux_vertex, parent[aux_vertex], path_flow)
            else:
                new_weight_backwards = graph.obtener_peso(aux_vertex, parent[aux_vertex]) + path_flow
                graph.cambiar_peso(aux_vertex, parent[aux_vertex], new_weight_backwards)

            aux_vertex = parent[aux_vertex]

    return max_flow
