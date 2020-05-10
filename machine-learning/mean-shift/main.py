import mean_shift
import pandas as pd

def main():
    # Read the iris dataset
    dataset = pd.read_csv("iris.csv")
    dataset.drop(['species'], axis=1, inplace=True)
    mean_shift_clf = mean_shift.Mean_Shift()
    mean_shift_clf.fit(dataset)

if __name__ == "__main__":
    main()