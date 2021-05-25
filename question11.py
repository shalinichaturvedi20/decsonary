my_dic={'a':50, 'b':58, 'c':56, 'd':40, 'e':100, 'f':20}
a=[]
for i in my_dic:
    a.append(my_dic[i])
# print(a)
i=0
b=[]
while i<len(a):
    c=max(a)
    a.remove(c)
    b.append(c)
    i=i+1
print(b)    


