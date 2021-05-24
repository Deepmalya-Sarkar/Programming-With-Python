age=int(input("Enter your age\n"))

try:
    if age<18:
        raise Exception("Not eligible to vote")
    else:
        print("Eligible to vote")
except Exception as e:
    print("Hi! ",e)


print("out now")