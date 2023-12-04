list=[1,2,3,4,5,6]

var=2
temp=0
list2=[]

for i in range(len(list)):
    for i in list:
        temp=var*i
        list2.append(temp)
    print(list2)
    break