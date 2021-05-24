def compressor(s):
    c=0
    new_s=[]
    if len(s)==0:
        return ""
    elif len(s)==1:
        return s+"1"
    elif len(s)>1:   
        for i in range(0,len(s)):
            c=c+1
            if i+1>=len(s) or s[i]!=s[i+1]:
                new_s.append(s[i])
                new_s.append(str(c))
                c=0

    return str(new_s)

s=input("Enter the string\n")
print(compressor(s))
