def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)

n=int(input("Enter n\n"))
for i in range(0,n):
    print(f"{fibo(i)} ",end="")