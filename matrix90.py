def rotateMatrix(n):
    m=list()
    print("enter the matrix")
    for i in range(n):
        a=[]
        for j in range(n):
            a.append(int(input()))
        m.append(a)

    print("Original")
    for i in range(n):
        for j in range(n):
            print(m[i][j],end=" ")
        print()

    #transposing
    for i in range(n):
        for j in range(i,n):
            temp=m[i][j]
            m[i][j]=m[j][i]
            m[j][i]=temp
    
    for i in range(n):
        li=0
        ri=len(m[i])-1

        while li<ri:
            temp=m[i][li]
            m[i][li]=m[i][ri]
            m[i][ri]=temp
            li+=1
            ri-=1
    
    print("After rotation")
    for i in range(n):
        for j in range(n):
            print(m[i][j],end=" ")
        print()

    



n=int(input("Enter the length\n"))
rotateMatrix(n)