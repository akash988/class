class Employee:
   no_of_leaves =8

   def __init__(self,aname,asalary,arole,aaddress):
       self.name=aname
       self.salary=asalary
       self.role=arole
       self.address=aaddress
   #def printdetails(self):
        #return f"This Employee name is {self.name},Employee salary is {self.salary},Employee role is {self.role}"
   #change method
   def from_dash(cls, string):
        return cls(*string.split('-'))

harry = Employee("HARRY POTTER",455,"ASSISTANT","MUMBAI")
karan = Employee.from_dash("KARAN-2000000-SELFASSISTANT-PUNE")

#harry.name = "HARRY POTTER"
#harry.salary = 455
#harry.role = "ASSISTANT"

print(harry.__dict__)
print(karan.salary)