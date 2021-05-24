def common(mat,r,c):
    d=dict()
    for i in range(c):
        d[mat[0][i]]=1
    
    for i in range(1,r):
        for j in range(c):
            if mat[i][j] in d and d[mat[i][j]]==i:
                d[mat[i][j]]+=1
    
    for i in d:
        if d[i]>1:
            print(i,end=" ")




print("Enter the number of rows and columns\n")
r,c=map(int,input().strip().split())
print("Enter the matrix\n")
mat=[]
for i in range(r):
    a=[]
    for j in range(c):
        a.append(int(input()))
    mat.append(a)
common(mat,r,c)
