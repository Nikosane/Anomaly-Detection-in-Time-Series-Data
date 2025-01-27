import pandas as pd

def extract_features(data):
    """
    Extract useful features from time series data.
    :param data: pandas DataFrame
    :return: pandas DataFrame with new features
    """
    data['rolling_mean'] = data['value'].rolling(window=5).mean()
    data['rolling_std'] = data['value'].rolling(window=5).std()
    data['lag_1'] = data['value'].shift(1)
    print("Feature extraction completed.")
    return data.dropna()
