import pandas as pd
from pathlib import Path

# Get project root
project_root = Path(__file__).resolve().parent.parent

# Load cleaned dataset
csv_file = project_root / "dataset" / "cleaned_superstore.csv"

df = pd.read_csv(csv_file)

print("=" * 50)
print("DATASET INFORMATION")
print("=" * 50)

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nTotal Sales:")
print(round(df["Sales"].sum(), 2))

print("\nTotal Profit:")
print(round(df["Profit"].sum(), 2))

print("\nTotal Quantity Sold:")
print(df["Quantity"].sum())

print("\nSales by Region:")
print(
    df.groupby("Region")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

print("\nProfit by Region:")
print(
    df.groupby("Region")["Profit"]
      .sum()
      .sort_values(ascending=False)
)

print("\nSales by Category:")
print(
    df.groupby("Category")["Sales"]
      .sum()
      .sort_values(ascending=False)
)

print("\nProfit by Category:")
print(
    df.groupby("Category")["Profit"]
      .sum()
      .sort_values(ascending=False)
)

print("\nTop 10 Sub-Categories by Sales:")
print(
    df.groupby("Sub-Category")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print("\nTop 10 Sub-Categories by Profit:")
print(
    df.groupby("Sub-Category")["Profit"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)