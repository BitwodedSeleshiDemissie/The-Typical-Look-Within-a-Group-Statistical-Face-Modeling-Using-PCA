import numpy as np

class PCAFromScratch:
    def __init__(self, n_components=None):
        self.n_components = n_components
        self.mean_ = None
        self.components_ = None
        self.explained_variance_ratio_ = None

    def fit(self, X):
        """
        PCA using the compact trick (eigen-decomposition of X X^T).
        Much faster for high-dimensional images.
        """
        # Center data
        self.mean_ = np.mean(X, axis=0)
        X_centered = X - self.mean_
        n_samples = X_centered.shape[0]

        # Covariance-like matrix
        C = np.dot(X_centered, X_centered.T) / n_samples
        eigvals, eigvecs = np.linalg.eigh(C)

        # Sort eigenvalues (descending)
        sorted_idx = np.argsort(eigvals)[::-1]
        eigvals = eigvals[sorted_idx]
        eigvecs = eigvecs[:, sorted_idx]

        # Keep top components
        if self.n_components:
            eigvals = eigvals[:self.n_components]
            eigvecs = eigvecs[:, :self.n_components]

        # Compute eigenfaces
        eigenfaces = np.dot(X_centered.T, eigvecs)
        eigenfaces = eigenfaces / np.linalg.norm(eigenfaces, axis=0)

        self.components_ = eigenfaces.T
        self.explained_variance_ratio_ = eigvals / np.sum(eigvals)
        return self

    def transform(self, X):
        X_centered = X - self.mean_
        return np.dot(X_centered, self.components_.T)

    def inverse_transform(self, X_proj):
        return np.dot(X_proj, self.components_) + self.mean_

