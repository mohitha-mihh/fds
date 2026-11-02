# Ex 4a: Reading data from text files
# Create a sample text file
text = """Data science is an interdisciplinary field.
It uses statistics, programming and domain knowledge.
Python is widely used for data science.
Pandas and NumPy are popular libraries."""
with open("sample.txt", "w") as f:
    f.write(text)

# 1. Read the whole file
with open("sample.txt", "r") as f:
    print("read():\n", f.read())

# 2. Read line by line
print("\nLine by line:")
with open("sample.txt") as f:
    for i, line in enumerate(f, 1):
        print(i, line.strip())

# 3. readlines()
with open("sample.txt") as f:
    lines = f.readlines()
print("\nreadlines():", lines)

# 4. Word count / simple analysis
words = text.split()
print("\nTotal lines:", len(lines), "| Total words:", len(words))
freq = {}
for w in words:
    w = w.lower().strip(".,")
    freq[w] = freq.get(w, 0) + 1
print("Most frequent:", sorted(freq.items(), key=lambda x: -x[1])[:3])

# 5. Read text with pandas / numpy
import pandas as pd, numpy as np
with open("data.txt", "w") as f:
    f.write("id name score\n1 Asha 85\n2 Ravi 72\n3 Meena 90\n")
print("\nPandas read_table:\n", pd.read_table("data.txt", sep=" "))
print("NumPy loadtxt:\n", np.loadtxt("data.txt", skiprows=1, usecols=(0, 2)))
