# Ex 6: Visualizing geographic data with Basemap and Matplotlib
# Install: pip install basemap basemap-data-hires matplotlib
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# ---- 1. World map ----
plt.figure(figsize=(12, 6))
m = Basemap(projection="mill", llcrnrlat=-60, urcrnrlat=90,
            llcrnrlon=-180, urcrnrlon=180, resolution="c")
m.drawcoastlines()
m.drawcountries()
m.fillcontinents(color="lightgreen", lake_color="aqua")
m.drawmapboundary(fill_color="aqua")
m.drawparallels(np.arange(-60, 91, 30), labels=[1, 0, 0, 0])
m.drawmeridians(np.arange(-180, 181, 60), labels=[0, 0, 0, 1])
plt.title("World Map (Miller Projection)")
plt.savefig("world_map.png")
plt.show()

# ---- 2. Plot cities on a map of India ----
cities = {"Chennai": (13.08, 80.27), "Delhi": (28.61, 77.21), "Mumbai": (19.07, 72.88),
          "Kolkata": (22.57, 88.36), "Bengaluru": (12.97, 77.59)}
population = {"Chennai": 11, "Delhi": 32, "Mumbai": 21, "Kolkata": 15, "Bengaluru": 13}

plt.figure(figsize=(8, 9))
m = Basemap(projection="merc", llcrnrlat=6, urcrnrlat=37,
            llcrnrlon=67, urcrnrlon=98, resolution="l")
m.drawcoastlines()
m.drawcountries()
m.drawstates(linewidth=0.3)
m.fillcontinents(color="wheat", lake_color="lightblue")
m.drawmapboundary(fill_color="lightblue")

for city, (lat, lon) in cities.items():
    x, y = m(lon, lat)
    m.scatter(x, y, s=population[city] * 20, c="red", alpha=0.6, zorder=5)
    plt.text(x + 20000, y + 20000, city, fontsize=9)

plt.title("Major Indian Cities (size = population in millions)")
plt.savefig("india_cities.png")
plt.show()

# ---- 3. Orthographic globe ----
plt.figure(figsize=(7, 7))
m = Basemap(projection="ortho", lat_0=20, lon_0=80)
m.fillcontinents(color="green", lake_color="blue")
m.drawcoastlines()
m.drawmapboundary(fill_color="aqua")
m.drawparallels(np.arange(-90, 91, 30))
m.drawmeridians(np.arange(0, 360, 30))
plt.title("Orthographic Projection")
plt.savefig("globe.png")
plt.show()
