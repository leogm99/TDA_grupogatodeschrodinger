def cargar_grafo(nombre_archivo):
    red_criminal = Grafo(True)
    with open(nombre_archivo,'r') as archivo:
        for linea in archivo:
            linea_separada = linea.split('\t')
            red_criminal.agregar_vertice(linea_separada[0].rstrip())
            red_criminal.agregar_vertice(linea_separada[1].rstrip())
            red_criminal.agregar_arista(linea_separada[0].rstrip(),linea_separada[1].rstrip())
    return red_criminal