l=[1,2,3,4]
l1=[1,2]
dif=[]
for i in l:
    if i not in l1:
        dif.append(i)
print(dif)