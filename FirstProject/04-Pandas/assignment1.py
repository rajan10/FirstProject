import pandas as pd
students = {
    "Name":["Ravi","Sita","Kiran","Rahul","Priya"],
    "Course":["Python","Java","Python","DevOps","Python"],
    "Marks":[85,90,75,60,95]
}
# print(type(students))
df=pd.DataFrame(students)
print("-"*50)
print("Question 1: Show only python students")
python_students = df[df["Course"] == "Python"]
print(python_students)
print("-"*50)
print("Question 2:Show students with marks > 80")
high_marks = df[df["Marks"] > 80]
print(high_marks)
print("-"*50)
print("Question 3:Sort students based on marks")
sorted_students= df.sort_values("Marks", ascending=False)
print(sorted_students)
print("-"*50)
print("Question 4:Find Highest marks")
highest_marks = df["Marks"].max()
print(highest_marks)
print("-"*50)
print("Question 5: Find Avg Marks")
avg_marks = df["Marks"].mean()
print(avg_marks)
print("-"*50)
print("Question 6: Count students in each course")
course_counts = df["Course"].value_counts()
print(course_counts)
print("-"*50)
# print("Question 7: Add Grade Column")
# def assign_grade(marks):
#     if marks >= 90:
#         return "A"
#     elif marks >= 80:
#         return "B"
#     elif marks >= 70:
#         return "C"
#     else:
#         return "D"
# df["Grade"] = df["Marks"].apply(assign_grade)
# print(df)

df.loc[(df["Marks"] >= 90) & (df["Marks"] <= 100), "Grade"] = "A"
df.loc[(df["Marks"] >= 80) & (df["Marks"] < 90), "Grade"] = "B"
df.loc[(df["Marks"] >= 70) & (df["Marks"] < 80), "Grade"] = "C"
df.loc[(df["Marks"] >= 60) & (df["Marks"] < 70), "Grade"] = "D"
df.loc[(df["Marks"] >= 50) & (df["Marks"] < 60), "Grade"] = "E"
print(df)
print("-"*50)
df.to_csv("students_csv.csv", index=False)


df = pd.read_csv("students_csv.csv")
print("-"*50)
print(df)
df.to_excel("students.xlsx", index=False)