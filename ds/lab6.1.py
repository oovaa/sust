# Import required libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.decomposition import TruncatedSVD
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.manifold import TSNE
from umap import UMAP
from sklearn.preprocessing import StandardScaler

# Load and preprocess Iris dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target
target_names = iris.target_names

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)



# SVD with 2 components
svd = TruncatedSVD(n_components=2, random_state=42)
X_svd = svd.fit_transform(X_scaled)

# Plot results
plt.figure(figsize=(8, 6))
for i, name in enumerate(target_names):
    plt.scatter(X_svd[y == i, 0], X_svd[y == i, 1], label=name, alpha=0.8)
plt.title('SVD of Iris Dataset', fontsize=14)
plt.xlabel('SVD Component 1', fontsize=12)
plt.ylabel('SVD Component 2', fontsize=12)
plt.legend()
plt.grid(alpha=0.3)
plt.show()

# Explained variance
print(f"Explained variance ratio: {svd.explained_variance_ratio_}")
print(f"Total explained variance: {sum(svd.explained_variance_ratio_):.3f}")


# LDA with 2 components
lda = LinearDiscriminantAnalysis(n_components=2)
X_lda = lda.fit_transform(X_scaled, y)

# Plot results
plt.figure(figsize=(8, 6))
for i, name in enumerate(target_names):
    plt.scatter(X_lda[y == i, 0], X_lda[y == i, 1], label=name, alpha=0.8)
plt.title('LDA of Iris Dataset', fontsize=14)
plt.xlabel('LDA Component 1', fontsize=12)
plt.ylabel('LDA Component 2', fontsize=12)
plt.legend()
plt.grid(alpha=0.3)
plt.show()

# Explained variance
print(f"Explained variance ratio: {lda.explained_variance_ratio_}")



# t-SNE with 2 components
tsne = TSNE(n_components=2, random_state=42, perplexity=30)
X_tsne = tsne.fit_transform(X_scaled)

# Plot results
plt.figure(figsize=(8, 6))
for i, name in enumerate(target_names):
    plt.scatter(X_tsne[y == i, 0], X_tsne[y == i, 1], label=name, alpha=0.8)
plt.title('t-SNE of Iris Dataset', fontsize=14)
plt.xlabel('t-SNE Dimension 1', fontsize=12)
plt.ylabel('t-SNE Dimension 2', fontsize=12)
plt.legend()
plt.grid(alpha=0.3)
plt.show()





# UMAP with 2 components
umap = UMAP(n_components=2, random_state=42, n_neighbors=15, min_dist=0.1)
X_umap = umap.fit_transform(X_scaled)

# Plot results
plt.figure(figsize=(8, 6))
for i, name in enumerate(target_names):
    plt.scatter(X_umap[y == i, 0], X_umap[y == i, 1], label=name, alpha=0.8)
plt.title('UMAP of Iris Dataset', fontsize=14)
plt.xlabel('UMAP Dimension 1', fontsize=12)
plt.ylabel('UMAP Dimension 2', fontsize=12)
plt.legend()
plt.grid(alpha=0.3)
plt.show()