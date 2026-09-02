import pandas as pd

marks=pd.Series([10, 20, 30, 40, 50])
print(marks)

students =pd.Series([85, 90, 78, 92], index=["Alice", "Bob", "Charlie", "Diana"])
print(students)