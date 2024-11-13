import pandas as pd
import numpy as np

# Load the transaction history CSV file
df = pd.read_csv('./transaction_history.csv')

# Convert the 'Transaction Date' column to datetime format
df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])

# Flagging late-night spending: Potential indicators of insomnia or emotional distress
def flag_late_night_spending(df, start_hour=22, end_hour=6):
    df['Late-Night Spending'] = df['Transaction Date'].dt.hour.apply(lambda x: 'Late-Night' if x >= start_hour or x <= end_hour else 'Normal')
    return df

# Flagging impulsive spending: Transactions with unusual increases in amount
def flag_spending_spikes(df, threshold=1.5):
    df['Spending Change (%)'] = df['Amount'].pct_change() * 100
    df['Spending Spike'] = df['Spending Change (%)'].apply(lambda x: 'Spike' if abs(x) > threshold else 'Normal')
    return df

# Flagging increased spending in certain categories: Impulsive or stress-driven behavior
def flag_increased_spending(df, threshold=50000, category='Entertainment'):
    category_spending = df[df['Category'] == category]
    category_spending['Increased Spending'] = category_spending['Amount'].apply(lambda x: 'Increased' if x > threshold else 'Normal')
    return category_spending

# Flagging frequent small transactions: Sign of stress-driven purchases
def flag_frequent_small_transactions(df, max_amount=50000, min_transactions=10):
    small_transactions = df[df['Amount'] < max_amount]
    transaction_count = small_transactions.groupby('Transaction Date').size()
    frequent_small_trans = transaction_count[transaction_count >= min_transactions]
    return frequent_small_trans

# Apply flags to the transaction data
df = flag_late_night_spending(df)
df = flag_spending_spikes(df)

# Analyze risks and flag products
def recommend_financial_products(df):
    products = []

    # Late-night spending recommendation (potential insomnia or emotional distress)
    late_night_spending = df[df['Late-Night Spending'] == 'Late-Night']
    if len(late_night_spending) > 0:
        products.append('Mental Health Support Plan')
        products.append('Budgeting App Subscription')

    # Spending spikes recommendation (potential impulsive behavior or financial distress)
    spending_spikes = df[df['Spending Spike'] == 'Spike']
    if len(spending_spikes) > 0:
        products.append('Debt Consolidation Loan')
        products.append('Personal Financial Advisor')

    # Increased spending in entertainment recommendation (potential stress-driven purchases)
    entertainment_spending = flag_increased_spending(df, threshold=50000, category='Entertainment')
    if len(entertainment_spending) > 0:
        products.append('Emergency Savings Account')
        products.append('Spending Tracker App')

    # Frequent small transactions recommendation (potential stress/anxiety-driven purchases)
    frequent_small_transactions = flag_frequent_small_transactions(df)
    if len(frequent_small_transactions) > 0:
        products.append('Emergency Savings Account')
        products.append('Financial Coaching')

    # If no issues detected, recommend general financial products
    if not (len(late_night_spending) > 0 or len(spending_spikes) > 0 or len(entertainment_spending) > 0 or len(frequent_small_transactions) > 0):
        products.append('Standard Savings Account')
        products.append('Retirement Plan')

    return list(set(products))  # Remove duplicates

# Get the financial product recommendations
recommended_products = recommend_financial_products(df)

# Display the recommended financial products
print("\nRecommended Financial Products based on the Analysis:")
for product in recommended_products:
    print(f"- {product}")
