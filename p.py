import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV file
df = pd.read_csv('nhpc_cash_flow.csv')

# Create a figure and two subplots
fig, ax1 = plt.subplots(figsize=(10, 6))

# Create a bar chart for Operating Activity and Financing Activity on ax1
ax1.bar(df['Year'], df['Operating Activity'], label='Operating Activity', color='b', alpha=0.7)
ax1.bar(df['Year'], df['Financing Activity'], label='Financing Activity', color='r', alpha=0.7, bottom=df['Operating Activity'])

# Set labels for ax1
ax1.set_xlabel('Year')
ax1.set_ylabel('Cash Flow (in Crore)')
ax1.set_title('Cash Flow Analysis for NHPC Ltd')
ax1.legend(loc='upper left')

# Create a second y-axis for the line chart (Investing Activity)
ax2 = ax1.twinx()
ax2.plot(df['Year'], df['Investing Activity'], label='Investing Activity', color='g', marker='o')

# Set labels for ax2
ax2.set_ylabel('Cash Flow (in Crore)')
ax2.legend(loc='upper right')

# Display the chart
plt.grid(True)
plt.tight_layout()
plt.show()
