import os
from urllib.error import HTTPError
import pandas as pd


def load_data(config=None, path=None):
    if path is not None:
        return pd.read_parquet(path)
    
    if config is None:
        # Load data from the default path
        return pd.read_parquet('data.parquet')
    
    filename = config["path"]["filename"]
    data_raw = config["path"]["data_raw"]
    destiny_file = f"{data_raw}/{filename}"
    

    # Load data from the path specified in the config
    # Check if the data is already in the desired format
    if os.path.exists(destiny_file):
        return pd.read_parquet(destiny_file)
    else:
        # Load data from the source and save it in the desired format
        try:
            return (
                pd.read_csv(config['data']['source'], sep=';')
                    .to_parquet(destiny_file, **{"compression": "brotli"})
            )
        except HTTPError as e:
            print("Update the link")
            print(f"Error: {e}")
            return None