import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import zscore

# Load the transaction history CSV file
df = pd.read_csv('./transaction_history.csv')

# Convert the 'Transaction Date' column to datetime format
df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])

# Flagging late-night spending: Potential indicators of insomnia or emotional distress
def flag_late_night_spending(df, start_hour=22, end_hour=6):
    # Identify transactions that happen between 10 PM and 6 AM
    df['Late-Night Spending'] = df['Transaction Date'].dt.hour.apply(lambda x: 'Late-Night' if x >= start_hour or x <= end_hour else 'Normal')
    return df

# Flagging impulsive spending: Transactions with unusual increases in amount
def flag_spending_spikes(df, threshold=1.5):
    # Calculate percentage change in spending between consecutive transactions
    df['Spending Change (%)'] = df['Amount'].pct_change() * 100
    # Flag significant spending spikes (above threshold)
    df['Spending Spike'] = df['Spending Change (%)'].apply(lambda x: 'Spike' if abs(x) > threshold else 'Normal')
    return df

# Flagging increased spending in certain categories: Impulsive or stress-driven behavior
def flag_increased_spending(df, threshold=50000, category='Entertainment'):
    # Filter transactions in the specified category and flag large amounts
    category_spending = df[df['Category'] == category]
    category_spending['Increased Spending'] = category_spending['Amount'].apply(lambda x: 'Increased' if x > threshold else 'Normal')
    return category_spending

# Flagging frequent small transactions: Sign of stress-driven purchases
def flag_frequent_small_transactions(df, max_amount=50000, min_transactions=10):
    # Count transactions below the max amount
    small_transactions = df[df['Amount'] < max_amount]
    transaction_count = small_transactions.groupby('Transaction Date').size()
    frequent_small_trans = transaction_count[transaction_count >= min_transactions]
    return frequent_small_trans

# Apply flags to the transaction data
df = flag_late_night_spending(df)
df = flag_spending_spikes(df)

# Analyzing late-night spending (Potential insomnia or emotional distress)
late_night_spending = df[df['Late-Night Spending'] == 'Late-Night']
print("\nLate-Night Spending (Potential Mental Health Indicator):")
print(late_night_spending)

# Visualize late-night spending
plt.figure(figsize=(10, 6))
plt.scatter(df['Transaction Date'], df['Amount'], c=df['Late-Night Spending'].apply(lambda x: 1 if x == 'Late-Night' else 0), cmap='coolwarm', label='Late-Night Spending', alpha=0.7)
plt.title('Late-Night Spending Detection (Potential Mental Health Indicator)')
plt.xlabel('Transaction Date')
plt.ylabel('Amount')
plt.legend(loc='best')
plt.tight_layout()
plt.show()

# Analyzing spending spikes (Potential impulsive behavior or financial distress)
spending_spikes = df[df['Spending Spike'] == 'Spike']
print("\nSpending Spikes (Potential Impulsive Behavior/Financial Distress):")
print(spending_spikes)

# Visualize spending spikes
plt.figure(figsize=(10, 6))
plt.scatter(df['Transaction Date'], df['Amount'], c=df['Spending Spike'].apply(lambda x: 1 if x == 'Spike' else 0), cmap='coolwarm', label='Spending Spike', alpha=0.7)
plt.title('Spending Spikes Detection (Potential Impulsive Behavior/Financial Distress)')
plt.xlabel('Transaction Date')
plt.ylabel('Amount')
plt.legend(loc='best')
plt.tight_layout()
plt.show()

# Analyzing increased spending in entertainment (Potential stress-driven purchases)
entertainment_spending = flag_increased_spending(df, threshold=50000, category='Entertainment')
print("\nIncreased Spending in Entertainment (Potential Stress/Emotional Spending):")
print(entertainment_spending)

# Analyzing frequent small transactions (Sign of stress-driven purchases)
frequent_small_transactions = flag_frequent_small_transactions(df)
print("\nFrequent Small Transactions (Potential Stress/Anxiety Driven):")
print(frequent_small_transactions)

# Combine all risk indicators into one DataFrame
mental_health_risks = pd.concat([late_night_spending, spending_spikes, entertainment_spending, frequent_small_transactions], axis=0)
mental_health_risks = mental_health_risks.drop_duplicates(subset=['Transaction Date', 'Amount'])

# Displaying all risk signals in one table
print("\nAll Potential Mental Health Risk Indicators:")
print(mental_health_risks)

# Generating the conclusion based on the flags
def generate_conclusion(late_night_spending, spending_spikes, entertainment_spending, frequent_small_transactions):
    conclusion = ""

    # Late-night spending check
    if len(late_night_spending) > 0:
        conclusion += "Late-night spending detected. This could be a sign of insomnia or emotional distress. Please investigate further.\n"
    
    # Spending spikes check
    if len(spending_spikes) > 0:
        conclusion += "Spending spikes detected. This could indicate impulsive spending or financial distress. Please assess the situation.\n"
    
    # Increased entertainment spending check
    if len(entertainment_spending) > 0:
        conclusion += "Increased spending on entertainment detected. This could be a sign of stress-driven spending or emotional coping. Consider assessing the individual’s emotional health.\n"
    
    # Frequent small transactions check
    if len(frequent_small_transactions) > 0:
        conclusion += "Frequent small transactions detected. This may be a sign of anxiety or stress-driven purchases. It may require further attention.\n"

    # If no issues detected
    if len(late_night_spending) == 0 and len(spending_spikes) == 0 and len(entertainment_spending) == 0 and len(frequent_small_transactions) == 0:
        conclusion += "No significant signs of mental health-related spending behavior detected. However, continued monitoring may be beneficial."

    return conclusion

# Get and print the conclusion
conclusion = generate_conclusion(late_night_spending, spending_spikes, entertainment_spending, frequent_small_transactions)
print("\nConclusion based on the analysis:")
print(conclusion)
