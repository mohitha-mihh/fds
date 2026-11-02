# Ex 7: Data description and visualization
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)
df = pd.DataFrame({
    "Age": np.random.randint(18, 60, 100),
    "Salary": np.random.normal(50000, 12000, 100).round(2),
    "Experience": np.random.randint(0, 30, 100),
    "Dept": np.random.choice(["HR", "IT", "Sales", "Finance"], 100),
})

# ---- Data description ----
print("Head:\n", df.head())
print("\nShape:", df.shape)
print("\nInfo:"); df.info()
print("\nDescribe:\n", df.describe())
print("\nMissing values:\n", df.isnull().sum())
print("\nDept counts:\n", df["Dept"].value_counts())
print("\nMean:\n", df[["Age", "Salary", "Experience"]].mean())
print("Median:\n", df[["Age", "Salary", "Experience"]].median())
print("Mode of Age:", df["Age"].mode()[0])
print("Variance:\n", df[["Age", "Salary"]].var())
print("Skewness:\n", df[["Age", "Salary"]].skew())
print("Kurtosis:\n", df[["Age", "Salary"]].kurt())
print("Quantiles:\n", df["Salary"].quantile([0.25, 0.5, 0.75]))
print("Salary by Dept:\n", df.groupby("Dept")["Salary"].agg(["mean", "median", "std"]))

# ---- Visualization ----
fig, ax = plt.subplots(2, 3, figsize=(16, 9))
ax[0, 0].hist(df["Salary"], bins=15, color="skyblue", edgecolor="black"); ax[0, 0].set_title("Salary Histogram")
ax[0, 1].boxplot(df["Salary"]); ax[0, 1].set_title("Salary Box Plot")
df["Dept"].value_counts().plot(kind="bar", ax=ax[0, 2], color="orange"); ax[0, 2].set_title("Dept Count")
ax[1, 0].scatter(df["Experience"], df["Salary"], alpha=0.6); ax[1, 0].set_title("Experience vs Salary")
df["Dept"].value_counts().plot(kind="pie", ax=ax[1, 1], autopct="%1.1f%%"); ax[1, 1].set_title("Dept Share"); ax[1, 1].set_ylabel("")
df.groupby("Dept")["Salary"].mean().plot(kind="bar", ax=ax[1, 2], color="green"); ax[1, 2].set_title("Avg Salary by Dept")
plt.tight_layout()
plt.savefig("data_description.png")
plt.show()
