import pandas as pd

def main():
    dataset = pd.read_csv("toPlayOrNot.csv")
    
    # Target attribute is play
    class_yes = dataset['play'].value_counts()['yes'] / dataset['play'].count()
    class_no = dataset['play'].value_counts()['no'] / dataset['play'].count()

if __name__ == "__main__":
    main()