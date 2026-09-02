import pandas as pd

students={"name":["Ravi","Ramesh","Suresh","Mahesh"],
          "course":["Python","Java","C++","JavaScript"],
          "marks":[85,90,78,92]    }


df=pd.DataFrame(students).to_csv("students.csv",index=False)
print("CSV file created successfully!")
