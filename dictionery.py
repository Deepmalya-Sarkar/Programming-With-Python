h=dict()
s=input("Enter a string\n")

for i in s:
    if i in h:
        h[i]=h[i]+1
    else:
        h[i]=1
print(h)
h.update({'m':1})
for item,value in h.items():
    print(f"{item}    {value}\n")


print(f"{h.keys()}")