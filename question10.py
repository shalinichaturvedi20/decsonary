dic =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}  
count=0
for i in dic:
    if dic[i]:
        count = count + len(dic[i])
print(count)
