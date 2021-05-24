class A:
    def __init__(self,string):
        self.var=string
    
    def printing(self):
        print(f"The string is {self.var}")

class B(A):
    def __init__(self,string1,string2):
        super().__init__(string1)
        self.var2=string2
    
    def printing(self):
        print(f"{self.var2}, the class is {self.var}")

deep=A("Class A")
deep.printing()
deep2=B("Class B","Hi!")
deep2.printing()