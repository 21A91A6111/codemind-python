t=int(input())
for k in range(t):
    a=int(input())
    if a==0:
        print("YES")
    else:
        arr=[]
        while a>0:
            arr.append(a%10)
            a//=10
        f=0
        arr.sort()
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i]==1:
                f=1
            else:
                f=0
                break
        if f==1:
            print("YES")
        else:
            print("NO")