import pandas as pd

# Read your Flipkart CSV
df = pd.read_csv("flipkart_mobiles.csv")

# Find exact duplicates (same Product_name and Price)
duplicates = df[df.duplicated(subset=["Product_name", "Price"], keep=False)]

# Sort for better visibility
duplicates = duplicates.sort_values(by=["Product_name", "Price"])

# Print all duplicates
print("📦 Found Exact Duplicates:\n")
print(duplicates)

# Save duplicates separately (optional)
duplicates.to_csv("flipkart_mobiles_duplicates.csv", index=False)
print(f"\n✅ Total Exact Duplicates Found: {len(duplicates)}")
print("💾 Saved to flipkart_mobiles_duplicates.csv")
