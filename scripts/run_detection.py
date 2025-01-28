import os
from src.data_loader import load_data, preprocess_data
from src.feature_engineering import extract_features
from src.anomaly_detection import detect_anomalies
from src.visualization import plot_anomalies

# Define file paths
data_file = "data/raw_data.csv"
processed_file = "data/processed_data.csv"
results_file = "results/anomalies_detected.csv"

# Step 1: Load Data
data = load_data(data_file)
if data is None:
    exit("Failed to load data. Exiting...")

# Step 2: Preprocess Data
processed_data = preprocess_data(data)
processed_data.to_csv(processed_file)

# Step 3: Feature Engineering
feature_data = extract_features(processed_data)

# Step 4: Anomaly Detection
anomaly_data = detect_anomalies(feature_data)
anomaly_data.to_csv(results_file, index=True)
print(f"Anomalies saved to {results_file}")

# Step 5: Visualization
plot_anomalies(anomaly_data)
