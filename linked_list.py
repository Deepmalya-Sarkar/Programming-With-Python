class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    
    def append(self,new_element):
        new_node=Node(new_element)
        if self.head:
            current=self.head
            while current.next:
                current=current.next
            current.next=new_node
        else:
            self.head=new_node
    
    def insert(self,new_element,position):
        new_node=Node(new_element)
        counter=1
        current=self.head
        if position>1:
            while current and counter<position:
                if counter==position-1:
                    new_node.next=current.next
                    current.next=new_node
                current=current.next
                counter+=1
        elif position==1:
            new_node.next=self.head
            self.head=new_node

    def get_element(self,position):
        counter=1
        current=self.head
        if position>=1:
            while current and counter<=position:
                if counter==position:
                    return current.value
                current=current.next
                counter+=1
            return None
        else:
            return None

    def delete(self,key):
        current=self.head
        if self.head:
            if self.head.value==key:
                self.head=current.next
            else:
                while current.next:
                    if current.next.value==key:
                        current.next=current.next.next
                        break
                    current=current.next
                else:
                    print("No such element present\n")
        else:
            print("No such element present\n")

    
    def display(self):
        current=self.head
        while current:
            print(f"{current.value}",end=" ")
            current=current.next

L1=LinkedList()
while True:
    print("Press 1 for appending to the list\n")
    print("Press 2 for inserting to the beginning or middle of the list\n")
    print("Press 3 for getting an element at a particular position\n")
    print("Press 4 for deleting an element\n")
    print("Press 5 for displaying the list\n")
    print("Press 0 to exit\n")
    n=int(input("Enter your choice\n"))
    if n==0:
        break

    elif n==1:
        limit=int(input("Enter the number of elements you want to enter\n"))
        print("Enter the elements\n")
        for i in range(limit):
            L1.append(int(input()))
    
    elif n==2:
        e=int(input("Enter the element\n"))
        p=int(input("Enter the position\n"))
        L1.insert(e,p)

    elif n==3:
        p=int(input("Enter the position\n"))
        e=L1.get_element(p)
        print(f"\n{e}")

    elif n==4:
        e=int(input("Enter the element you want to delete\n"))
        L1.delete(e)
    elif n==5:
        L1.display()
        print()



