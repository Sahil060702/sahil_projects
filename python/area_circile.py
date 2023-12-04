import math
'''d=input('Value of diameter:')
r=(d/2)
result=(3.14)*(r)**(2)
print('Area of circle is:',result)'''

d=int(input('Value of diameter:'))
r=float(d/2)
def area_of_circle(r):
    area=3.14*r**2
    return area
print('Area of circle is:',area_of_circle(r))