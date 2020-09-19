class Employee:
    no_of_leaves=8

    def __init__(self,name,rollno,gender,gmail):
        self.Name=name
        self.Rollno=rollno
        self.Gender=gender
        self.gmail=gmail


pankaj=Employee("PANKAJ RATHOD",12,"MALE","ABCD1234@GMAIL.COM")



print(pankaj.__dict__)
Employee.no_of_leaves=12
print(Employee.no_of_leaves)