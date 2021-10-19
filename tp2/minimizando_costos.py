from grafo import *
from caminos_minimos import *
import pandas as pd
import argparse


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument('-f', '--file', dest='file', help='Path al archivo de ciudades', required=True)
	args = parser.parse_args()

	g = Grafo(True)
	try:
		cargar_grafo(g, args.file)
	except FileNotFoundError:
		print("Archivo invalido")
		return -1
	except BaseException as err:
		print("{}".format(err))
		return -1

	distancias_totales = camino_minimo_johnson(g)
	matriz_caminos_minimos(distancias_totales)
	vertice = obtener_vertice_ideal(distancias_totales)
	print("El vertice ideal es " + str(vertice))

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
			g.agregar_arista(s, t, int(w))

def matriz_caminos_minimos(distancias_totales):
	df = pd.DataFrame(distancias_totales)
	print(df.T)				

if __name__ == '__main__':
	main()