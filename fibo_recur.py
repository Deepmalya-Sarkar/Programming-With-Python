def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)

n=int(input("Enter the number of terms\n"))
for i in range(0,n):
    print(fibo(i),end=" ")