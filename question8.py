i=1
student=[]
marks=[]
while i<=10:
    user=input("enter the student name")
    student.append(user)
    mark=int(input("enter the student marks"))
    marks.append(mark)
    i+=1
d=dict()
n=marks[0]
for i in student:
    d[i]=n
    n+=1
print(d)        
