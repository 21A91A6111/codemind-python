import math
s=input()
s.lower()
v=s[::-1]
if v.lower()==s.lower() :
    print(True)
else:
    print(False)