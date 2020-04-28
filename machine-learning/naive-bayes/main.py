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
        #print(class_propability)
        
        self.features_propability = []
        for item in self.features:
            df = self.dataset[item]
            values = df.unique()
            feature_values = []
            for value in values:
                indexes = self.dataset[self.dataset[item] == value].index.tolist()      # Get indexes of the feature value
                sub_matrix = self.dataset[self.target_attribute].iloc[indexes]          # Get target class values for this feature value
                sub_matrix_counts = sub_matrix.value_counts()
                value_classes = []
                for f_item in range(0, sub_matrix_counts.shape[0]):
                    f_label = sub_matrix_counts.index[f_item]
                    f_probability = sub_matrix_counts[f_item] / total_counts
                    value_classes.append((f_label, sub_matrix_counts[f_item], f_probability))
                feature_values.append((value, value_classes))
            self.features_propability.append((item, feature_values))

    def predict(self, attributes):
        pass

def main():
    dataset = pd.read_csv("toPlayOrNot.csv")
    
    nb = NaiveBayes(dataset, 'play')
    nb.train()

if __name__ == "__main__":
    main()