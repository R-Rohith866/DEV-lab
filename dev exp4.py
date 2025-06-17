import pandas as pd

# Load your CSV file
df = pd.read_csv("C:/Users/ROHITH/Downloads/Temperature.csv")

# Correct date parsing assuming the format is dd-mm-yyyy
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

# Display DataFrame
print(df.head())

# Step 3: Extract month name
df['Month'] = df['Date'].dt.strftime('%B')  # E.g., January, February

# Step 4: Group by City and Month, sum the temperature
grouped = df.groupby(['City', 'Month'])['Temperature'].sum().reset_index()

# Step 5: Pivot for city-month table
pivot_table = grouped.pivot(index='City', columns='Month', values='Temperature').fillna(0)

# Step 6: Add total temperature column
pivot_table['Total_Temperature'] = pivot_table.sum(axis=1)

# Step 7: Find city with highest total temperature
max_temp_city = pivot_table['Total_Temperature'].idxmax()
max_temp_value = pivot_table['Total_Temperature'].max()

# Step 8: Print result
print("\nPivot Table (City vs Month-wise Temperature Sum):")
print(pivot_table)

print(f"\nCity with highest total temperature: {max_temp_city} ({max_temp_value}°C)")
