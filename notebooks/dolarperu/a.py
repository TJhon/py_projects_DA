from sklearn.cluster import KMeans
from sklearn import metrics
import pandas as pd

dataset, classes = make_blobs(n_samples=500, centers=2, n_features=2, random_state=311)
df = pd.DataFrame(dataset, columns=["a", "b"])

model = KMeans(n_clusters=2, random_state=10).fit(df)
labels = model.labels_
centers = model.cluster_centers_

# Calculate the Silhouette Coefficient
model_performance = metrics.silhouette_score(df, labels)
print("Model A:", model_performance)
