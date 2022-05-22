import math
n=int(input())
while n:
    i = int(input())
    r=math.sqrt(i)
    if int(r)**2 == i:
        print('True')
    else:
        print('False')
    n-=1
    