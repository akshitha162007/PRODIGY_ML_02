import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
data = pd.read_csv("Mall_Customers.csv")
print("First 5 rows of dataset:")
print(data.head())
X = data[['Annual Income (k$)', 'Spending Score (1-100)']]
kmeans = KMeans(n_clusters=5, random_state=42)
data['Cluster'] = kmeans.fit_predict(X)
print("\nCluster distribution:")
print(data['Cluster'].value_counts())
plt.figure(figsize=(8,6))
plt.scatter(
    X.iloc[:, 0],
    X.iloc[:, 1],
    c=data['Cluster'],
    cmap='viridis'
)
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.title("Customer Segmentation using K-Means")
plt.show()
