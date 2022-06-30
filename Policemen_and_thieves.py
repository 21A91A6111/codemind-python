t=int(input())
for l in range(t):
    a,b=map(int,input().split())
    c=0
    for i in range(a):
        s=input()
        arr=[]
        for j in s:
            if j=='P' or j=='T':
                arr.append(j)
        for j in range(a):
            if arr[j]=='P':
                for k in range(a):
                    if arr[k]=='T':
                        if abs(j-k)<=b:
                            c+=1
                            arr[k]='0'
                            break
                continue
    print(c)