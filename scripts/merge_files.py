import pandas as pd
import glob

# Find all CSV files starting with 'sales_'
files = glob.glob("../data/sales_*.csv")

# Read and merge files
df_list = [pd.read_csv(file) for file in files]
merged_df = pd.concat(df_list, ignore_index=True)

# Save merged file
merged_df.to_csv("../output/merged_sales.csv", index=False)

print("Files merged successfully.")
