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