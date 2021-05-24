def reverseEachWord(s):
    s_list=s.split(" ")
    new_s_list=[]
    for word in s_list:
        new_word=word[::-1]
        new_s_list.append(new_word)
    print(" ".join(new_s_list))

s="deep sarkar"
reverseEachWord(s)