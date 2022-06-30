t=int(input())
for i in range(t):
    a=int(input())
    arr=list(map(int,input().split()))
    m=1
    while True:
        f=0
        for j in range(a-1):
            if arr[j]==m:
                f=0
                break
            else:
                f=1
        if f==1:
            break
        else:
            m+=1
    print(m)