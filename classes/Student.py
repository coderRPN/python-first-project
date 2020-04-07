class Student:
    def __init__(self, name, grade, roll_no, percentage):
        self.name = name
        self.grade = grade
        self.roll_no = roll_no
        self.percentage = percentage

    def is_with_honors(self):
        if self.percentage >= 80:
            return True
        else:
            return False
