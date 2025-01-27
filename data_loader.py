import pandas as pd

def load_data(file_path):
    """
    Load time series data from a CSV file.
    :param file_path: str, path to the CSV file.
    :return: pandas DataFrame
    """
    try:
        data = pd.read_csv(file_path, parse_dates=['timestamp'], index_col='timestamp')
        print("Data loaded successfully.")
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def preprocess_data(data):
    """
    Preprocess time series data.
    - Handle missing values
    - Normalize data
    :param data: pandas DataFrame
    :return: pandas DataFrame
    """
    # Fill missing values with forward fill
    data.fillna(method='ffill', inplace=True)
    # Normalize data
    data = (data - data.mean()) / data.std()
    print("Data preprocessing completed.")
    return data
