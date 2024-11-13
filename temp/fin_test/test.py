import pandas as pd
import matplotlib.pyplot as plt

# Load the transaction history CSV file
df = pd.read_csv('./transaction_history.csv')

# Convert the 'Transaction Date' column to datetime format
df['Transaction Date'] = pd.to_datetime(df['Transaction Date'])

# Summary Statistics: Display the total amount spent by category
category_summary = df.groupby('Category')['Amount'].sum().sort_values(ascending=False)
print("Spending by Category:")
print(category_summary)

# Visualization: Plot the spending per category
plt.figure(figsize=(10, 6))
category_summary.plot(kind='bar')
plt.title('Total Spending by Category')
plt.xlabel('Category')
plt.ylabel('Total Amount Spent')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Trend Analysis: Spending trend over time
df['Month'] = df['Transaction Date'].dt.to_period('M')
monthly_spending = df.groupby('Month')['Amount'].sum()
print("\nMonthly Spending Trend:")
print(monthly_spending)

# Visualization: Plot the spending trend over time
plt.figure(figsize=(10, 6))
monthly_spending.plot(kind='line', marker='o')
plt.title('Monthly Spending Trend')
plt.xlabel('Month')
plt.ylabel('Total Amount Spent')
plt.grid(True)
plt.tight_layout()
plt.show()

# Identifying Abnormal Spending Patterns: Flagging days with unusually high spending
high_spending_threshold = df['Amount'].quantile(0.9)  # Top 10% spending
high_spending_days = df[df['Amount'] > high_spending_threshold]
print("\nHigh Spending Days (Top 10%):")
print(high_spending_days)

# Analysis of spending by time of day (hourly breakdown)
df['Hour'] = df['Transaction Date'].dt.hour
hourly_spending = df.groupby('Hour')['Amount'].sum()
print("\nSpending by Hour of the Day:")
print(hourly_spending)

# Visualization: Plot spending by hour
plt.figure(figsize=(10, 6))
hourly_spending.plot(kind='line', marker='o')
plt.title('Spending by Hour of the Day')
plt.xlabel('Hour of Day')
plt.ylabel('Total Amount Spent')
plt.xticks(range(24))
plt.grid(True)
plt.tight_layout()
plt.show()

# Analyzing the total amount spent per day of the week
df['Weekday'] = df['Transaction Date'].dt.day_name()
weekday_spending = df.groupby('Weekday')['Amount'].sum().reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])
print("\nSpending by Weekday:")
print(weekday_spending)

# Visualization: Plot spending by weekday
plt.figure(figsize=(10, 6))
weekday_spending.plot(kind='bar')
plt.title('Total Spending by Weekday')
plt.xlabel('Weekday')
plt.ylabel('Total Amount Spent')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
