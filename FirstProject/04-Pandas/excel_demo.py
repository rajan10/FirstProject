import pandas as pd

students={"name":["Ravi","Ramesh","Suresh","Mahesh"],
          "course":["Python","Java","C++","JavaScript"],
          "marks":[85,90,78,92]    }

pd.DataFrame(students).to_excel("students.xlsx",index=False)
print("Excel file created successfully!")

df=pd.read_excel("students.xlsx")
print(df.head())