"""."""

# import matplotlib.pylab as plt
import numpy as np
import sompy

# A toy example: two dimensional data, four clusters
# fig = plt.figure()
# plt.plot(Data1[:,0],Data1[:,1],'ob',alpha=0.2, markersize=4)
# fig.set_size_inches(7,7)
# plt.savefig('teste.jpg')


class SOM():
    """."""

    def __init__(self, animal_matrix, mapsize, parametros=""):
        """."""
        self.matrix = animal_matrix
        self.mapsize = mapsize
        self.parametros = parametros


    def train_som(self):
        """."""
        # this will use the default parameters, but i can change the initialization and neighborhood methods
        self.som = sompy.SOMFactory.build(self.matrix, self.mapsize, mask=None, mapshape='planar', lattice='rect', normalization='var', initialization='pca', neighborhood='gaussian', training='batch', name='animal_som')
        self.som.train(n_job=1, verbose='info')  # verbose='debug' will print more, and verbose=None wont print anything
        # trained_som = self.som.train(n_job=1, verbose='info')
        # som.set_parameter(neighbor=0.1, learning_rate=0.2)

    def view2dpacked(self):
        """."""
        v = sompy.mapview.View2DPacked(50, 50, 'test', text_size=8)
        # could be done in a one-liner: sompy.mapview.View2DPacked(300, 300, 'test').show(som)
        # which_dim='all' default
        # 1 visualizacao
        v.show(self.som, what='codebook', which_dim=[0, 1], cmap=None, col_sz=6)
        v.save(str(self.parametros + 'img1'))

        # 2 visualizacao
        self.som.component_names = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
        v = sompy.mapview.View2DPacked(50, 50, 'test',text_size=8)
        v.show(self.som, what='codebook', which_dim='all', cmap='jet', col_sz=6) #which_dim='all' default
        v.save(str(self.parametros + 'img2'))

        # c = sompy.mapview.View2DPacked()
        v = sompy.mapview.View2DPacked(2, 2, 'test',text_size=8)
        #first you can do clustering. Currently only K-means on top of the trained som
        cl = self.som.cluster(n_clusters=7)
        # print cl
        getattr(self.som, 'cluster_labels')

        v.show(self.som, what='cluster')
        v.save(str(self.parametros + 'img3'))

        h = sompy.hitmap.HitMapView(10, 10, 'hitmap', text_size=8, show_text=True)
        h.show(self.som)
        v.save(str(self.parametros + 'img4'))

    def visualization_umatrix(self):
        """."""
        u = sompy.umatrix.UMatrixView(50, 50, 'umatrix', show_axis=True, text_size=8, show_text=True)
        #This is the Umat value
        UMAT  = u.build_u_matrix(self.som, distance=1, row_normalized=False)

        #Here you have Umatrix plus its render
        UMAT = u.show(self.som, distance2=1, row_normalized=False, show_data=True, contooor=True, blob=False)
        u.save(str(self.parametros + 'img5'))

    def interpolation(self):
        plt.imshow(self.som, interpolation='none')
        plt.show()

# mapsize = [30,30]
# som = sompy.SOMFactory.build(Data2, mapsize, mask=None, mapshape='planar', lattice='rect', normalization='var', initialization='pca', neighborhood='gaussian', training='batch', name='sompy')  # this will use the default parameters, but i can change the initialization and neighborhood methods
# som.train(n_job=1, verbose='info')  # verbose='debug' will print more, and verbose=None wont print anything
#
# v = sompy.mapview.View2DPacked(50, 50, 'test',text_size=8)
# # could be done in a one-liner: sompy.mapview.View2DPacked(300, 300, 'test').show(som)
# v.show(som, what='codebook', which_dim=[0,1], cmap=None, col_sz=6) #which_dim='all' default
# # v.save('2d_packed_test')
#
# #In this case, K-means simply fails as expected
#
# v = sompy.mapview.View2DPacked(2, 2, 'test',text_size=8)
# #first you can do clustering. Currently only K-means on top of the trained som
# cl = som.cluster(n_clusters=4)
# v.show(som, what='cluster')
# # v.save('kmeans_test')
#
# #But Umatrix finds the clusters easily
#
# u = sompy.umatrix.UMatrixView(50, 50, 'umatrix', show_axis=True, text_size=8, show_text=True)
#
# #This is the Umat value
# UMAT  = u.build_u_matrix(som, distance=1, row_normalized=False)
#
# UMAT = u.show(som, distance2=1, row_normalized=False, show_data=True, contooor=False, blob=False)
