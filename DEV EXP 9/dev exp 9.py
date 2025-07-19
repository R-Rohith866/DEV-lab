import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'Date': pd.date_range(start='2023-01-01', periods=365, freq='D'),
    'City': np.random.choice(['Delhi', 'Mumbai', 'Chennai', 'Kolkata', 'Bangalore'], 365),
    'State': np.random.choice(['Delhi', 'Maharashtra', 'Tamil Nadu', 'West Bengal', 'Karnataka'], 365),
    'Country': 'India',
    'MaxTemp': np.random.normal(35, 5, 365),
    'MinTemp': np.random.normal(22, 4, 365)
}
df = pd.DataFrame(data)
print(df.head())
print(df.info())
print(df.describe())
df['AvgTemp'] = (df['MaxTemp'] + df['MinTemp']) / 2
df['Date'] = pd.to_datetime(df['Date'])
df = df.dropna()
df = df.drop_duplicates()
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day

plt.figure(figsize=(10, 5))
sns.histplot(df['AvgTemp'], kde=True, color='tomato')
plt.title("Distribution of Average Temperature")
plt.xlabel("Average Temperature (°C)")
plt.show()

monthly_avg = df.groupby('Month')['AvgTemp'].mean().reset_index()
sns.lineplot(x='Month', y='AvgTemp', data=monthly_avg)
plt.title("Average Monthly Temperature Trend")
plt.xticks(range(1, 13))
plt.show()

top_cities = df['City'].value_counts().head(5).index
filtered_df = df[df['City'].isin(top_cities)]
sns.lineplot(x='Month', y='AvgTemp', hue='City', data=filtered_df)
plt.title("Monthly Avg Temperature in Top Cities")
plt.show()

delhi_df = df[df['State'] == 'Delhi']
yearly_trend = delhi_df.groupby('Year')['AvgTemp'].mean().reset_index()
sns.lineplot(x='Year', y='AvgTemp', data=yearly_trend)
plt.title("Average Yearly Temperature in Delhi")
plt.show()

sns.heatmap(df[['MaxTemp', 'MinTemp', 'AvgTemp']].corr(), annot=True)
plt.title("Temperature Variable Correlation")
plt.show()
