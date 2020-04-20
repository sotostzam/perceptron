import pandas as pd

class naive_bayes():
    def __init__(self, dataset, target_class):
        self.dataset = dataset
        self.target_attribute = target_class
        self.classes = dataset[target_class].unique()

    def train(self):
        # Find target attributes probabilities
        class_propability = []
        for class_item in self.classes:
            class_propability.append((class_item, self.dataset[self.target_attribute].value_counts()[class_item] / self.dataset[self.target_attribute].count()))
        print(class_propability)

    def predict(self, attributes):
        pass

def main():
    dataset = pd.read_csv("toPlayOrNot.csv")
    
    nb = naive_bayes(dataset, 'play')
    nb.train()

if __name__ == "__main__":
    main()