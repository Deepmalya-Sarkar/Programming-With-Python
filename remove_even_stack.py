class Stack:
    def __init__(self):
        self.container=[]
    
    def push(self,e):
        self.container.append(e)
    
    def pop(self):
        self.container.pop()

    def peek(self):
        if self.container:
            return self.container[-1]
        else:
            return None
    
    def display(self):
        if self.container:
            for i in self.container:
                print(f"{i}",end="")
        else:
            print("KHALI")
        print("")
        self.container=[]

def match(n):
    for ch in n:
        if ch==s.peek():
            s.pop()
        else:
            s.push(ch)
    s.display()

s=Stack()
if __name__=='__main__':
    t=int(input())
    n=[]
    for i in range(0,t):
        n.append(input())
    
    for i in range(0,t):
        match(n[i])
