import matplotlib.pyplot as plt

courses=["Python","Java","C++","JavaScript"]
students=[50,40,30,20]

plt.pie(students, labels=courses, autopct='%1.1f%%', startangle=90)
plt.title("Course Enrollment")
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()