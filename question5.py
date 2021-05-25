list1 = ["one","two","three","four","five"]
list2 = [1,2,3,4,5] 
z=[]
f={}
i=0
while i<len(list1):
    new={list1[i]: list2[i]}
    f.update(new)
    i=i+1
print(f)
