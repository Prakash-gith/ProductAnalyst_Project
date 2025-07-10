import pandas as pd

print("Script started!")

# Load dataset, force user_id as string to preserve all formatting
df = pd.read_csv("mobile_app_interactions_expanded.csv", dtype={'user_id': str})
print(f"Loaded dataset with {len(df)} total rows.")

# Convert timestamps
df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
df.dropna(subset=['timestamp'], inplace=True)
print("Timestamps converted and cleaned!")

# Convert user_id to string explicitly, even if it looks like a number
df['user_id'] = df['user_id'].astype(str).str.strip()

# Replace placeholder strings for missing user IDs (e.g., 'nan' or 'NaN') with actual NaN
df['user_id'] = df['user_id'].replace(['nan', 'NaN'], pd.NA)

# Replace empty strings with NaN
df.loc[df['user_id'] == '', 'user_id'] = pd.NA

# Drop rows where user_id is missing or invalid
before = len(df)
df = df.dropna(subset=['user_id'])
after = len(df)
print(f"Dropped {before - after} rows with missing or invalid user IDs.")

# Remove rows with unreasonable timestamps
df = df[(df['timestamp'].dt.year >= 2020) & (df['timestamp'].dt.year <= 2026)]
print("Removed rows with timestamps outside 2020-2026 range.")

# Sort by user_id and timestamp
df.sort_values(by=['user_id', 'timestamp'], inplace=True)
print("Data sorted by user_id and timestamp!")

# Confirm cleaned data
print("Cleaned data sample:")
print(df.head())

# Export cleaned dataset
df.to_csv("cleaned_mobile_app_data.csv", index=False)
print(f"Cleaned data exported to cleaned_mobile_app_data.csv with {len(df)} rows.")
