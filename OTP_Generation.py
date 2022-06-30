s=input()
o="13579"
e="02468"
for i in s:
    if i in e:
        continue
    elif i in o:
        v=ord(i)-48
        print(v**2,end="")

