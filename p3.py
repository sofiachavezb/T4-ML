from src import PCA
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA as SKPCA
"""
Dataset:
https://www.kaggle.com/datasets/fedesoriano/company-bankruptcy-prediction
"""

DATASET_PATH = "data.csv"
N_SUB_DATASETS = 6
PROJECTION_DIM = 2
COMPARE_AGAINST_SKLEARN = True

# Fix seeds for reproducibility
np.random.seed(0)

with open(DATASET_PATH, "r") as file:
    data = file.readlines()
    data = data[1:]  # Remove header
    rows = [row.strip().split(",") for row in data]
    rows = [[float(cell) for cell in row] for row in rows]

# Initialize Numpy matrix
X = np.array(rows)

# Split dataset into sub-datasets of columns
sub_datasets = np.split(X, N_SUB_DATASETS, axis=1)

scratch_results = []
sklearn_results = []
# Run PCA on each sub-dataset
for i, sub_dataset in enumerate(sub_datasets):
    pca = PCA.pca(sub_dataset, PROJECTION_DIM)
    scratch_results.append(pca)
    if COMPARE_AGAINST_SKLEARN:
        sklearn_pca = SKPCA(n_components=PROJECTION_DIM, random_state=0)
        sklearn_result = sklearn_pca.fit_transform(sub_dataset)
        sklearn_results.append(sklearn_result)

    
# plot results
fig = plt.figure()
for i, result in enumerate(scratch_results):
    plt.subplot(2, 3, i+1)
    plt.scatter(result[:, 0], result[:, 1],s=1, c='b', marker='o')
    if COMPARE_AGAINST_SKLEARN:
        plt.scatter(sklearn_results[i][:, 0], sklearn_results[i][:, 1], s=1, c='r', marker='x')
    plt.title(f"Sub-dataset {i+1}")

plt.scatter([], [], s=1, c='r', marker='x', label=f"sklearn")
plt.scatter([], [], s=1, c='b', marker='o', label=f"implementacion propia")
plt.suptitle(f"PCA en {N_SUB_DATASETS} sub-datasets")
fig.legend(loc='lower center', ncol=2, fontsize=12)
plt.tight_layout()
plt.show()