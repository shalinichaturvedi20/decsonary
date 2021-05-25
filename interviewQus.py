# name=["shalini","neha","sagreeka","amisha",]
# age=[20,21,19,23]
# clas=["10th","12th","7th","9th"]
# f={}
# z=[]
# i=0
# while i<len(name):
#     new={"name": name[i],"age":age[i],"clas":clas[i]}
#     f.update(new)
#     z.append(new)
#     i=i+1
# print(z)


# num1={"a":200,"b":400,"c":600,"d":200,"g":100}
# num2={"a":300,"b":500,"c":800,"e":300,"g":200}
# for key in num1:
#     if key in num2:
#         num2[key]=num1[key]+num2[key]
#     else:
#         num2[key]=num1[key]
# print(num2)            

 
movie=[{"name":"golmal","language":"hindi","date":"1950"},
{"name":"damayanthi","language":"english","date":"2009"},
{"name":"don","language":"tamil","date":"1965"},
{"name":"vivah","language":"british","date":"2005"},
{"name":"bahubali","language":"bangoli","date":"2015"},
{"name":"janwar","language":"hindi","date":"1965"},
{"name":"aitraj","language":"british","date":"1950"},
{"name":"bagwan","language":"tamil","date":"1951"}]
i=0
list_1=[]
for i in movie:
    lan = i["language"]
    list_1.append(lan)
movie = list_1
i=0
a=[]
b=[]
while i<len(movie):
    count=0
    j=0
    while j<len(movie): 
        if movie[i]==movie[j]:
            b.append(movie[j])
            count=count+1
        j=j+1
    k=0
    while k < len(movie):
        if movie[i] not in a:
            a.append(movie[i])
            print(movie[i],count)  
        k=k+1
    i=i+1


# count=0
# k=0
# l=0
# c=0
# m=0
# for i in movie:
#     if i["language"]=="hindi":
#         count+=1
#     if i["language"]=="english":
#         k=k+1
#     if i["language"]=="tamil":
#         l=l+1
#     if i["language"]=="british":
#         c=c+1 
#     if i["language"]=="bangoli":
#         m=m+1
# print("hindi",count)
# print("english",k)
# print("tamil",l) 
# print("british",c)
# print("bangoli",m)      
                    

a=[]
i=0
while i<len(movie):
    j=0
    count=0
    b=[]
    while i<len(b):
        if a[i]==a[i]:
            count=count+1
        j=j+1 
        b.append(a[i])
        b.append(count)
        if b  in a:
            a.append(b)
        i=i+1
print(a) 
