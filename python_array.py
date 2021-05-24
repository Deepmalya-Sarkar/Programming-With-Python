import array as arr
vals=arr.array('i',[1,2,3,4,5])
# vals.append(6)
# for i in vals:
#     print(i)
print(vals.typecode)
val2=arr.array(vals.typecode,[i for i in vals])
print(val2)


# vals=arr.array('i',[])
# print("Insert elements")
# for i in range(0,5):
#     vals.append(int(input()))
# print("Printing...................")
# vals.reverse()
# vals.remove(5)
# f=0
# key=int(input("Enter the element you want to search\n"))
# for i in vals:
#     if key==i:
#         print(vals.index(i)+1)
#         f=1
#         break
# if f==0:
#     print("Element not present")


