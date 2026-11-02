# Ex 8: Z-scores and Normal Distribution
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

data = np.array([55, 62, 68, 70, 72, 75, 78, 80, 85, 90, 95, 40, 100])
mean, std = data.mean(), data.std()

# Z-score: z = (x - mean) / std
z_manual = (data - mean) / std
z_scipy = stats.zscore(data)
print("Mean:", round(mean, 2), "| Std:", round(std, 2))
print("Data   :", data)
print("Z-score:", np.round(z_manual, 2))
print("Matches scipy:", np.allclose(z_manual, z_scipy))
print("Outliers (|z| > 2):", data[np.abs(z_manual) > 2])

# Normal distribution probabilities
mu, sigma = 70, 10
print("\nP(X < 80) :", round(stats.norm.cdf(80, mu, sigma), 4))
print("P(X > 85) :", round(1 - stats.norm.cdf(85, mu, sigma), 4))
print("P(60<X<80):", round(stats.norm.cdf(80, mu, sigma) - stats.norm.cdf(60, mu, sigma), 4))
print("Value at 95th percentile:", round(stats.norm.ppf(0.95, mu, sigma), 2))

# 68-95-99.7 rule
sample = np.random.normal(mu, sigma, 10000)
for k in (1, 2, 3):
    pct = np.mean(np.abs(sample - mu) <= k * sigma) * 100
    print(f"Within {k} sd: {pct:.2f}%")

# Visualization
x = np.linspace(mu - 4 * sigma, mu + 4 * sigma, 500)
fig, ax = plt.subplots(1, 2, figsize=(13, 5))
ax[0].plot(x, stats.norm.pdf(x, mu, sigma), "b")
ax[0].fill_between(x, stats.norm.pdf(x, mu, sigma), where=(x < 80), alpha=0.4, color="orange")
ax[0].set_title("Normal Distribution: P(X < 80)")
ax[1].hist(sample, bins=40, density=True, alpha=0.6, edgecolor="black")
ax[1].plot(x, stats.norm.pdf(x, mu, sigma), "r", lw=2)
ax[1].set_title("Sample vs Normal Curve")
plt.tight_layout()
plt.savefig("normal_distribution.png")
plt.show()

# Normality check
stat, p = stats.shapiro(sample[:500])
print("\nShapiro-Wilk p-value:", round(p, 4), "->", "Normal" if p > 0.05 else "Not normal")
