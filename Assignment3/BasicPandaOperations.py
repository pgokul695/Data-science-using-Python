import pandas as pd

# Load the dataset
df = pd.read_csv(https://corgis-edu.github.io/corgis/datasets/csv/weather/weather.csv)

# Inspect the data
print(df.info())
print(df.describe())
print(df.head())
print(df.columns)

# Rename columns
df.rename(columns={
    'temperature': 'Temp',
    'humidity': 'Humidity',
    'wind_speed': 'Wind_Speed',
    'precipitation': 'Precipitation'
}, inplace=True)

# Filter rows where temperature is greater than 30
filtered_df = df[df['Temp'] > 30]
print(filtered_df.head())

# Sort by temperature in descending order
sorted_df = df.sort_values(by='Temp', ascending=False)
print(sorted_df.head())

# Group by month and calculate average temperature
if 'month' in df.columns:
    grouped_df = df.groupby('month')['Temp'].mean().reset_index()
    print(grouped_df)

# Check and handle missing values
print(df.isnull().sum())
df_cleaned = df.dropna()
df_filled = df.fillna(df.mean())
print(df_cleaned.head())
print(df_filled.head())

# Add a new column 'Temp_Category'
df['Temp_Category'] = pd.cut(df['Temp'], bins=[-float('inf'), 0, 20, 30, float('inf')], 
                             labels=['Freezing', 'Cold', 'Warm', 'Hot'])
print(df.head())
