import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from kmedoids import KMedoids

def main():
    # Load Iris data
    iris = load_iris()
    X = iris.data
    feature_names = iris.feature_names

    # K-Medoids clustering
    n_clusters = 3
    model = KMedoids(n_clusters=n_clusters, metric='euclidean', max_iter=100)
    model.fit(X)
    labels = model.labels_
    medoids = X[model.medoid_indices_]
    print(model.labels_)

    # Plot (first two features)
    plt.figure(figsize=(8, 6))
    for i in range(n_clusters):
        plt.scatter(X[labels == i, 0], X[labels == i, 1], label=f'Cluster {i+1}', alpha=0.7)
    plt.scatter(medoids[:, 0], medoids[:, 1], c='black', marker='X', s=200, label='Medoids', edgecolors='white')
    plt.xlabel(feature_names[0])
    plt.ylabel(feature_names[1])
    plt.title('K-Medoids Clustering (Iris)')
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
