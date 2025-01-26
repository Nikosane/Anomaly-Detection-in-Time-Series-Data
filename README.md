# TimeGuard -An Anomaly-Detection-in-Time-Series-Data

## Project Overview
TimeGuard is a lightweight anomaly detection system for time series data. It utilizes statistical and machine learning-based approaches to identify unusual patterns, trends, and outliers in sequential data, making it ideal for applications such as financial analysis, IoT monitoring, and operational data tracking.


## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/nikosane/Anomaly-Detection-in-Time-Series-Data.git
   cd Anomaly-Detection-in-Time-Series-Data
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. **Prepare your data:**
   - Place raw time series data in the `data/` folder.
2. **Run anomaly detection:**
   ```bash
   python scripts/run_detection.py
   ```
3. **View results:**
   - Anomalies will be saved in `results/anomalies_detected.csv`.
   - Visualization plots will be saved in `results/plots/`.

## Features
- **Data Preprocessing:**
  - Handling missing values.
  - Data normalization and scaling.
  
- **Anomaly Detection Methods:**
  - Z-score method.
  - Moving average and Bollinger bands.
  - Isolation Forest.
  - One-Class SVM.
  - Seasonal-Trend Decomposition.
  
- **Evaluation Metrics:**
  - Precision, Recall, F1-score.
  - RMSE for forecasting models.
  
- **Visualization:**
  - Time series anomaly plots.
  - Decomposed trend analysis.

## Dependencies
- Python 3.x
- NumPy
- Pandas
- SciPy
- Scikit-learn
- Matplotlib
- Statsmodels

## Contributing
Contributions are welcome! Feel free to fork this repository and submit pull requests.

## License
This project is licensed under the MIT License. See `LICENSE` for more details.

## Contact
For any questions or suggestions, please reach out to:
- Email: niteshkotian3@gmail.com

