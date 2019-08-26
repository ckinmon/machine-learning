import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

image = plt.imread('trees.png')
arr = np.array(image)
samples, x, y = arr.shape
newarr = arr.reshape(samples, x * y)
kmeans = KMeans(n_clusters=3).fit(newarr)
#print(kmeans.labels_)
print(kmeans.cluster_centers_)