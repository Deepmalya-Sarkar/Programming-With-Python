def binary_search(arr,key):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==key:
            return mid
        elif key>arr[mid]:
            low=mid+1
        else:
            high=mid-1
    return -1



n=int(input("Enter the number of elements you want to enter\n"))
print("Enter the elements\n")
arr=[]
for i in range(n):
    arr.append(int(input()))
key=int(input("Enter the number you want to search\n"))
b=binary_search(arr,key)
if b==-1:
    print("Element not found")
else:
    print(f"Element found at {b+1}")
