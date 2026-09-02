import matplotlib.pyplot as plt

courses=["Python","Java","C++","JavaScript"]
students=[50,40,30,20]

plt.bar(courses,students)
plt.title("Course Enrollment")
plt.xlabel("Courses")
plt.ylabel("Number of Students")
plt.title("Monthly Sales Report")
plt.show()