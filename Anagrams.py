s=input()
x=input()

c=v=0
if len(s)==len(x):
    for i in x:
        if i in s or i.upper() in s or i.lower() in s:
            c+=1
        else:
            v=1
            break
    if(c==len(x) and v!=1):
        print(True)
    else:
        print(False)
else:
    print(False)