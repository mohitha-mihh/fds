# Ex 4c: Reading data from a web file (URL)
import pandas as pd

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"

try:
    df = pd.read_csv(url)
    print("Data loaded from web.")
except Exception as e:
    print("Could not reach URL:", e)
    print("Using local fallback sample data.")
    df = pd.DataFrame({
        "sepal_length": [5.1, 4.9, 6.2, 5.9],
        "sepal_width": [3.5, 3.0, 3.4, 3.0],
        "petal_length": [1.4, 1.4, 5.4, 5.1],
        "petal_width": [0.2, 0.2, 2.3, 1.8],
        "species": ["setosa", "setosa", "virginica", "virginica"],
    })

print("\nHead:\n", df.head())
print("\nShape:", df.shape)
print("\nColumns:", list(df.columns))
print("\nSummary:\n", df.describe())
print("\nSpecies count:\n", df["species"].value_counts())
print("\nMean by species:\n", df.groupby("species").mean(numeric_only=True))

# Reading an HTML table from a web page (optional, needs lxml)
# tables = pd.read_html("https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)")
# print(tables[0].head())
