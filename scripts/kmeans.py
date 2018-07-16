"""."""
import numpy as np


class Kmeans():
    """."""

    def __init__(self, points, k_centroids, n_iteracoes=100, error=0.1):
        """Generate a KMeans model for a specific 'k' and a n-matrix of point.

        It will return a model which represents the k-means cluster function
        """
        self.points = points
        self.n_iteracoes = n_iteracoes
        self.error = error
        self.k = k_centroids

        centroids = self.points.copy()
        np.random.shuffle(centroids)
        self.centroids = centroids[:k_centroids]

    def calc_distancia(self, pointA, pointB, type='euclidian'):
        """Calcula distancia entre pontoA e pontoB.

        1 - Euclidiana
        2 - Similaridade cosseno
        """
        point_to_centroids = 0
        if type == 'euclidian':
            centroid_vencedor = np.sqrt(((pointA - pointB) ** 2).sum(axis=1)).argmin(axis=0)
            point_to_centroids = centroid_vencedor + 1
            return point_to_centroids
        if type == 'cosseno':
            return None

    def recalcula_centroids(self, novos_centroids):
        """Dado uma lista de lista de pontos, calculamos os novos centroids."""
        _novos_centroids = [0] * (self.k+1)
        contador_pontos = [0] * (self.k+1)
        for ponto in novos_centroids:
            centroid_winner = list(ponto.keys())[0]
            _novos_centroids[centroid_winner] += list(ponto.values())[0]
            contador_pontos[centroid_winner] += 1
        for iterador in range(1, self.k+1):
            _novos_centroids[iterador] = _novos_centroids[iterador]/contador_pontos[iterador]
        _novos_centroids.pop(0)
        _novos_centroids = np.array(_novos_centroids)
        self.centroids = _novos_centroids
        # with open('log.txt', 'w') as inp:
        #     inp.write(str(self.centroids))
        #     inp.write(str(self.centroids.shape))
        # with open('log2.txt', 'w') as inp:
        #     inp.write(str(_novos_centroids))
        #     inp.write(str(_novos_centroids.shape))

    def run_kmeans(self):
        """Roda kmeans ate convergir."""
        _iteracoes = 0
        _novos_centroids = []
        # avg_dist_atual = 0
        # avg_dist_anterior = 100

        # print('Centroid shape:', self.centroids.shape)
        # print('Points shape:', self.points.shape)

        # while((_iteracoes < self.n_iteracoes) or (abs(avg_dist_anterior - avg_dist_atual) > self.error)):
        # Enquanto nao batermos os numeros de iteracoes minimas
        while((_iteracoes < self.n_iteracoes)):
            # A cada 10 iteracoes damos um print
            if(_iteracoes % 10 == 0):
                print('-- iteracao' + str(_iteracoes) + ' --')
                # print(str(_iteracoes) + " vs " + str(self.n_iteracoes))
            _iteracoes += 1
            # Para cada linha do dataset, identificamos o centroid mais proximo
            for _data in self.points:
                _ponto = {}
                centroid_vencedor = self.calc_distancia(self.centroids, _data)
                _ponto[centroid_vencedor] = _data
                _novos_centroids.append(_ponto)
            self.recalcula_centroids(_novos_centroids)
