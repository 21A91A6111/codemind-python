s=input()
arr="abcdefghijklmnopqrstuvwxyz"
c=v=0
for i in arr:
    if i in s or i.upper() in s:
        c+=1
    else:
        v=1
        break
if(v!=1):
    print(True)
else:
    print(False)