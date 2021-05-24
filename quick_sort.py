def quick_sort(arr,low,high):
    if low<high:
        p=partition(arr,low,high)
        quick_sort(arr,low,p-1)
        quick_sort(arr,p+1,high)

def get_pivot(arr,low,high):
    mid=(low+high)//2
    pivot=high
    if arr[low]<arr[mid]:
        if arr[mid]<arr[high]:
            pivot=mid
    elif arr[low]<arr[high]:
        pivot=low
    return pivot

def partition(arr,low,high):
    pivotindex=get_pivot(arr,low,high)
    pivotvalue=arr[pivotindex]
    arr[pivotindex],arr[low]=arr[low],arr[pivotindex]
    border=low

    for i in range(low,high+1):
        if arr[i]<pivotvalue:
            border+=1
            arr[i],arr[border]=arr[border],arr[i]
    arr[low],arr[border]=arr[border],arr[low]
    return border

n=int(input("Enter the number of elements you want to enter\n"))
print("Enter the elements\n")
arr=[]
for i in range(n):
    arr.append(int(input()))
quick_sort(arr,0,len(arr)-1)

print("Sorted elements are\n")
for i in arr:
    print(f"{i}",end=" ")
