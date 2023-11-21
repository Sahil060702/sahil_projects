'''list=[1,4,3]
result=sum(list)
print(result)'''


def add(n):
    sum=0
    while (n>0):
        dig=n%10
        sum=sum+dig
        n=n//10
add(143)
print(sum)



'''def s_o_d(n):
    if n<10:
        return n
    else:
        return n%10+s_o_d(n//10)
    
print(s_o_d(143))'''


   
