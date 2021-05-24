def counting(amt):
    notes={2000:0,500:0,200:0,100:0,50:0,20:0,10:0,5:0,2:0,1:0}
    for element in notes:
        if amt<=0:
            break
        else:
            c=amt//element
            if c>0:
                notes[element]=c
            amt=amt-(element*c)
    for element in notes:
        print(f"{element}-{notes[element]}")

amt=int(input("Enter the amount\n"))
counting(amt)

