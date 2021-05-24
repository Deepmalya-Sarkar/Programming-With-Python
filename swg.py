import random
us=0
comp=0
a=1

while a<=3:
    game=["Snake","Water","Gun"]
    print("Press S for snake")
    print("Press W for water")
    print("Press G for gun")

    ch=input("Enter your choice\n")
    comp_ch=random.choice(game)

    print(f"computer's choice is {comp_ch}")


    if ch=="S" and comp_ch=="Snake" or ch=="W" and comp_ch=="Water" or ch=="G" and comp_ch=="Gun":
        continue
    else:
        if ch=="S" and comp_ch=="Water":
            us=us+1
        elif ch=="G" and comp_ch=="Snake":
            us=us+1
        elif ch=="W" and comp_ch=="Gun":
            us=us+1
        else:
            comp=comp+1
    
    a=a+1

if us>comp:
    print("You are the winner\n")
elif comp>us:
    print("Computer is the winner")
else:
    print("It's a tie")