def fact(n):
    if n<=1:
        return 1
    else:
        return n*fact(n-1)

def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)

n=int(input("Enter the number\n"))
s=0
print(f"The factorial is {fact(n)}")
for i in range(0,n):
    x=fibo(i)
    s=s+x
    print(f"{x}",end=" ")
print(f"\nThe sum of fibonacci is {s}")