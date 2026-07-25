class faculty:
    def getdata(self):
        self.name = input("Enter your name: ")
        self.id = int(input("Enter your ID: "))
        self.salary = float(input("Enter your salary: "))

    def display(self):
        print("Faculty Name: ", self.name)
        print("Faculty ID: ", self.id)
        print("Faculty Salary: ",self.salary)

f = faculty()
f.getdata()
f.display()