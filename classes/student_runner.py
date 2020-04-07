from classes.Student import Student

student1 = Student("prabhdeep", 13, 335, 79)
student2 = Student("prabhdeep", 13, 335, 81)

print(student1.name)
print(student1.grade)
print(student1.roll_no)

print("is student 1 with honors: " + str(student1.is_with_honors()))
print("is student 2 with honors: " + str(student2.is_with_honors()))