def merge_sort(arr,first,last):
    if first<last:
        mid=(first+last)//2
        merge_sort(arr,first,mid)
        merge_sort(arr,mid+1,last)
        merge(arr,first,mid,last)

def merge(arr,first,mid,last):
    left=arr[first:mid+1]
    right=arr[mid+1:last+1]
    
    i=0
    j=0
    k=first
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[j]
            j+=1
        k+=1
    
    while i<len(left):
        arr[k]=left[i]
        i+=1
        k+=1

    while j<len(right):
        arr[k]=right[j]
        j+=1
        k+=1

n=int(input("Enter the number of numbers\n"))
arr=[]
print("Enter the elements\n")
for i in range(n):
    arr.append(int(input()))
merge_sort(arr,0,n-1)

print("Sorted elements are\n")
for i in arr:
    print(f"{i}",end=" ")


    