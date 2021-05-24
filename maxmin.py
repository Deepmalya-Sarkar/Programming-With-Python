def maxmin(low,high,arr):
    if low==high:
        arr_max=arr[low]
        arr_min=arr[low]
        return arr_min,arr_max
    elif high==low+1:
        if arr[low]<arr[high]:
            arr_min=arr[low]
            arr_max=arr[high]
        else:
            arr_min=arr[high]
            arr_max=arr[low]
        return arr_min,arr_max
    else:
        mid=(low+high)//2
        arr_min1,arr_max1=maxmin(low,mid,arr)
        arr_min2,arr_max2=maxmin(mid+1,high,arr)
    return min(arr_min1,arr_min2),max(arr_max1,arr_max2)

n=int(input("Enter the limit\n"))
arr=list()
print("Enter the elements\n")
for i in range(n):
    arr.append(int(input()))
arr_min,arr_max=maxmin(0,len(arr)-1,arr)
print(f"Max is {arr_max}. Min is {arr_min}.")