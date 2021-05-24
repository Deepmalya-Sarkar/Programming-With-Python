# def factorial(n):
#     if n<0:
#         return n
#     if n==0 or n==1:
#         return 1
#     else:
#         return n*factorial(n-1)

# print(factorial(0))

def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1)+fibo(n-2)

for i in range(0,5):
    print(fibo(i),end=" ")