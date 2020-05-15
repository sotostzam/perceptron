# Mean-Shift Algorithm

## Information

Mean shift is a clustering algorithm, which is based on the hierarchical clustering methodology. This means that the mean shift algorithm figures out how many clusters are needed to partition a dataset, as well as where these clusters should be.

![mean-shift](/images/mean-shift.gif)

## Radius and bandwidth

Unlike the k-means algorithm, mean shift makes use of two variables. The first one, radius, defines the maximum distance from the centroid. This creates a perfect circle around the centroid. This whole circle is defined as the bandwidth of the centroid.

## Distance measurement

Distance is measured using the Euclidean distance. This is the straight-line distance between two points.
