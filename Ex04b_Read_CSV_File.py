# Ex 4b: Reading data from a CSV file
import pandas as pd

# Create a sample CSV file
pd.DataFrame({
    "ID": [1, 2, 3, 4, 5],
    "Name": ["Asha", "Ravi", "Meena", "Kiran", "Divya"],
    "Dept": ["CSE", "ECE", "CSE", "IT", "ECE"],
    "Marks": [85, 72, 90, None, 78],
}).to_csv("students.csv", index=False)

df = pd.read_csv("students.csv")
print("Data:\n", df)
print("\nHead(3):\n", df.head(3))
print("\nShape:", df.shape)
print("Columns:", list(df.columns))
print("\nInfo:"); df.info()
print("\nDescribe:\n", df.describe())
print("\nMissing values:\n", df.isnull().sum())

# Reading options
print("\nSelected columns:\n", pd.read_csv("students.csv", usecols=["Name", "Marks"]))
print("\nIndex column set:\n", pd.read_csv("students.csv", index_col="ID"))
print("\nFirst 2 rows:\n", pd.read_csv("students.csv", nrows=2))

# Handle missing data and write back
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())
df.to_csv("students_clean.csv", index=False)
print("\nCleaned data saved:\n", df)
