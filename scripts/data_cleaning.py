import pandas as pd
import pandas as pd
from pathlib import Path

# Get project root folder automatically
project_root = Path(__file__).resolve().parent.parent

# Dataset path
csv_file = project_root / "dataset" / "SampleSuperstore.csv"

# Check if file exists
if not csv_file.exists():
    print(f"ERROR: File not found -> {csv_file}")
    exit()

# Load dataset
df = pd.read_csv(csv_file)

print("First 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

# Remove duplicates
df.drop_duplicates(inplace=True)

# Save cleaned dataset
cleaned_file = project_root / "dataset" / "cleaned_superstore.csv"
df.to_csv(cleaned_file, index=False)

print("\nCleaning Completed Successfully!")
print(f"Cleaned file saved at: {cleaned_file}")