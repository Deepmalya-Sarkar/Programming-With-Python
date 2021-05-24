class A:
   var1="This is class A"

   def display1(self):
       print(f"{self.var1}")

class B:
    var2="This is class B"

    def display2(self):
       print(f"{self.var2}")
  

class C(A,B):
    just="This is C"


    def displaying(self):
        super().display1()
        super().display2()
        print(f"And then {self.just}")

c=C()
c.displaying()
