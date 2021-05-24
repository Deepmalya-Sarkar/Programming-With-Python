def alternate(a,n):
    pos=1
    neg=0
    i=0
    if len(a)<=1:
        return a
    else:
        while i<n:
            if a[i]<0 and neg<n:
               a[i],a[neg]=a[neg],a[i]
               neg+=2
            i+=1
        i=0
        while i<n:
            if a[i]>=0 and pos<n:
                a[i],a[pos]=a[pos],a[i]
                pos+=2
            i+=1
    
        return a

        

n=int(input("Enter the length\n"))
a=[]
for i in range(n):
    a.append(int(input()))

arr=alternate(a,n)

for i in arr:
    print(f"{i}",end=" ")