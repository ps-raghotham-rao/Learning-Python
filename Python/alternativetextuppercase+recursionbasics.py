






# s="This is a test"
# l=""
# k=0
# i=0
# c=0
# while(len(s)>i):
#     if s[i] == " ":
#         i+=1
#         l+=" "
#         pass
#     if (c)%2==0:
#         l+=s[i].upper()
#     else:
#         l+=s[i].lower()
#     i+=1
#     c+=1
# print(l)


# c=0
# s="this is a test"
# s=s.split(' ')
# l=""
# for i in s:
#     c=0
#     for j in i:
#         if c%2 == 0:
#             l+=j.upper()
#         else:     
#             l+=j.lower()
#         c+=1
#     l+=" "
# print(l)    

f=1
def fact(n):

    global f
    if n == 1:
        return 1
    fact(n-1)

    f=f*n
    print(n)

fact(5)
print(f)