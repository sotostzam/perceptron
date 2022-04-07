from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
import c_means

def main():
    features, true_labels = make_blobs(n_samples=200, centers=3, cluster_std=0.60, random_state=0)
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

    model = c_means.C_Means_Classifier()
    model.fit(scaled_features, clusters=3)

if __name__ == "__main__":
    main()
    