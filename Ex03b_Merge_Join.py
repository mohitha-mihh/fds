# Ex 3b: Aggregate data using merge / join
import pandas as pd

students = pd.DataFrame({"ID": [1, 2, 3, 4], "Name": ["Asha", "Ravi", "Meena", "Kiran"]})
marks = pd.DataFrame({"ID": [2, 3, 4, 5], "Marks": [72, 90, 65, 80]})
print("Students:\n", students, "\n\nMarks:\n", marks)

print("\nInner join:\n", pd.merge(students, marks, on="ID", how="inner"))
print("\nLeft join:\n", pd.merge(students, marks, on="ID", how="left"))
print("\nRight join:\n", pd.merge(students, marks, on="ID", how="right"))
print("\nOuter join:\n", pd.merge(students, marks, on="ID", how="outer"))

# Different key names
dept = pd.DataFrame({"StudentID": [1, 2, 3], "Dept": ["CSE", "ECE", "IT"]})
print("\nMerge on different column names:\n",
      pd.merge(students, dept, left_on="ID", right_on="StudentID").drop("StudentID", axis=1))

# join() on index
print("\nJoin using index:\n", students.set_index("ID").join(marks.set_index("ID"), how="inner"))

# Concatenation
print("\nConcat (rows):\n", pd.concat([students, students.iloc[:2]], ignore_index=True))
print("\nConcat (columns):\n", pd.concat([students, marks], axis=1))

# Merge then aggregate
merged = pd.merge(students, marks, on="ID")
print("\nAverage marks of merged data:", merged["Marks"].mean())
