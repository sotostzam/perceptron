# K-Means Clustering

## Information

The objective is to partition (subdivide) a finite data set X to construct a Voronoi tesselation of K regions (clusters). To determine in which cluster each observation should be contained, centroids are used that indicate the mean of all existing features in this cluster. It is widely used in cluster analysis and data mining.

![k-means](/images/k-means.png)

## Estimating number of clusters

How do we to estimate the good number of clusters? We compute the variance for every number of clusters k (10% of samples in general). Ultimatelly, the best value for k, denoted by k∗, lies in the elbow region.

Another way of choosing the best k for the number of clusters is using a technique called Silhouette Width. Silhouette refers to a method of interpretation and validation of consistency within clusters of
data.

![k-means](/images/k-means-selection.png)

## Distance measurement

Distance is measured using the Euclidean distance. This is the straight-line distance between two points.
