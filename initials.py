name=input("Enter the name\n")
name1=" "+name
l=len(name1)
for i in range(0,l):
    if name1[i]==" ":
        k=i
        for j in range(k+1,l):
            if name1[j]==" ":
                print("{}. ".format(name1[k+1]),end="")
                break
print(name1[k+1:])