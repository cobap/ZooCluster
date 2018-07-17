"""."""

from process_zoo import ProcessZoo
from som import SOM
from kmeans import Kmeans


def le_parametros():
	"""Parametros para inpute no KMEANS e SOM.

	1 - tamanho do mapsize
	2 - tipo de vizinhanca (gaussiana, bubble)
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
		############################# SOM #############################
		print(parametros)
		_mapsize = int(parametros[0])*10
		som = SOM(animal_matrix=animal_matrix, mapsize=[_mapsize, _mapsize], parametros=parametros)
		# som.view2dpacked()
		# som.train_som()
		# som.view2dpacked()
		# som.visualization_umatrix()
		# som.interpolation()

		############################# KMEANS #############################
		kmeans = Kmeans(points=animal_matrix, k_centroids=4, n_iteracoes=100, error=0.1)
		kmeans.run_kmeans()

		############################# POS PROCESSAMENTO #############################
