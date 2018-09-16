from dataset_reader import get_trip_points
from drawing_functions import draw_map_with_clusters
from point import distance

import numpy as np
from sklearn.cluster import DBSCAN, KMeans

# Read data from file.
points = get_trip_points('data/trips.csv')

# Format expected by clustering functions: N by 2 matrix (N samples, 2 dimensions: x[0] - latitude; x[1] - longitude)
X = np.array([[p.latitude, p.longitude] for p in points])

# Do the clustering:
# labels = KMeans(n_clusters=10).fit_predict(X)
labels = DBSCAN(eps=100, min_samples=10, metric=distance).fit_predict(X)

draw_map_with_clusters(X, labels)
