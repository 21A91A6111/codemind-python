arr=input()
ma=c=0
for i in range(len(arr)):
    t=arr[i]
    c=0
    for j in range(i,len(arr)):
        if arr[j]==arr[i] and arr[j-1]==arr[i] and i>0:
            c+=1
            if ma<c:
                ma=c
        else:
            break
print(ma+1)