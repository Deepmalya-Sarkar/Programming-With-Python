def selection_sort(arr):
    for i in range(len(arr)):
        min_ind=i

        for j in range(i+1,len(arr)):
            if arr[min_ind]>arr[j]:
                min_ind=j
        
        arr[min_ind],arr[i]=arr[i],arr[min_ind]

n=int(input("Enter the number of elements\n"))
print("Enter the elements\n")
arr=[]
for i in range(n):
    arr.append(int(input()))

selection_sort(arr)

print("Sorted elements are::")
for i in arr:
    print(f"{i}",end=" ")
