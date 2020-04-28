import pandas as pd

class NaiveBayes():
    def __init__(self, dataset, target_class):
        self.dataset = dataset
        self.target_attribute = target_class
        self.features = dataset.columns.tolist()
        self.features.remove(self.target_attribute)
        self.classes = dataset[target_class].unique()

    def train(self):
        # Find class attribute probabilities
        class_propability = []
        total_counts = self.dataset[self.target_attribute].count()
        for class_item in self.classes:
            feature_counts = self.dataset[self.target_attribute].value_counts()[class_item]
            class_propability.append((class_item, feature_counts, feature_counts / total_counts))
        print(class_propability)
        
        features_propability = []
        for item in self.features:
            # Extract propabilities of every feature
            # print(self.dataset[item].value_counts())
            pass

    def predict(self, attributes):
        pass

def main():
    dataset = pd.read_csv("toPlayOrNot.csv")
    
    nb = NaiveBayes(dataset, 'play')
    nb.train()

if __name__ == "__main__":
    main()