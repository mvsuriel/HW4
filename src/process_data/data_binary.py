# f. Create a binary variable for gender M/F
from .data_encoding import data_encoding
import pandas as pd

def data_binary(file_name: str) -> tuple[pd.DataFrame, pd.DataFrame]:
    train, test = data_encoding(file_name)
    train['gender_M'] = (train['gender'] == 'M').astype(int)
    train['gender_F'] = (train['gender'] == 'F').astype(int)
    test['gender_M'] = (test['gender'] == 'M').astype(int)
    test['gender_F'] = (test['gender'] == 'F').astype(int)
    print("Binary variables 'gender_M' and 'gender_F' created (1 = True, 0 = False).")
    return train, test
