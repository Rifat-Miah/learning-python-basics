class student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def average(self):
        return sum(self.marks)/len(self.marks)

student1 = student("Rifat", 33, [78, 87, 92, 85, 75.90])  # (name, roll, marks)
print("Student Name: ", student1.name)
print("Student Roll: ", student1.roll)
print("Sudent marks: ", student1.marks)
print("Student average mark = ", student1.average())