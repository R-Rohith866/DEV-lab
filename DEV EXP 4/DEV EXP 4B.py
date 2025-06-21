import pandas as pd

df = pd.read_csv("C:/Users/ROHITH/Downloads/Temperature.csv")
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
df['Month'] = df['Date'].dt.strftime('%B')
grouped = df.groupby(['City', 'Month'])['Temperature'].sum().reset_index()
pivot_table = grouped.pivot(index='City', columns='Month', values='Temperature').fillna(0)
pivot_table['Total_Temperature'] = pivot_table.sum(axis=1)
max_temp_city = pivot_table['Total_Temperature'].idxmax()
max_temp_value = pivot_table['Total_Temperature'].max()

print("\nPivot Table (City vs Month-wise Temperature Sum):")
print(pivot_table)
print(f"\nCity with highest total temperature: {max_temp_city} ({max_temp_value}°C)")
