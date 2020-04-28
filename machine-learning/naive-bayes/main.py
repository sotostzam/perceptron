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
        self.class_propability = []
        total_counts = self.dataset[self.target_attribute].count()
        for class_item in self.classes:
            feature_counts = self.dataset[self.target_attribute].value_counts()[class_item]
            self.class_propability.append((class_item, feature_counts, feature_counts / total_counts))
        
        self.features_propability = {}
        for item in self.features:
            df = self.dataset[item]
            values = df.unique()
            feature_values = {}
            for value in values:
                indexes = self.dataset[self.dataset[item] == value].index.tolist()      # Get indexes of the feature value
                sub_matrix = self.dataset[self.target_attribute].iloc[indexes]          # Get target class values for this feature value
                sub_matrix_counts = sub_matrix.value_counts()
                value_classes = {}
                for f_item in range(0, sub_matrix_counts.shape[0]):
                    f_label = sub_matrix_counts.index[f_item]
                    f_probability = sub_matrix_counts[f_item] / total_counts
                    value_classes[f_label] = f_probability
                if not 'yes' in value_classes:
                    value_classes['yes'] = 0
                if not 'no' in value_classes:
                    value_classes['no'] = 0
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

        p_true = pyo * pyt * pyh * pyw
        p_false = pno * pnt * pnh * pnw

        # for attribute in self.features_propability:
        #     f_attributes = self.features_propability[attribute]
        #     for a_value in f_attributes:
        #         f_attributes_values = self.features_propability[attribute][a_value]
        #         if 'yes' in f_attributes_values:
        #             p_true *= f_attributes_values['yes']
        #         if 'no' in f_attributes_values:
        #             p_false *= f_attributes_values['no']
        
        p_true *= self.class_propability[1][2]
        p_false *= self.class_propability[0][2]

        #print(p_true + p_false)
        if p_true > p_false:
            print('yes')
        else:
            print('no')

def main():
    dataset = pd.read_csv("toPlayOrNot.csv")
    
    nb = NaiveBayes(dataset, 'play')
    nb.train()
    nb.predict('sunny', 'mild', 'high', False)

if __name__ == "__main__":
    main()