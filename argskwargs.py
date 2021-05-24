def printing(*args):
    print("Printing")
    for i in args:
        print(i)

def inputing():
    li=[]
    print("enter 5 numbers")
    for i in range(5):
        li.append(int(input()))

    return li

myli=inputing()

printing(*myli)
