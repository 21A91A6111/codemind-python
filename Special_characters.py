d="@#!*&^$/(){}[],."
eve="04268"
odd="13579"
w="0123456789"
a=[]
e=[]
o=[]
n=input()
c=0
x=y=0
for i in n:
    if i in d:
        c+=1
if c%2==0:
    for i in range(len(n)):
        if n[i] in w:
            a.append(n[i])
    for i in range(len(a)):
        if (ord(a[i]))%2==0:
            e.append(a[i])
        else:
            o.append(a[i])
    while(x<len(e) and y<len(o)):
        print(e[x],end="")
        x+=1
        print(o[y],end="")
        y+=1
    while(x<len(e)):
        print(e[x],end="")
        x+=1
    while(y<len(o)):
        print(o[y],end="")
        y+=1
else:
    for i in range(len(n)):
        if n[i] in w:
            a.append(n[i])
    for i in range(len(a)):
        if (ord(a[i]))%2==0:
            e.append(a[i])
        else:
            o.append(a[i])
    x=y=0
    while(x<len(e) and y<len(o)):
        print(o[y],end="")
        y+=1
        print(e[x],end="")
        x+=1
    while(y<len(o)):
        print(o[y],end="")
        y+=1
    while(x<len(e)):
        print(e[x],end="")
        x+=1