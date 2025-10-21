# d. Fill NaN with the mean value of the column in the columns: height, weight
from .data_remove_nans import data_remove_nans
import pandas as pd

def data_fill_nans(file_name: str) -> tuple[pd.DataFrame, pd.DataFrame]:
    train, test = data_remove_nans(file_name)
    for col in ['height', 'weight']:
        train[col] = train[col].fillna(train[col].mean())
        test[col] = test[col].fillna(test[col].mean())
    print("Filled NaN values in ['height', 'weight'] with column means.")
    return train, test
