import matplotlib.pyplot as plt

def plot_anomalies(data):
    """
    Plot time series data with anomalies highlighted.
    :param data: pandas DataFrame
    """
    plt.figure(figsize=(12,6))
    plt.plot(data.index, data['value'], label='Time Series Data')
    anomalies = data[data['anomaly'] == 1]
    plt.scatter(anomalies.index, anomalies['value'], color='red', label='Anomalies')
    plt.legend()
    plt.title("Time Series Anomaly Detection")
    plt.show()
    print("Visualization completed.")
