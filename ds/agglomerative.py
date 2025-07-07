import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage

def load_iris_data():
    iris = load_iris()
    return iris.data, iris.target, iris.feature_names, iris.target_names

def plot_dendrogram(data, title="Dendrogram", truncate_mode=None, p=30):
    Z = linkage(data, method='ward')
    plt.figure(figsize=(10, 5))
    plt.title(title)
    dendrogram(
        Z,
        truncate_mode=truncate_mode,
        p=p,
        leaf_rotation=90.,
        leaf_font_size=8.,
        show_contracted=True,
    )
    plt.tight_layout()
    plt.show()

def plot_clusters(X, labels, feature_names):
    plt.figure(figsize=(8, 6))
    plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', edgecolor='k')
    plt.xlabel(feature_names[0])
    plt.ylabel(feature_names[1])
    plt.title("Agglomerative Clustering Results")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    X, y, feature_names, target_names = load_iris_data()
    
    n_clusters = 3
    labels = AgglomerativeClustering(n_clusters=n_clusters, linkage='ward').fit_predict(X)
    print(f"Cluster labels for {n_clusters} clusters:\n{labels}")

    plot_clusters(X, labels, feature_names)
    plot_dendrogram(X, title='Truncated Dendrogram (last 30 merges)', truncate_mode='lastp', p=30)
