arr=[4,-4,3,-3]
count=0
n=len(arr)
arr.sort() 
for i in range(n-3):
    for j in range(i+1,n-2):
        l=j+1
        r=n-1
        while l<r:
            if arr[i]+arr[j]+arr[l]+arr[r]==0:
                count+=1
                r-=1
                l+=1
            elif arr[i]+arr[j]+arr[l]+arr[r]<0:
                l+=1
            else:
                r-=1
print(count)