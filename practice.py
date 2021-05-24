# print(list(range(1,10+1)))
# print(range(1,11))
# filter(function,iterable object)
# print(list(filter(lambda x: x%2==0,list(range(1,11)))))

# print([i for i in range(1,11) if i %2!=0])

# def wrapper_func(some):
# 	def inner():
# 		print("I am inside inner")
# 		some()
# 	return inner
# @wrapper_func
# def some():
# 	print("Hi I am a good boy")
# some()

# def gen():
#     for i in range(1,6):
#         yield i
# y=gen()
# print(y.__next__())
# print(y.__next__())
# print(y.__next__())

# li=[i for i in range(1,11) if i%2==0]
# li.reverse()
# print(li)

c=1
for i in range(1,6):
    for j in range(1,i+1):
        if c%2==0:
            print("0",end="")
        else:
            print("1",end="")
        c=c+1
    print()

# c=1
# for i in range(1,6):
#     for j in range(1,i+1):
#         if c%2!=0:
#             print("1",end="")
#         else:
#             print("0",end="")
#         c=c+1
#     print()
    