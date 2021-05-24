def bubble_sort(arr,n):
     for i in range(0,n-1):
         for j in range(0,n-i-1):
             if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
            

n=int(input("Enter the number of elements you want to enter\n"))
print("Enter the elements\n")
arr=[]
for i in range(n):
    arr.append(int(input()))
bubble_sort(arr,n)

print("Sorted elements are\n")
for i in arr:
    print(f"{i}",end=" ")