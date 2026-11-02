# Ex 4d: Reading data from an Excel file  (pip install openpyxl)
import pandas as pd

# Create a sample Excel file with two sheets
students = pd.DataFrame({"ID": [1, 2, 3, 4], "Name": ["Asha", "Ravi", "Meena", "Kiran"],
                         "Marks": [85, 72, 90, 65]})
staff = pd.DataFrame({"EmpID": [101, 102], "Name": ["Dr. Kumar", "Dr. Devi"],
                      "Dept": ["CSE", "IT"]})
with pd.ExcelWriter("college.xlsx") as writer:
    students.to_excel(writer, sheet_name="Students", index=False)
    staff.to_excel(writer, sheet_name="Staff", index=False)

# Read default (first) sheet
print("First sheet:\n", pd.read_excel("college.xlsx"))

# Read a specific sheet
print("\nStaff sheet:\n", pd.read_excel("college.xlsx", sheet_name="Staff"))

# Read all sheets
all_sheets = pd.read_excel("college.xlsx", sheet_name=None)
for name, sheet in all_sheets.items():
    print(f"\nSheet '{name}' shape: {sheet.shape}")

# Read selected columns / rows
print("\nSelected columns:\n", pd.read_excel("college.xlsx", usecols=["Name", "Marks"]))
print("\nFirst 2 rows:\n", pd.read_excel("college.xlsx", nrows=2))

# Sheet names
xl = pd.ExcelFile("college.xlsx")
print("\nSheet names:", xl.sheet_names)
print("Average marks:", students["Marks"].mean())
