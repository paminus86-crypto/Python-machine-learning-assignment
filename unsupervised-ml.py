import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

customer_data = [
    [1000, 2],
    [1500, 3],
    [2000, 2],
    [5000, 6],
    [6000, 7],
    [5500, 5],
    [12000, 12],
    [15000, 14],
    [13000, 11],
    [3000, 4]
]

X = np.array(customer_data)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)

kmeans.fit(X_scaled)

clusters = kmeans.labels_

print("--- Customer Cluster Assignments ---")
for i, cluster in enumerate(clusters):
    customer_num = i + 1
    print(f"Customer {customer_num} belongs to Cluster {cluster}")

print("\n--- Customers per Cluster ---")
for cluster_id in range(3):
    count = np.sum(clusters == cluster_id)
    print(f"Cluster {cluster_id}: {count} customers")

plt.figure(figsize=(8, 6))
plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=clusters, cmap='viridis', marker='o', s=100, edgecolors='k')

centroids = kmeans.cluster_centers_
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='X', s=200, label='Centroids')

plt.title('Customer Segmentation (K-Means Clustering)')
plt.xlabel('Monthly Spending (Scaled)')
plt.ylabel('Monthly Visits (Scaled)')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()