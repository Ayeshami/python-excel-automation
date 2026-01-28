import pandas as pd

# Load CSV file
df = pd.read_csv("../data/sample.csv")

# Remove empty rows
df = df.dropna(how="all")

# Remove duplicate rows
df = df.drop_duplicates()

# Save cleaned data to Excel
df.to_excel("../output/cleaned_data.xlsx", index=False)

print("Data cleaned and saved successfully.")
