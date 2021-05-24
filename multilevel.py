class A:
    var1="This is class A"

class B(A):
    var2="This is class B"
    var3="This is class B's 2nd part"

class C(B):
    var4="This is class C"

    def printing(self):
        print(f"{self.var1}\t{self.var2}\t{self.var3}\t{self.var4}")

cobj=C()
cobj.printing()