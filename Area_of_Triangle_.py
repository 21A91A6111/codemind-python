import math
a,b,c=map(int,input().split())
s=(a+b+c)/2
ar=s*(s-a)*(s-b)*(s-c)
area=math.pow(ar,0.5)
print("{:.2f}".format(area))