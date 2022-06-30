a=input()
vow="aeiouAEIOU"
arr=[]
for i in a:
    if i in vow:
        arr.append(i)
i=len(arr)-1
s2=""
for j in a:
    if j in vow:
        s2+=arr[i]
        i-=1
    else:
        s2+=j
print(s2)