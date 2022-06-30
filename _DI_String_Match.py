a=input()
inc=0
dec=len(a)
for i in a:
    if i=='I':
        print(inc,end=" ")
        inc+=1
    elif i=='D':
        print(dec,end=" ")
        dec-=1
print(inc)