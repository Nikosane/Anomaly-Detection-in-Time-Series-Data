import numpy as np
from sklearn.ensemble import IsolationForest

def detect_anomalies(data):
    """
    Detect anomalies using Isolation Forest.
    :param data: pandas DataFrame
    :return: pandas DataFrame with anomaly labels
    """
    model = IsolationForest(contamination=0.05, random_state=42)
    data['anomaly'] = model.fit_predict(data[['value']])
    data['anomaly'] = data['anomaly'].apply(lambda x: 1 if x == -1 else 0)
    print("Anomaly detection completed.")
    return data
