def kthLargest(arr, l, r, k):
    '''
    arr : given array
    l : starting index of the array i.e 0
    r : ending index of the array i.e size-1
    k : find kth smallest element and return using this function
    '''
    if k>=0 and k<=r-l+1:
        pos=partition(arr,l,r)
        if pos-l==k-1:
            return arr[pos]
        elif pos-l>k-1:
            return kthLargest(arr,l,pos-1,k)
        return kthLargest(arr,pos+1,r,k-pos+l-1)
    return 999999999999



def pivot(arr,l,r):
    mid=(l+r)//2
    pivot=r
    if arr[l]<arr[mid]:
        if arr[mid]<arr[r]:
            pivot=mid
    elif arr[l]<arr[r]:
        pivot=l
    return pivot

def partition(arr,l,r):
    pivotindex=pivot(arr,l,r)
    pivotvalue=arr[pivotindex]
    arr[l],arr[pivotindex]=arr[pivotindex],arr[l]
    border=l
    
    for i in range(l,r+1):
        if arr[i]>pivotvalue:
            border+=1
            arr[border],arr[i]=arr[i],arr[border]
    arr[l],arr[border]=arr[border],arr[l]
    return border

n=int(input("Enter the number of elements you want to enter\n"))
print("Enter the elements\n")
arr=[]
for i in range(n):
    arr.append(int(input()))
k=int(input("The kth term\n"))
print(kthLargest(arr,0,len(arr)-1,k))
