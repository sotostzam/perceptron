from sklearn.datasets import make_circles
from sklearn.datasets import make_moons
from sklearn.preprocessing import StandardScaler
import kernel_k_means

features, true_labels = make_circles(n_samples=200, factor=0.3, noise=0.05, random_state=0)
#features, true_labels = make_moons(n_samples=200, shuffle=True, noise=0.05, random_state=0)
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

model = kernel_k_means.K_Means_Classifier()

model.fit(scaled_features, num_clusters=2)
