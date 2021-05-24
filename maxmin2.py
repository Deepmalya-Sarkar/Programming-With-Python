def maxmin(a):
    min_a=a[0]
    max_a=a[0]
    
    for i in range(n):
        if a[i]<min_a:
            min_a=a[i]
        if a[i]>max_a:
            max_a=a[i]
    
    print(f"{min_a} {max_a}")
n=int(input("Enter the limit\n"))
arr=list()
print("Enter the elements\n")
for i in range(n):
    arr.append(int(input()))

maxmin(arr)