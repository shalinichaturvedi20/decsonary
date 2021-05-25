my_dict = {'data1':100,'data2': -54,'data3': 247} 
list1 = []
for i in my_dict:
        list1.append(my_dict[i])
i = 0
s = 0
while i < len(list1):
        s = s + list1[i]
        i = i + 1
print(s)