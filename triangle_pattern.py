a=0
for i in range(1,6):
    a=a+1
    for k in range(5,a,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print(j,end="")
    for m in range(i-1,0,-1):
        print(m,end="")
    print("")
