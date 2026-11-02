# Ex 5: Basic plots using Matplotlib and three-dimensional plots
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)

# ---- Basic 2D plots ----
fig, ax = plt.subplots(2, 3, figsize=(15, 8))

ax[0, 0].plot(x, np.sin(x), "b-", label="sin")
ax[0, 0].plot(x, np.cos(x), "r--", label="cos")
ax[0, 0].set_title("Line Plot"); ax[0, 0].legend(); ax[0, 0].grid(True)

ax[0, 1].scatter(np.random.rand(50), np.random.rand(50), c="green", marker="o")
ax[0, 1].set_title("Scatter Plot")

ax[0, 2].bar(["A", "B", "C", "D"], [23, 45, 12, 36], color="orange")
ax[0, 2].set_title("Bar Chart")

ax[1, 0].hist(np.random.randn(1000), bins=20, color="purple", edgecolor="black")
ax[1, 0].set_title("Histogram")

ax[1, 1].pie([30, 25, 25, 20], labels=["P", "Q", "R", "S"], autopct="%1.1f%%")
ax[1, 1].set_title("Pie Chart")

ax[1, 2].boxplot([np.random.randn(100) for _ in range(3)])
ax[1, 2].set_title("Box Plot")

plt.tight_layout()
plt.savefig("basic_plots.png")
plt.show()

# ---- Three-dimensional plots ----
fig = plt.figure(figsize=(15, 5))

# 3D line
ax1 = fig.add_subplot(1, 3, 1, projection="3d")
z = np.linspace(0, 15, 200)
ax1.plot3D(np.sin(z), np.cos(z), z, "gray")
ax1.set_title("3D Line")

# 3D scatter
ax2 = fig.add_subplot(1, 3, 2, projection="3d")
ax2.scatter3D(np.random.rand(100), np.random.rand(100), np.random.rand(100), c=np.random.rand(100))
ax2.set_title("3D Scatter")

# 3D surface
ax3 = fig.add_subplot(1, 3, 3, projection="3d")
X, Y = np.meshgrid(np.linspace(-5, 5, 50), np.linspace(-5, 5, 50))
Z = np.sin(np.sqrt(X**2 + Y**2))
ax3.plot_surface(X, Y, Z, cmap="viridis")
ax3.set_title("3D Surface")

plt.tight_layout()
plt.savefig("3d_plots.png")
plt.show()
