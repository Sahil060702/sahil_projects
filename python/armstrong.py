Num=int (input ('Enter a number: '))
x=len(str (Num) )
sum=0
temp=Num
while temp>0:
    digit=temp % 10 
    sum += digit **x
    temp //=10

if Num==sum:
    print('It is an armstfong number')
else:
    print('Its not an armstrong number')