def reverseArray(arr):
    start=0
    end=len(arr)-1
    while start<=end:
        arr[start],arr[end]=arr[end],arr[start]
        end-=1
        start+=1
    return arr
n=int(input("enter the limit\n"))
arr=list()
print("Enter the numbers")
for i in range(n):
    arr.append(int(input()))
print(f"{reverseArray(arr)}")