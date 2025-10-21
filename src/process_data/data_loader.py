# a. Load the data
import pandas as pd

def data_loader(file_name: str) -> pd.DataFrame:
    data = pd.read_csv(file_name)
    print(f"Data loaded successfully. Shape: {data.shape}")
    return data
