import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import zscore

# Load the transaction history CSV file
df = pd.read_csv('./transaction_history.csv')

# Convert the 'Transaction Date' column to datetime format
df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])

# Define a function to identify unusual spending (Anomaly Detection using Z-score)
def flag_anomalous_spending(df, threshold=3):
    # Calculate the Z-score for 'Amount' to detect outliers
    df['Z-score'] = zscore(df['Amount'])
    # Flag transactions where the Z-score exceeds the threshold (outliers)
    df['Anomaly'] = df['Z-score'].apply(lambda x: 'Anomaly' if abs(x) > threshold else 'Normal')
    return df

# Apply anomaly detection to the dataset
df = flag_anomalous_spending(df)

# Show anomalous transactions (outliers)
anomalies = df[df['Anomaly'] == 'Anomaly']
print("\nAnomalous Transactions (Potential Risks):")
print(anomalies)

# Visualize the anomalies
plt.figure(figsize=(10, 6))
plt.scatter(df['Transaction Date'], df['Amount'], c=df['Anomaly'].apply(lambda x: 1 if x == 'Anomaly' else 0), cmap='coolwarm', label='Anomalies', alpha=0.7)
plt.title('Anomalous Spending Detection')
plt.xlabel('Transaction Date')
plt.ylabel('Amount')
plt.legend(loc='best')
plt.tight_layout()
plt.show()

# Detecting Behavioral Changes: Flagging late-night or unusual spending times
def flag_late_night_spending(df, start_hour=22, end_hour=6):
    # Identify transactions that happen between 10 PM and 6 AM
    df['Late-Night Spending'] = df['Transaction Date'].dt.hour.apply(lambda x: 'Late-Night' if x >= start_hour or x <= end_hour else 'Normal')
    return df

# Flag late-night spending
df = flag_late_night_spending(df)

# Show transactions flagged as late-night spending (Potential health/mental stress signal)
late_night_spending = df[df['Late-Night Spending'] == 'Late-Night']
print("\nLate-Night Spending (Potential Health or Mental Stress Indicator):")
print(late_night_spending)

# Visualize late-night spending
plt.figure(figsize=(10, 6))
plt.scatter(df['Transaction Date'], df['Amount'], c=df['Late-Night Spending'].apply(lambda x: 1 if x == 'Late-Night' else 0), cmap='coolwarm', label='Late-Night Spending', alpha=0.7)
plt.title('Late-Night Spending Detection (Potential Health/Mental Stress)')
plt.xlabel('Transaction Date')
plt.ylabel('Amount')
plt.legend(loc='best')
plt.tight_layout()
plt.show()

# Identifying Large Spending Increases (Potential Financial Risk)
def detect_spending_spikes(df, threshold=1.5):
    # Calculate the percentage change in spending between consecutive days
    df['Spending Change (%)'] = df['Amount'].pct_change() * 100
    # Flag significant spikes (above threshold)
    df['Spending Spike'] = df['Spending Change (%)'].apply(lambda x: 'Spike' if abs(x) > threshold else 'Normal')
    return df

# Detect spending spikes
df = detect_spending_spikes(df)

# Show transactions flagged as spending spikes (Potential financial risk)
spending_spikes = df[df['Spending Spike'] == 'Spike']
print("\nSpending Spikes (Potential Financial Risk):")
print(spending_spikes)

# Visualize spending spikes
plt.figure(figsize=(10, 6))
plt.scatter(df['Transaction Date'], df['Amount'], c=df['Spending Spike'].apply(lambda x: 1 if x == 'Spike' else 0), cmap='coolwarm', label='Spending Spike', alpha=0.7)
plt.title('Spending Spikes Detection (Potential Financial Risk)')
plt.xlabel('Transaction Date')
plt.ylabel('Amount')
plt.legend(loc='best')
plt.tight_layout()
plt.show()
