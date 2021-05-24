# s=input("Enter a string\n")
# print(s[::-1])
# print("".join(sorted(s,reverse=True)))

# print(list(filter(lambda x: x%2==0,list(range(1,51)))))

# mystr="I am Deep. Deep Deep is a very good boy"
# print(mystr.count("Deep"))
# a=0
# b=0
# n=10
# print(f"{a} {b}",end="")
# for i in range(1,n-1):
#     if i%2!=0:
#         a+=7
#         print(f" {a}",end="")
#     else:
#         b+=6     
#         print(f" {b}",end="")
    
# if n%2!=0:
#     print(f"\n{a}")
# else:
#     print(f"\n{b}")

# s=input("Enter the string\n")
# li=[]
# size=len(s)
# si=""
# li=s.split()
# for i in li:
#     si=si+i[::-1]+" "
# print(si)


# word="xyzbyxzaaccdfvbgyxz"
# test="zyx"
# test_length=len(test)
# word_length=len(word)
# c=0

# for i in range(0,word_length):
#     s=word[i:i+test_length]
#     if sorted(test)==sorted(s):
#         c=c+1

# print(f"The number of anagrams are {c}")



# s=input("Enter a string\n")
# s_li=s.split()
# for ind,ele in enumerate(s_li):
#     new_ele=ele[::-1]
#     s_li[ind]=new_ele
# new_s=" ".join(s_li)
# print(f"{new_s}")
# print(f"length of old string is {len(s)} and length of new string is {len(new_s)}")


text="madam"
word="ma"
len_text=len(text)
len_word=len(word)
c=0
for i in range(len_text):
    check=text[i:i+len_word]
    if sorted(word)==sorted(check):
        print(f"{check}")
        c=c+1

print(f"The total number of anagrams is {c}")