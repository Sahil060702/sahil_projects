list=[1,2,3,4,5]
def check(list):
    if len(list)<0:
        print('None')
    else:
        l=max(list)
        s=min(list)
        print(l,s,sep=' ')
        
check(list)
        

