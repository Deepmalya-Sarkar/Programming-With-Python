import datetime
def getdate():
    return datetime.datetime.now().ctime()

print("1 for Rohan\n")
print("2 for Harry\n")
choice=int(input())
if choice==1:
    print("1 for Diet\n")
    print("2 for excercise\n")
    ch=int(input())
    if ch==1:
        f=open("rohan_diet.txt","r+")
        print(f.read())
        food=input("Enter what you ate\n")
        time=getdate()
        f.write(time)
        f.write(food)
        print("Successfully edited")
        f.close()
    elif ch==2:
        f=open("rohan_exer.txt","r+")
        print(f.read())
        exer=input("Enter what exercises you did\n")
        time=getdate()
        f.write(time)
        f.write(exer)
        print("Successfully edited")
        f.close()
    else:
        print("Wrong Choice")


elif choice==2:
    print("1 for Diet\n")
    print("2 for excercise\n")
    ch=int(input())
    if ch==1:
        f=open("harry_diet.txt","r+")
        print(f.read())
        food=input("Enter what you ate\n")
        time=getdate()
        f.write(time)
        f.write(food)
        print("Successfully edited")
        f.close()
    elif ch==2:
        f=open("harry_exer.txt","r+")
        print(f.read())
        exer=input("Enter what exercises you did\n")
        time=getdate()
        f.write(time)
        f.write(exer)
        print("Successfully edited")
        f.close()
    else:
        print("Wrong Choice")
else:
    print("Wrong choice")
