def max_subarray(arr):
    msf=arr[0]
    cm=arr[0]
   

    for i in range(0,len(arr)):
        cm=max(arr[i],cm+arr[i])
        msf=max(cm,msf)
        
    return msf

arr=[-2,-3,4,-1,-2,1,5,-3]
print(f"the max sum is {max_subarray(arr)}")