# Ex 3a: Aggregate data using groupby
import pandas as pd

df = pd.DataFrame({
    "Region": ["North", "South", "North", "East", "South", "East", "North", "South"],
    "Product": ["A", "B", "A", "B", "A", "A", "B", "B"],
    "Sales": [250, 300, 150, 400, 200, 350, 100, 500],
    "Units": [5, 6, 3, 8, 4, 7, 2, 10],
})
print("Dataset:\n", df)

print("\nTotal sales by Region:\n", df.groupby("Region")["Sales"].sum())
print("\nMean sales by Product:\n", df.groupby("Product")["Sales"].mean())
print("\nMultiple aggregates:\n",
      df.groupby("Region")["Sales"].agg(["sum", "mean", "min", "max", "count"]))
print("\nGroup by two keys:\n", df.groupby(["Region", "Product"])["Sales"].sum())
print("\nDifferent aggregations per column:\n",
      df.groupby("Region").agg({"Sales": "sum", "Units": "mean"}))
print("\nFilter groups with total sales > 500:\n",
      df.groupby("Region").filter(lambda g: g["Sales"].sum() > 500))
df["Region_Avg"] = df.groupby("Region")["Sales"].transform("mean")
print("\nTransform (group mean added):\n", df)
for name, group in df.groupby("Region"):
    print(f"\nGroup: {name}\n", group)
