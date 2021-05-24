class Stack:
    def __init__(self):
        self.container=[]
    
    def push(self,element):
        if element=="(" or element=="[" or element=="{":
            self.container.append(element)
    
    def pop(self):
        self.container.pop()
    
    def peek(self):
        if self.container:
            return self.container[-1]
        else:
            return None
    
    def display(self):
        if len(self.container)==0:
            print(f"Expression has balanced parenthesis\n")
        else:
            print(f"Expression doesn't have balanced parenthesis\n")
            for i in self.container:
                print(f"{i}",end=" ")
    
def match(s):
    for ch in s:
        if ch==")" and obj.peek()=="(" or ch=="]" and obj.peek()=="[" or ch=="}" and obj.peek()=="{":
            obj.pop()
        else:
            obj.push(ch)
    
    obj.display()


obj=Stack()
exp=input("Enter the expression\n")
match(exp)