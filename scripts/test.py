import pandas as pd
file_path = 'SBIN-Jan.csv'
df = pd.read_csv(file_path)

# Display first few rows to understand structure
df.head()
# Ensure DATE is in datetime format and sort data chronologically
df['DATE'] = pd.to_datetime(df['DATE'], format='%Y-%m-%d')
df = df.sort_values(by='DATE')

# Calculate True Range (TR)
df['Previous Close'] = df['CLOSE'].shift(1)
df['TR'] = df[['HIGH', 'Previous Close']].max(axis=1) - df[['LOW', 'Previous Close']].min(axis=1)

# Calculate Average True Range (ATR) - 14-day period
df['ATR_14'] = df['TR'].rolling(window=14).mean()

# Identify top 10 True Range values
top_10_ranges = df[['DATE', 'TR']].sort_values(by='TR', ascending=False).head(10)

# Identify trend based on CLOSE price
df['Trend'] = df['CLOSE'].diff().apply(lambda x: 'Up' if x > 0 else ('Down' if x < 0 else 'Neutral'))

top_10_with_trend = df.loc[top_10_ranges.index, ['DATE', 'TR', 'Trend']]

# Show results
average_true_range = df['ATR_14'].iloc[-1]
average_true_range, top_10_with_trend
print(average_true_range, top_10_with_trend)
