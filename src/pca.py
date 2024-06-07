import numpy as np

class PCA:
    """
    Class to perform Principal Component Analysis (PCA) on a dataset.
    """
    
    @staticmethod
    def __call__(self, X: np.ndarray, dim: int) -> np.ndarray:
        """
        Run PCA on a dataset to reduce its dimensionality.
        """
        return self.pca(X, dim)
    
    @staticmethod
    def covariance(X: np.ndarray) -> np.ndarray:
        """
        Calculate the covariance matrix of a dataset.
        """
        if not isinstance(X, np.ndarray):
            X = np.array(X)

        assert X.ndim == 2, "X must be a 2D array"

        n_samples = X.shape[0]
        return np.dot(X.T, X) / (n_samples - 1)

    @staticmethod
    def pca(X: np.ndarray, dim: int) -> np.ndarray:
        """
        Run PCA on a dataset to reduce its dimensionality.
        """
        if not isinstance(X, np.ndarray):
            X = np.array(X)

        assert isinstance(dim, int) and dim > 0, "dim must be a positive int"
        assert X.ndim == 2, "X must be a 2D array"
        assert dim <= X.shape[1], "dim must be <= number of columns in X"

        # center the matrix
        X_centered = X - np.mean(X, axis=0)

        # calculate the covariance matrix 
        cov = PCA.covariance(X_centered)

        # diagonalize the covariance matrix
        eigenvalues, eigenvectors = np.linalg.eigh(cov)

        # sort the eigenvalues and eigenvectors
        sorted_indices = np.argsort(eigenvalues)[::-1]
        sorted_eigenvalues = eigenvalues[sorted_indices]
        sorted_eigenvectors = eigenvectors[:, sorted_indices]

        # select the top-dim eigenvectors corresponding to the largest eigenvalues
        projection_matrix = sorted_eigenvectors[:, :dim]

        # project the centered data onto the new feature space
        X_projected = np.dot(X_centered, projection_matrix)
        
        return X_projected