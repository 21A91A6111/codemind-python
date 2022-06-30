a=input()
arr=[]
for i in a:
    if i not in arr:
        arr.append(i)
arr2=[]
for i in arr:
    c=0
    for j in a:
        if i==j:
            c+=1
    arr2.append(c)
m1=max(arr2)
m2=0
for i in arr2:
    if i>m2 and i<m1:
        m2=i
if len(arr)==1 or m2==0:
    print(-1)
else:
    for i in range(len(arr)):
        if arr2[i]==m2:
            print(arr[i])
            break