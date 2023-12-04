t=(1,2,3,(4,5),6,(7,8,9))
for i in range(len(t)):
    if t[i] is tuple:
        if len(t[i])>1:
            for j in range(len(t[i])):
                print(f'{[i]}{[j]}','value',[i][j])
    else:
        print(f'{[i]}',i)