

class Employee:
    no_of_leaves = 8
    pass

harry = Employee()
rohan = Employee()

harry.name = "HARRY POTTER"
harry.salary = 455
harry.role = "Instructor"

rohan.name = "RAM RANE"
rohan.salary=67548
rohan.role="JUNIOR ASSISTANT ENGINEER"

print(Employee.no_of_leaves)
print(rohan.__dict__)
Employee.no_of_leaves = 9
print(Employee.__dict__)
print(Employee.no_of_leaves)

