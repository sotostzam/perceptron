# K-Means Clustering

## Information

The k-means clustering algorithm is aims to partition a dataset (a set of features) into k amount of clusters, in which every feature belongs to one cluster. To determine in which cluster each observation should be contained, special centroids are used that indicate the mean of all existing features in this cluster. It is widely used in cluster analysis and data mining.

![k-means](/images/k-means.gif)

## Quality of cluster

In order to determine the quality of each cluster, this implementation uses the residual sum of squares function (also known as sum of squared error). It is a measure of the dispersion of the model. A small rss value indicates a tight fit of the model to the dataset.

## Distance measurement

Distance is measured using the Euclidean distance. This is the straight-line distance between two points.
