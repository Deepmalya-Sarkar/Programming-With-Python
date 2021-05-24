class Stack:
    def __init__(self):
        self.storage=[]
    
    def push(self,new_element):
        self.storage.append(new_element)
    
    def pop(self):
        if self.storage: 
            return self.storage.pop()
        else:
            return "No element left to pop"
    
    def display(self):
        for i in self.storage:
            print(f"{i}",end=" ")

S=Stack()
while True:
    print("Press 1 for appending to the stack\n")
    print("Press 2 for poping the last element\n")
    print("Press 3 for displaying the list\n")
    print("Press 0 to exit\n")
    n=int(input("Enter your choice\n"))
    if n==0:
        break

    elif n==1:
        S.push(int(input("Enter the element\n")))
    
    elif n==2:
        e=S.pop()
        print(f"\n{e}\n")

    elif n==3:
        S.display()
        print()



