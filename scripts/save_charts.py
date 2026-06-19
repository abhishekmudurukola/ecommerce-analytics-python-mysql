import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Project root
project_root = Path(__file__).resolve().parent.parent

# Dataset
df = pd.read_csv(
    project_root / "dataset" / "cleaned_superstore.csv"
)

# Screenshots folder
screenshots_folder = project_root / "screenshots"

# ------------------------
# Chart 1
# ------------------------

region_sales = df.groupby("Region")["Sales"].sum()

plt.figure(figsize=(8,5))
region_sales.plot(kind="bar")

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")

plt.tight_layout()

plt.savefig(
    screenshots_folder / "sales_by_region.png"
)

plt.close()

# ------------------------
# Chart 2
# ------------------------

category_profit = df.groupby("Category")["Profit"].sum()

plt.figure(figsize=(8,5))
category_profit.plot(kind="bar")

plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")

plt.tight_layout()

plt.savefig(
    screenshots_folder / "profit_by_category.png"
)

plt.close()

# ------------------------
# Chart 3
# ------------------------

category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(8,5))

category_sales.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Sales Distribution")

plt.ylabel("")

plt.savefig(
    screenshots_folder / "category_distribution.png"
)

plt.close()

# ------------------------
# Chart 4
# ------------------------

top_products = (
    df.groupby("Sub-Category")["Sales"]
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

plt.figure(figsize=(10,5))

top_products.plot(kind="bar")

plt.title("Top 10 Sub-Categories")

plt.xlabel("Sub-Category")
plt.ylabel("Sales")

plt.tight_layout()

plt.savefig(
    screenshots_folder / "top_products.png"
)

plt.close()

print("All charts saved successfully!")