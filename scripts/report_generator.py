import pandas as pd

# Load merged sales data
df = pd.read_csv("../output/merged_sales.csv")

# Create summary report
summary = df.groupby("product")["amount"].sum().reset_index()

# Save report to Excel
summary.to_excel("../output/sales_summary.xlsx", index=False)

print("Report generated successfully.")
