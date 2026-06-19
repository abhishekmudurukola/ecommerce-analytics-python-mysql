import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Project path
project_root = Path(__file__).resolve().parent.parent

# Load data
df = pd.read_csv(project_root / "dataset" / "cleaned_superstore.csv")

# Sales by Region
region_sales = df.groupby("Region")["Sales"].sum()

plt.figure(figsize=(8,5))
region_sales.plot(kind="bar")
plt.title("Sales by Region")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

# ------------------------
# Chart 2 : Profit by Category
# ------------------------

category_profit = df.groupby("Category")["Profit"].sum()

plt.figure(figsize=(8,5))

category_profit.plot(kind="bar")

plt.title("Profit by Category")

plt.xlabel("Category")

plt.ylabel("Profit")

plt.tight_layout()

plt.show()

# ------------------------
# Chart 3 : Sales Distribution
# ------------------------

category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(8,5))

category_sales.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Sales Distribution by Category")

plt.ylabel("")

plt.show()

# ------------------------
# Chart 4 : Top 10 Sub-Categories
# ------------------------

top_products = (
    df.groupby("Sub-Category")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

plt.figure(figsize=(10,5))

top_products.plot(kind="bar")

plt.title("Top 10 Sub-Categories by Sales")

plt.xlabel("Sub-Category")

plt.ylabel("Sales")

plt.tight_layout()

plt.show()