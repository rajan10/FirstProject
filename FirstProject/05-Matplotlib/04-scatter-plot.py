import matplotlib.pyplot as plt


study_hours = [1, 2, 3, 4, 5]
grades = [50, 60, 70, 80, 90]
plt.scatter(study_hours, grades)
plt.title("Study Hours vs Grades")
plt.xlabel("Study Hours")
plt.ylabel("Grades")
plt.show()