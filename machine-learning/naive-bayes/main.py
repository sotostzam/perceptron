import pandas as pd

class NaiveBayes:
    def __init__(self, dataset, target_class):
        self.dataset = dataset
        self.target_attribute = target_class
        self.features = dataset.columns.tolist()
        self.features.remove(self.target_attribute)
        self.classes = dataset[target_class].unique()

    def train(self):
        # Find class attribute probabilities
        self.class_propability = {}
        total_counts = self.dataset[self.target_attribute].count()
        for class_item in self.classes:
            feature_counts = self.dataset[self.target_attribute].value_counts()[class_item]
            self.class_propability[class_item] = (feature_counts, feature_counts / total_counts)
        
        self.features_propability = {}
        for item in self.features:
            df = self.dataset[item]
            values = df.unique()
            feature_values = {}
            for value in values:
                indexes = self.dataset[self.dataset[item] == value].index.tolist()      # Get indexes of the feature value
                sub_matrix = self.dataset[self.target_attribute].iloc[indexes]          # Get target class values for this feature value
                sub_matrix_counts = sub_matrix.value_counts()
                value_classes = {'yes': 0, 'no': 0}
                for f_item in range(0, sub_matrix_counts.shape[0]):
                    f_label = sub_matrix_counts.index[f_item]
                    if f_label == 'yes':
                        value_classes['yes'] += sub_matrix_counts[f_item] / self.class_propability['yes'][0]
                    else:
                        value_classes['no'] += sub_matrix_counts[f_item] / self.class_propability['no'][0]
                feature_values[value] = value_classes
            self.features_propability[item] = feature_values

    def predict(self, outlook, temperature, humidity, windy):
        pyo = self.features_propability['outlook'][outlook]['yes']
        pyt = self.features_propability['temperature'][temperature]['yes']
        pyh = self.features_propability['humidity'][humidity]['yes']
        pyw = self.features_propability['windy'][windy]['yes']

        pno = self.features_propability['outlook'][outlook]['no']
        pnt = self.features_propability['temperature'][temperature]['no']
        pnh = self.features_propability['humidity'][humidity]['no']
        pnw = self.features_propability['windy'][windy]['no']

        p_true = pyo * pyt * pyh * pyw * self.class_propability['yes'][1]
        p_false = pno * pnt * pnh * pnw * self.class_propability['no'][1]

        # Since p(c1) + p(c2) = 1
        true_class = p_true / (p_true + p_false)
        false_class = p_false / (p_true + p_false)

        if true_class > false_class:
            print('Prediction: yes\nScore: ' + str(true_class))
        else:
            print('Prediction: no\nScore: ' + str(false_class))

def main():
    dataset = pd.read_csv("toPlayOrNot.csv")
    
    nb = NaiveBayes(dataset, 'play')
    nb.train()
    nb.predict('rainy', 'mild', 'high', True)

if __name__ == "__main__":
    main()