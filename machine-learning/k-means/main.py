import k_means
import pandas as pd

def main():
    # Read the iris dataset
    dataset = pd.read_csv("iris.csv")
    dataset.drop(['species'], axis=1, inplace=True)
    k_means_clf = k_means.K_Means(k=3)      # Maximum k for this implementation is 8
    k_means_clf.fit(dataset)
    k_means_clf.predict([[5.5, 3.1, 1.2, 0.3],
                         [6.1, 2.5, 4.1, 1.7]])

if __name__ == "__main__":
    main()