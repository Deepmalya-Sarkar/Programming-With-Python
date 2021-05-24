n=int(input("Enter the number of rows\n"))
b=int(input("Enter 1 for true and 0 for false\n"))

if bool(b):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print("*",end="")
        print("")
else:
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print("*",end="")
        print("")
