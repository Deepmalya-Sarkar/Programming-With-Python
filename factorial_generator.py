def factorial(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    yield f

g=factorial(5)
print(g.__next__())
