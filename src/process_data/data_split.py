# b. Split the data between train and test
from sklearn.model_selection import train_test_split
import pandas as pd

def data_split(data: pd.DataFrame, test_size: float = 0.2, random_state: int = 42) -> tuple[pd.DataFrame, pd.DataFrame]:
    train, test = train_test_split(data, test_size=test_size, random_state=random_state)
    print(f"Split complete: {len(train)} training rows, {len(test)} testing rows.")
    return train, test
