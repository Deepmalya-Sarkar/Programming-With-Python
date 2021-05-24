def fact(n):
    if n<=0:
        return 1
    else:
        return n*fact(n-1)

def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)

n=int(input("Enter the number\n"))
f=fact(n)
print(f"{f}")

for i in range(0,n):
    print(f"{fibo(i)}",end=" ")