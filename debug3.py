i=1
dict1={}
for i in range(1,16):
    if i<=16:
        new_dict={i:i*i}
        i=i+1
        dict1.update(new_dict)
print(dict1) 



