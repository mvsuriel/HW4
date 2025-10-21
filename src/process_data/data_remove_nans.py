# c. Remove rows that contain NaN values in the columns: age, gender, ethnicity
from .data_loader import data_loader
from .data_split import data_split
import pandas as pd

def data_remove_nans(file_name: str) -> tuple[pd.DataFrame, pd.DataFrame]:
    data = data_loader(file_name)
    train, test = data_split(data)
    train = train.dropna(subset=['age', 'gender', 'ethnicity'])
    test = test.dropna(subset=['age', 'gender', 'ethnicity'])
    print("Removed NaN rows from train and test for columns: ['age', 'gender', 'ethnicity']")
    return train, test
