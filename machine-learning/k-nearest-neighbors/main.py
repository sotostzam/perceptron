import pandas as pd
import knn_classifier

def main():
    # Read the iris dataset
    dataset = pd.read_csv("iris.csv")
    knn_cls = knn_classifier.KNN_Classifier(k = 5)
    knn_cls.fit(dataset, train_percent = 0.2)
    print("Confidence: " + str(knn_cls.accuracy()) + "%")
    print("Prediction: " + str(knn_cls.predict([0,0,0,0])))
    knn_cls.visualize()

if __name__ == "__main__":
    main()