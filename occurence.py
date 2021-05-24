s=input("Enter a string\n")
word=input("Enter a word\n")
n=int(input("Enter number of occurence you want to delete"))
li=s.split(" ")
lis=[]
c=0
print(li)
for i in li:
    if i==word:
        c=c+1
        if c==n:
            continue
        else:
            lis.append(i)
    else:
        lis.append(i)

print(lis)