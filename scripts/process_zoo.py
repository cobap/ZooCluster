"""Class to process all texts."""

import pandas as pd
import numpy as np
from pandas.tools.plotting import scatter_matrix
from pandas import DataFrame
import matplotlib.pyplot as plt


class ProcessZoo():
    """."""

    def __init__(self):
        """."""
        self._read_text()

    def _read_text(self):
        """."""
        df = pd.read_csv('../database/zoo.csv', delimiter=',', header=None)
        new_df = df.drop(df.columns[0], axis=1)
        new_df = new_df.drop(df.columns[-1], axis=1)
        self.animais_matrix = np.array(new_df.values)

    def get_original_matrix(self):
        """."""
        return self.animais_matrix

    def plot_original_data(self):
        """."""
        df = DataFrame(data = Data[1:1000,:], columns= header.T)
        fig = scatter_matrix(df, alpha=0.2, figsize=(10, 10), diagonal='kde')
        plt.plot(fig)
        plt.show()
