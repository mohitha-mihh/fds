# Ex 3c: Aggregate data using hierarchical (multi-level) indexes
import pandas as pd
import numpy as np

arrays = [["2023", "2023", "2024", "2024", "2025", "2025"],
          ["Q1", "Q2", "Q1", "Q2", "Q1", "Q2"]]
index = pd.MultiIndex.from_arrays(arrays, names=["Year", "Quarter"])
s = pd.Series([100, 120, 130, 150, 170, 190], index=index)
print("MultiIndex Series:\n", s)

# Indexing
print("\nYear 2024:\n", s["2024"])
print("2024, Q2:", s["2024", "Q2"])
print("All Q1:\n", s.xs("Q1", level="Quarter"))

# DataFrame with MultiIndex
idx = pd.MultiIndex.from_product([["2023", "2024"], ["Q1", "Q2"]], names=["Year", "Quarter"])
df = pd.DataFrame(np.random.randint(50, 200, (4, 2)), index=idx, columns=["Sales", "Profit"])
print("\nDataFrame:\n", df)

# Aggregation by level
print("\nSum by Year:\n", df.groupby(level="Year").sum())
print("Mean by Quarter:\n", df.groupby(level="Quarter").mean())

# Stack / unstack / reset / swap
print("\nUnstack:\n", df.unstack())
print("Swap levels:\n", df.swaplevel().sort_index())
print("Reset index:\n", df.reset_index())
print("Slice with loc:\n", df.loc["2023"])
