"""Main module."""
import pandas as pd

def give_head(dataframe : pd.DataFrame):
    return dataframe.head()

if __name__ == "__main__":
    dataframe = pd.DataFrame({"Col1": [1.0, 2.0], "Col2": [3.0, 4.0]})
    print(give_head(dataframe= dataframe))