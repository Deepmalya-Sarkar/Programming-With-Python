li=[]
n=int(input("Enter the total number of elements\n"))
print("Enter the elements")

for i in range(0,n):
    li.append(int(input()))

m=max(li)
li.remove(m)
print("The 2nd max element is {}".format(max(li)))
