from grafo import *


def main():
	g = Grafo()
	cargar_grafo(g, "prueba_parse.txt")



def cargar_grafo(g: Grafo, archivo: str) -> None:
	with open(archivo, "r") as f:
		while True:
			line_list = f.readline().strip().split(',')
			if len(line_list) < 3:
				break
			s, t, w = tuple(line_list)
			if not g.existe_vertice(s):
				g.agregar_vertice(s)
			if not g.existe_vertice(t):
				g.agregar_vertice(t)
			g.agregar_arista(s, t, w)
	print(g)




if __name__ == '__main__':
	main()
