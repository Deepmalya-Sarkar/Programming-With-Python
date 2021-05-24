def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        for j in range(i-1,-1,-1):
            if arr[j]>key:
                arr[j+1],arr[j]=arr[j],arr[j+1]
            else:
                arr[j+1]=key
                break

n=int(input("Enter the number of elements\n"))
print("Enter the elements")
arr=[]
for i in range(n):
    arr.append(int(input()))

insertion_sort(arr)

print("The sorted elements are ::")
for i in arr:
    print(f"{i}",end=" ")