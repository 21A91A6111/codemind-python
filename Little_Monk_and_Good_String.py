a=input()
c=ma=0
vow="aeiouAEIOU"
for i in range(len(a)):
    c=0
    for j in range(i,len(a)):
        if a[j] in vow:
            c+=1
            if ma<c:
                ma=c
        else:
            break
print(ma)