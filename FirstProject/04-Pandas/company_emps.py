import pandas as pd
employees = {

    "EmpId": [101, 102, 103, 104, 105],
    "Name": ["John", "Alice", "Bob", "Eve", "Charlie"],
    "Department": ["HR", "IT", "Finance", "IT", "HR"],
    "Salary": [50000, 60000, 55000, 70000, 65000],
    "Experience": [2, 5, 3, 7, 4]
}
df=pd.DataFrame(employees)
print("---------------*25")
print(df)
print("---------------*25")
print(df.head(3))
print("-"*25)
print(df.tail(3))
print(df["Name"])
print("-"*25)
print(df[["Name", "Salary"]])
print("-"*25)
print(df[df["Salary"]>60000])
print("-"*50)
print(df[df["Department"]=="IT"])
print("-"*50)
print(df[df["Experience"]>3][["Name", "Department", "Salary"]])
print("-"*50)
print(df[(df["Department"]=="IT") & (df["Salary"] > 60000)])
print("-"*50)
print(df[(df["Department"]=="IT") | (df["Salary"] > 60000)])
print("-"*50)
print(df.sort_values("Salary",ascending=False))
print("-"*50)
print(df.sort_values(["Salary", "Department"], ascending=[False, True]))
print("-"*50)
df["Bonus"]=df["Salary"]*0.1
print(df)
print("-"*50)
df["Total Salary"]=df["Salary"]+df["Bonus"]
print(df)
print("-"*50)
df.drop(columns=["Bonus"], inplace=True)
print(df)
print("-"*50)
print(df.groupby("Department")["Salary"].mean())
print(df.groupby("Department")["Salary"].describe())
print("-"*50)
print(df["Department"].unique())
print("-"*50)
print(df["Department"].nunique())
print("-"*50)

employees = {
    "Name": ["John", "Alice", "Bob", "Eve", "Charlie"],
    "Salary": [50000, None, 55000, 70000, None]
}
df=pd.DataFrame(employees)
print(df)
print(df.isnull())
print("-"*50)
print(df.dropna())
print("-"*50)
# ndf=df.fillna(df["Salary"].mean(), inplace=True)
# print(ndf)
print("-"*50)
ndf=df.fillna(0, inplace=True)
print(ndf)