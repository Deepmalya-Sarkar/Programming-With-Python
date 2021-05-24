n=int(input("Enter the number of rows\n"))
a=n
for i in range(1,n+1):
    for k in range(a,1,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end="")
    for m in range(1,i):
        print("*",end="")
    print("")
    a=a-1