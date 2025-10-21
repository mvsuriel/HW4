# e. Generate dummies for ethnicity column (One hot encoding)
from .data_fill_nans import data_fill_nans
import pandas as pd


def data_encoding(file_name: str) -> tuple[pd.DataFrame, pd.DataFrame]:
    train, test = data_fill_nans(file_name)
    train = pd.get_dummies(train, columns=['ethnicity'], drop_first=True)
    test = pd.get_dummies(test, columns=['ethnicity'], drop_first=True)
    test = test.reindex(columns=train.columns, fill_value=0)
    print("One-hot encoding applied to 'ethnicity' column.")
    return train, test
