import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets.samples_generator import make_blobs

X, y_true = make_blobs(n_samples=800, centers=5, cluster_std=0.45, random_state=0)
plt.scatter(X[:,0], X[:,1], s=30)
func = KMeans(n_clusters=5)
func.fit(X)
y_func = func.predict(X)
plt.scatter(X[:,0], X[:,1], c=y_func, s=15)
centers = func.cluster_centers_
plt.scatter(centers[:,0], centers[:,1], c='red', s=75, alpha=1)
plt.show()






