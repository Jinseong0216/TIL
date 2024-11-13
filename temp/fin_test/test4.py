import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load the transaction data
df = pd.read_csv('./transaction_history.csv')

# Convert 'Transaction Date' to datetime format
df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])

# 1. **Transaction Frequency & Time of Day Analysis**:

# Flag late-night transactions (late-night spending can be linked to insomnia or emotional distress)
def flag_late_night_spending(df, start_hour=22, end_hour=6):
    df['Late-Night Spending'] = df['Transaction Date'].dt.hour.apply(lambda x: 'Late-Night' if x >= start_hour or x <= end_hour else 'Normal')
    return df

# Apply late-night flag
df = flag_late_night_spending(df)

# 2. **Spending Behavior Analysis**:

# Detect large spikes in spending: Spending greater than 1.5 times the previous transaction
def flag_spending_spikes(df, threshold=1.5):
    df['Spending Change (%)'] = df['Amount'].pct_change() * 100  # Percentage change
    df['Spending Spike'] = df['Spending Change (%)'].apply(lambda x: 'Spike' if abs(x) > threshold else 'Normal')
    return df

# Apply spending spike detection
df = flag_spending_spikes(df)

# 3. **Category-Specific Spending**:

# Flag high spending in certain categories (e.g., entertainment, dining)
def flag_category_spending(df, category='Entertainment', threshold=50000):
    category_spending = df[df['Category'] == category]
    category_spending['High Spending'] = category_spending['Amount'].apply(lambda x: 'High' if x > threshold else 'Normal')
    return category_spending

# Apply category spending analysis (e.g., Entertainment)
df_entertainment = flag_category_spending(df, category='Entertainment')

# 4. **Long-Term Spending Trends**:

# Detecting trends in spending over time (moving average to capture long-term changes)
def detect_spending_trends(df, window=30):
    df['Amount Rolling Mean'] = df['Amount'].rolling(window=window).mean()
    df['Amount Trend'] = df['Amount'].diff()  # Trend (difference between consecutive days)
    return df

# Apply trend detection (e.g., over 30 days)
df = detect_spending_trends(df)

# 5. **Statistical Modeling**:

# Apply KMeans clustering to detect unusual spending patterns (anomaly detection)
def detect_anomalous_spending(df):
    # Using MinMaxScaler to normalize the data for clustering
    scaler = MinMaxScaler()
    df['Normalized Amount'] = scaler.fit_transform(df[['Amount']])
    
    # Using KMeans to cluster the data points into two clusters: normal and anomalous
    kmeans = KMeans(n_clusters=2, random_state=0)
    df['Cluster'] = kmeans.fit_predict(df[['Normalized Amount']])
    
    # The anomalous spending will likely fall into the cluster with higher average amounts
    return df

# Apply anomaly detection
df = detect_anomalous_spending(df)

# 6. **Risk Analysis & Financial Product Recommendation**:

def analyze_risks_and_recommend(df):
    risk_score = 0
    products = []

    # **Late-Night Spending**: Stress-related or poor mental health
    late_night_spending = df[df['Late-Night Spending'] == 'Late-Night']
    if len(late_night_spending) > 0:
        risk_score += 1
        products.append('Mental Health Support Plan')

    # **Spending Spikes**: Impulsive spending behavior
    spending_spikes = df[df['Spending Spike'] == 'Spike']
    if len(spending_spikes) > 0:
        risk_score += 2
        products.append('Debt Consolidation Loan')

    # **High Entertainment Spending**: Stress-driven or emotional spending
    high_entertainment_spending = df_entertainment[df_entertainment['High Spending'] == 'High']
    if len(high_entertainment_spending) > 0:
        risk_score += 1
        products.append('Emergency Savings Account')

    # **Spending Trends**: Decreasing savings, increasing debt
    decreasing_savings = df[df['Amount Trend'] < 0]
    if len(decreasing_savings) > 0:
        risk_score += 2
        products.append('Personal Financial Advisor')

    # **Anomalous Spending**: Detecting abnormal spending patterns (potential emotional spending)
    anomalous_spending = df[df['Cluster'] == 1]  # Assuming cluster 1 is anomalous
    if len(anomalous_spending) > 0:
        risk_score += 3
        products.append('Spending Tracker App')

    # Provide risk assessment based on score
    if risk_score <= 3:
        conclusion = 'Low risk, you are in good financial health.'
    elif risk_score <= 6:
        conclusion = 'Medium risk, consider improving your financial habits.'
    else:
        conclusion = 'High risk, take immediate action to address financial stress or impulsivity.'

    return products, conclusion

# Get risk analysis and financial product recommendations
recommended_products, risk_assessment = analyze_risks_and_recommend(df)

# Display results
print("\nRecommended Financial Products:")
for product in recommended_products:
    print(f"- {product}")

print("\nRisk Assessment Conclusion:")
print(risk_assessment)
