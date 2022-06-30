import math
def pal(s):
    v=s[::-1]
    if v.lower()==s.lower() :
        return 1
    else:
        return 0
s=input()
z=s.split()
c=0
for i in z:
    if(pal(i)==1):
        c+=1
print(c)
