class Employee:
    leaves=9
    def __init__(self, aname,asalary):
        self.name=aname
        self.salary=asalary
    
    def leavechange(self):
        self.leave=10
    
    def printing(self):
        print(f"{self.name}\n{self.leave}\n{self.salary}")
    
deep=Employee("Deepmalya Sarkar",50000)
deep.leavechange()
deep.printing()
print(Employee.leaves)