class Queue:
    def __init__(self):
        self.storage=[]
    
    def enqueue(self,new_element):
        self.storage.append(new_element)
    
    def dequeue(self):
        if self.storage:
            return self.storage.pop(0)
        else:
            return "No element left to be dequeued\n"
    
    def display(self):
        for i in self.storage:
            print(f"{i}",end=" ")

Q=Queue()
while True:
    print("Press 1 for enqueuing\n")
    print("Press 2 for dequeuing\n")
    print("Press 3 for displaying the queue\n")
    print("Press 0 to exit\n")
    n=int(input("Enter your choice\n"))
    if n==0:
        break

    elif n==1:
        Q.enqueue(int(input("Enter the element\n")))
    
    elif n==2:
        e=Q.dequeue()
        print(f"\n{e}\n")

    elif n==3:
        Q.display()
        print()

