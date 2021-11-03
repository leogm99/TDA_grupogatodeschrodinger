from grafo import Grafo
import max_flow


def main():
    g = Grafo(dirigido=True)

    # para este grafo se espera un max_flow de 23
    g.agregar_vertice('s')
    g.agregar_vertice('t')
    g.agregar_vertice('v1')
    g.agregar_vertice('v2')
    g.agregar_vertice('v3')
    g.agregar_vertice('v4')

    g.agregar_arista('s', 'v1', 16)
    g.agregar_arista('s', 'v2', 13)
    g.agregar_arista('v1', 'v2', 10)
    g.agregar_arista('v2', 'v1', 4)
    g.agregar_arista('v1', 'v3', 12)
    g.agregar_arista('v3', 'v2', 9)
    g.agregar_arista('v2', 'v4', 14)
    g.agregar_arista('v4', 'v3', 7)
    g.agregar_arista('v3', 't', 20)
    g.agregar_arista('v4', 't', 4)

    print(g)
    # despues de esto, g es modificado (por ser puntero)!
    flow = max_flow.max_flow_ford_fulkerson(g, 's', 't')
    print(f"El flujo maximo es {flow}")


if __name__ == '__main__':
    main()
