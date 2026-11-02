# Ex 2: Indexing, slicing, filtering and reshaping data with Pandas
import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name": ["Asha", "Ravi", "Meena", "Kiran", "Divya", "Arun"],
    "Dept": ["CSE", "ECE", "CSE", "IT", "ECE", "IT"],
    "Year": [1, 2, 3, 2, 1, 3],
    "Marks": [85, 72, 90, 65, 78, 88],
})
print("DataFrame:\n", df)

# Indexing
print("\nColumn 'Name':\n", df["Name"])
print("Multiple columns:\n", df[["Name", "Marks"]])
print("iloc[2]:\n", df.iloc[2])
print("loc[1:3, ['Name','Marks']]:\n", df.loc[1:3, ["Name", "Marks"]])
print("iloc[0:3, 1:3]:\n", df.iloc[0:3, 1:3])

# Slicing
print("\nFirst 3 rows:\n", df[:3])
print("Alternate rows:\n", df[::2])

# Filtering
print("\nMarks > 80:\n", df[df["Marks"] > 80])
print("CSE and Marks > 85:\n", df[(df["Dept"] == "CSE") & (df["Marks"] > 85)])
print("Dept in [ECE, IT]:\n", df[df["Dept"].isin(["ECE", "IT"])])
print("Query Year == 2:\n", df.query("Year == 2"))

# Reshaping
pivot = df.pivot_table(values="Marks", index="Dept", columns="Year", aggfunc="mean")
print("\nPivot table:\n", pivot)
print("Stacked:\n", pivot.stack())
print("Unstacked:\n", pivot.stack().unstack())
melted = pd.melt(df, id_vars=["Name"], value_vars=["Year", "Marks"])
print("Melted:\n", melted.head(8))
print("Transpose:\n", df.set_index("Name").T)
