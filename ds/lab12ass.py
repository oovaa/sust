import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.metrics import adjusted_rand_score
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage
from kmedoids import KMedoids



def load_iris_data():
    iris = load_iris()
    return iris.data, iris.target, iris.feature_names, iris.target_names

def plot_clusters(X, labels, medoids=None, feature_names=None, title="Clustering Results"):
    plt.figure(figsize=(8, 6))
    plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', edgecolor='k', alpha=0.7)
    if medoids is not None:
        plt.scatter(medoids[:, 0], medoids[:, 1], c='black', marker='X', s=200, label='Medoids', edgecolors='white')
    if feature_names:
        plt.xlabel(feature_names[0])
        plt.ylabel(feature_names[1])
    plt.title(title)
    plt.tight_layout()
    plt.show()

def plot_dendrogram(X, title="Dendrogram", truncate_mode='lastp', p=30):
    Z = linkage(X, method='ward')
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

def main():
    X, y, feature_names, _ = load_iris_data()
    n_clusters = 3

    # K-Medoids clustering
    try:
        kmedoids = KMedoids(n_clusters=n_clusters, metric='euclidean', max_iter=100)
        kmedoids.fit(X)
        kmedoids_labels = kmedoids.labels_
        medoids = X[kmedoids.medoid_indices_]
        # print("K-Medoids cluster labels:\n", kmedoids_labels)
        print("K-Medoids Adjusted Rand Index:", adjusted_rand_score(y, kmedoids_labels))
        plot_clusters(X, kmedoids_labels, medoids=medoids, feature_names=feature_names, title="K-Medoids Clustering (Iris)")
    except Exception as e:
        print("K-Medoids clustering Error:", e)

    # Agglomerative clustering
    agglo = AgglomerativeClustering(n_clusters=n_clusters, linkage='ward')
    agglo_labels = agglo.fit_predict(X)
    # print("Agglomerative cluster labels:\n", agglo_labels)
    print("Agglomerative Adjusted Rand Index:", adjusted_rand_score(y, agglo_labels))
    plot_clusters(X, agglo_labels, feature_names=feature_names, title="Agglomerative Clustering (Iris)")
    plot_dendrogram(X, title='Agglomerative Dendrogram (last 30 merges)', truncate_mode='lastp', p=30)

    # Compare clusterings
    print("Adjusted Rand Index between K-Medoids and Agglomerative:", 
          adjusted_rand_score(kmedoids_labels, agglo_labels) if 'kmedoids_labels' in locals() else "N/A")

if __name__ == "__main__":
    main()
