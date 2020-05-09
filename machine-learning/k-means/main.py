import k_means
import pandas as pd

def main():
    # Read the iris dataset
    dataset = pd.read_csv("iris.csv")
    dataset.drop(['species'], axis=1, inplace=True)
    k_means_cls = k_means.K_Means(k=3)
    k_means_cls.fit(dataset)

if __name__ == "__main__":
    main()