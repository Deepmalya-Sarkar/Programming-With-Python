# li=[
#     [(1,2),(2,3)],
#     [(4,5),(5,6)]   #li[1]
#     ]

# new_li=[i**3 for i in li if i%2==0]
# print(new_li)

# def sq(a):
#     return a*a
# p=list(map(sq,li))
# print(p)

# p=list(filter(lambda i:i%3==0,li))
# print(p)

# for ind,ele in enumerate(li[1]):
#     print(ind," ",ele," ",len(ele))

x=lambda a: pow(a,3)
print(x(3))

li=[1,2,3,4]
def even(x):
    if x%2==0:
        return x
    else:
        return 0
li1=list(filter(lambda x: x%2==0,li))
print(li1)
li2=list(filter(even,li))
print(li2)


def add(display):
    def inner():
        print("Gonna print display")
        display()
        print("Over with display")
    return inner

@add
def display():
    print("Hi there this is display")

display()