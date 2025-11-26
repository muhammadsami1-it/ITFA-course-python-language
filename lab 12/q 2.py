# print("hello")
# n = 4
# for i in range(5):
#     print(i ,end=" ")
# for i in range(5,18,4):
#     print(i)
# for i in range(0,8):
#     print(i)
# i=5
# while i<=15:
#     print(i)
#     i+=3
# li= ["a","b","c"]
# for x in li:
#     print(x, end=" ")
# print("")
# tup=("a","c","b")
# for y in tup:
#     print(y, end=" ")
# s={"c","a","b"}
# for x in s:
#     print(x)
# sy={1,2,3,2,1}
# for x in sy:
#     print(x)
# d=dict({'a':123,'b':234})
# for x in d:
    # print("%s : %d"%(x,d[x]))
#     print(f"x: {x}, d[x]: {d[x]}")
# str="abcd"
# for s in str:
#     print(s ,end=" ")
# li=["a","b","c","d"]
# for i in range(len(li)):
#     print(li[i])
# print("lenght of list :", len(li))
# for l in "abcd":
#     pass
# print(l)
# for i in range (5):
#     for j in range (3):
#         print("*", end="")
#     print()
# for i in range (5):
#     for j in range (i):
#         print("*", end="")
#     print()
# print()
# for i in range (5):
#     for j in range (5-i):
#         print("*", end="")
#     print()
# print()
# for i in range (7):
#     for j in range (0,i,2):
#         print(i, end="")
#     print()
li=["a","b","c"]
for i in reversed(li):
    print(i)
num=int(input("enter number to find its factorial:"))
fac=1
for i in range(1,num+1):
    fac=fac*i
print(fac)