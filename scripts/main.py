"""."""

from process_zoo import ProcessZoo
from som import SOM

def le_parametros():
	"""Parametros para inpute no KMEANS e SOM.
		1 - tamanho do mapsize
		2 - tipo de vizinhança (gaussiana, bubble)
		3 - inicializando do SOM (PCA, aleatoria)
		4 - SOM clusters para visualizacao
	"""

	parametros = None
	with open('./parametros.txt', 'r') as inp:
		parametros = inp.read().splitlines()
	return parametros

if __name__ == "__main__":
	pre_process = ProcessZoo()
	animal_matrix = pre_process.get_original_matrix()

	for parametros in le_parametros():
		print(parametros)
		_mapsize = int(parametros[0])*10
		som = SOM(animal_matrix=animal_matrix, mapsize=[_mapsize, _mapsize], parametros=parametros)
		som.train_som()
		som.view2dpacked()
		som.visualization_umatrix()
		som.interpolation()
