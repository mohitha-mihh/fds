# Ex 9: Correlation coefficients and scatter plots
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

np.random.seed(1)
hours = np.random.uniform(1, 10, 50)
df = pd.DataFrame({
    "Hours_Studied": hours,
    "Marks": 35 + 6 * hours + np.random.normal(0, 5, 50),      # positive correlation
    "Hours_Gaming": 10 - hours + np.random.normal(0, 1.5, 50),  # negative correlation
    "Random": np.random.rand(50) * 100,                         # no correlation
})

# Correlation coefficients
print("Pearson correlation matrix:\n", df.corr().round(3))
print("\nSpearman:\n", df.corr(method="spearman").round(3))
print("\nKendall:\n", df.corr(method="kendall").round(3))

r, p = stats.pearsonr(df["Hours_Studied"], df["Marks"])
print(f"\nPearson r (Hours vs Marks) = {r:.3f}, p-value = {p:.4g}")
print("NumPy corrcoef:\n", np.corrcoef(df["Hours_Studied"], df["Marks"]).round(3))

# Scatter plots
fig, ax = plt.subplots(1, 3, figsize=(16, 4.5))
pairs = [("Hours_Studied", "Marks", "Positive"),
         ("Hours_Studied", "Hours_Gaming", "Negative"),
         ("Hours_Studied", "Random", "No correlation")]
for a, (x, y, t) in zip(ax, pairs):
    a.scatter(df[x], df[y], alpha=0.7)
    m, c = np.polyfit(df[x], df[y], 1)
    a.plot(df[x], m * df[x] + c, "r")
    a.set_title(f"{t} (r = {df[x].corr(df[y]):.2f})")
    a.set_xlabel(x); a.set_ylabel(y)
plt.tight_layout()
plt.savefig("scatter_correlation.png")
plt.show()

# Correlation heatmap
plt.figure(figsize=(6, 5))
plt.imshow(df.corr(), cmap="coolwarm", vmin=-1, vmax=1)
plt.colorbar()
plt.xticks(range(4), df.columns, rotation=45)
plt.yticks(range(4), df.columns)
for i in range(4):
    for j in range(4):
        plt.text(j, i, round(df.corr().iloc[i, j], 2), ha="center", va="center")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("heatmap.png")
plt.show()
