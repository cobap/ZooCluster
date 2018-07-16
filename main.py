"""."""

from process_zoo import ProcessZoo
from som import SOM

if __name__ == "__main__":
	pre_process = ProcessZoo()
	animal_matrix = pre_process.get_original_matrix()
	som = SOM(animal_matrix=animal_matrix, mapsize=[20, 20])
	# print(animal_matrix)
	# print(animal_matrix[0].dtype)
	som.train_som()
	som.view2dpacked()
	som.visualization_umatrix()
