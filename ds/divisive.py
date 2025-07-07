import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from scipy.cluster.hierarchy import dendrogram, linkage

def load_iris_data():
    iris = load_iris()
    X = iris.data
    feature_names = iris.feature_names
    return X, feature_names

def plot_agglomerative_dendrogram(X):
    Z = linkage(X, method='ward')
    plt.figure(figsize=(10, 5))
    plt.title('Agglomerative Dendrogram (Ward Linkage)')
    plt.xlabel('Sample Index or (Cluster Size)')
    plt.ylabel('Distance')
    dendrogram(
        Z,
        truncate_mode='lastp',
        p=30,
        leaf_rotation=90.,
        leaf_font_size=8.,
        show_contracted=True,
    )
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    X, feature_names = load_iris_data()
    plot_agglomerative_dendrogram(X)
