import pandas as pd
import knn_classifier

def main():
    # Read the iris dataset
    dataset = pd.read_csv("iris.csv")
    knn_cls = knn_classifier.KNN_Classifier(k = 5)
    knn_cls.fit(dataset, train_percent = 0.2)
    print("Accuracy: " + str(knn_cls.accuracy()) + "%")
    knn_cls.predict([2.3,0.6,2.3,2.3])
    knn_cls.visualize()

if __name__ == "__main__":
    main()