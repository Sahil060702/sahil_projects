age=int(input("enter your age"))
if(age<=18):
    print('Children')
elif(age>=19 and age<=60):
    print('adult')
elif(age>60 and age<=95):
    print('senior citizen')
elif(age>96):
    print('overtime')

    