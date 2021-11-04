from grafo import Grafo
import max_flow


# se redujo el problema a max_flow (polinomialmente)
# se resuelve mediante ford fulkerson el problema de flujo maximo (pseudo polinomial)
# para luego poder encontrar el min-cut, o las aristas de corte minimo
# el grafo residual otorga las aristas del corte minimo
# (son las que van desde un vertice alcanzable por la fuente a un vertice no alcanzable)
# estas se pueden encontrar con dfs/bfs
# TODO: args
def main():
    # para este grafo se espera un max_flow de 23
    # ademas debo cortar las aristas (F, E), (F, B) y (C, E)
    # de tal manera de generar un corte minimo (el corte de menor costo posible)
    # en estas aristas debería poner las publicidades
    # me aseguro que TODOS los que van de s a t vean los carteles ya que
    # estas aristas cortan al grafo en dos componentes conexas, una contiene a s y otra contiene a t

    g = load_graph('test.txt')
    print(g)

    # despues de esto, g es modificado (por ser puntero)!
    # g se transforma en el grafo residual
    flow = max_flow.max_flow_ford_fulkerson(g, 'A', 'B')
    print(f"El costo total de los carteles será {flow}")
    print_solution(max_flow.modified_dfs(g, 'A'))


def load_graph(filename):
    g = Grafo(dirigido=True)
    with open(filename, 'r') as f:
        g.agregar_vertice(f.readline().strip())
        g.agregar_vertice(f.readline().strip())
        while True:
            line_list = f.readline().strip().split(',')
            if len(line_list) < 3:
                break
            s, t, w = tuple(line_list)
            if not g.existe_vertice(s):
                g.agregar_vertice(s)
            if not g.existe_vertice(t):
                g.agregar_vertice(t)
            g.agregar_arista(s, t, int(w))
    return g


def print_solution(non_reachable):
    [print(f"Poner un cartel publicitario entre {u} y {v}") for u, v in non_reachable]


if __name__ == '__main__':
    main()
