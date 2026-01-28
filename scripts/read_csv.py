import pandas as pd

df = pd.read_csv(
    r"C:\Users\ayesh\Documents\python_excel_automation\data\sample.csv"
)

print(df.head())

df.to_csv(
    r"C:\Users\ayesh\Documents\python_excel_automation\output\copied_sample.csv",
    index=False
)

print("File processed successfully.")
